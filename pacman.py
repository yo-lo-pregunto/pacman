import pygame
from pygame import KEYDOWN, Surface
from typing import TypeAlias
import os

Point: TypeAlias = list[int]
Size: TypeAlias = tuple[int, int]

WINDOWS_SIZE = (860, 820)
IMAGE_SIZE = (560, 620)
WINDOWS_TITLE = "󰮯 PAC - MAN 󰮯"

HEADER_LOC = (WINDOWS_SIZE[0] / 2, 50)

PACMAN_SPAW_LOC = [WINDOWS_SIZE[0] // 2,  560]

DIR_LEFT = 0
DIR_RIGHT = 1
DIR_UP = 2
DIR_DOWN = 3

# Game Constants
FRAME_RATE = 60
ANIMATION_FRAME_RATE = 3
SPEED = 2

class Object(pygame.sprite.Sprite):
    """
    pos = (x, y)
    size = (w, h)
    """
    def __init__(self, pos: Point, size: Size, image: Surface) -> None:
        super().__init__()
        self.pos = pos
        self.size = size
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect(center = self.pos)

class Pacman(Object):
    def __init__(self, pos: Point, size: Size, dir: str) -> None:
        self.tileset = load_tileset(dir, size)
        self.frame = 0
        self.frames = [*range(len(self.tileset))]
        self.frame_timer = 0
        self.direction = DIR_LEFT
        self.velocity = [0, 0]
        self.orientation = {
                DIR_LEFT: {"flip": False, "angle": 0},
                DIR_RIGHT: {"flip": True, "angle": 0},
                DIR_UP: {"flip": False, "angle": 90},
                DIR_DOWN: {"flip": False, "angle": -90},
                }

        super().__init__(pos, size, self.tileset[self.frames[0]])

    def player_input(self) -> tuple[int, list[int]]:
        global keydown

        if not keydown:
            return self.direction, self.velocity

        keydown = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            return DIR_UP, [0, -SPEED]
        if keys[pygame.K_j]:
            return DIR_DOWN, [0, SPEED]
        if keys[pygame.K_h]:
            return DIR_RIGHT, [-SPEED, 0]
        if keys[pygame.K_l]:
            return DIR_LEFT, [SPEED, 0]
        return self.direction, self.velocity

    def animation(self):
        self.frame_timer += 1
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.frame_timer < ANIMATION_FRAME_RATE:
            return

        self.frame_timer = 0
        self.frame += 1

        if self.frame >= len(self.frames):
            self.frame = 0

        new_image = self.tileset[self.frame]
        new_rect = self.rect
        if self.orientation[self.direction]["flip"]:
            new_image = pygame.transform.flip(new_image, self.orientation[self.direction]["flip"], False)

        if self.orientation[self.direction]["angle"]:
            x, y = self.rect.x, self.rect.y
            new_image = pygame.transform.rotate(new_image, self.orientation[self.direction]["angle"])
            new_rect = new_image.get_rect(center = (x, y))
            new_rect.x = x
            new_rect.y = y

        self.image = new_image
        self.rect = new_rect

    def update(self):
        self.direction, self.velocity = self.player_input()
        self.animation()


def load_tileset(dir: str, size: Size) -> list[Surface]:
    files = [f.path for f in os.scandir(dir) if f.is_file()]
    files = sorted(files)
    tileset: list[Surface] = []

    for f in files:
        image = pygame.image.load(f).convert_alpha()
        tileset.append(pygame.transform.scale(image, size))
    return tileset


# Image path
BACKGROUND = "./graphs/maze_2.png"

# Init the enginee
pygame.init()

window = pygame.display.set_mode(WINDOWS_SIZE, pygame.NOFRAME)
clock = pygame.time.Clock()
font = pygame.font.Font("./fonts/FiraCodeNerdFont-Bold.ttf", 50)

keydown = False

# Header
header = font.render(WINDOWS_TITLE, False, "#fdff00")
header_rect = header.get_rect(center = HEADER_LOC)

pygame.display.set_caption(WINDOWS_TITLE)

# Background
bg = pygame.image.load(BACKGROUND).convert()
bg = pygame.transform.scale(bg, IMAGE_SIZE)

# Player
pacman = pygame.sprite.GroupSingle()
pacman.add(Pacman(PACMAN_SPAW_LOC, (15, 15), "./graphs/pac man & life counter & death/pac man"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            keydown = True

    window.blit(bg, (150, 100))
    window.blit(header, header_rect)

    # Pacman
    pacman.draw(window)
    pacman.update()

    pygame.display.update()
    clock.tick(FRAME_RATE)
