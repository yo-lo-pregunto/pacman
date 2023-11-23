from constants import *
from ghost import Ghost
from pacman import Pacman
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

spawn = maze.get_spawn_loc("Huayra")
ghost = Ghost(spawn, "./graphs/ghost/blue ghost/")

spawn = maze.get_spawn_loc("Pancracio")
ghost1 = Ghost(spawn, "./graphs/ghost/red ghost/")

spawn = maze.get_spawn_loc("Tiburcio")
ghost2 = Ghost(spawn, "./graphs/ghost/orange ghost/")

spawn = maze.get_spawn_loc("Petra")
ghost3 = Ghost(spawn, "./graphs/ghost/pink ghost/")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            keydown = True

    screen.blit(bg, (150, 100))
    screen.blit(header, header_rect)

    # Maze
    maze.render(screen)

    # Pacman
    pacman.update(keydown)
    pacman.render(screen)

    # Ghosts
    ghost.update()
    ghost.render(screen)

    ghost1.update()
    ghost1.render(screen)

    ghost2.update()
    ghost2.render(screen)

    ghost3.update()
    ghost3.render(screen)

    keydown = False
    pygame.display.update()
    clock.tick(FRAME_RATE)
