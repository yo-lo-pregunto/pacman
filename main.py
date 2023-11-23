from constants import *
from pacman import Pacman
from point import Vector
from maze import Maze
from node import Node
import pygame

# Image path
BACKGROUND = "./graphs/maze_2.png"

# Init the enginee
pygame.init()

screen = pygame.display.set_mode(WINDOWS_SIZE, pygame.NOFRAME)
clock = pygame.time.Clock()
font = pygame.font.Font("./fonts/FiraCodeNerdFont-Bold.ttf", 50)

# Header
header = font.render(WINDOWS_TITLE, False, "#fdff00")
header_rect = header.get_rect(center = HEADER_LOC)

pygame.display.set_caption(WINDOWS_TITLE)

# Background
bg = pygame.image.load(BACKGROUND).convert()
bg = pygame.transform.scale(bg, IMAGE_SIZE)

keydown = False


# Nodes
maze = Maze()

# Player
spawn = maze.get_spawn_loc("Pacman")
pacman = Pacman(spawn, "./graphs/pac man & life counter & death/pac man/")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            keydown = True

    screen.blit(bg, (150, 100))
    screen.blit(header, header_rect)

    # Maze
    #maze.render(screen)

    # Pacman
    pacman.update(keydown)
    pacman.render(screen)

    keydown = False
    pygame.display.update()
    clock.tick(FRAME_RATE)
