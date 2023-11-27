from constants import *
from ghost import Ghost
from pacman import Pacman
from maze import Maze
from node import Node
import pygame

from pill import PillGroup
from text import TextGroup

# Image path
BACKGROUND = "./graphs/maze_2.png"

# Init the enginee
pygame.init()

screen = pygame.display.set_mode(WINDOWS_SIZE, pygame.NOFRAME)
clock = pygame.time.Clock()
font = pygame.font.Font("./fonts/FiraCodeNerdFont-Bold.ttf", 50)

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

pill_group = PillGroup(maze.nodes)

text = TextGroup()

pause = True

def render():
    global screen
    screen.blit(bg, (150, 100))
    pill_group.render(screen)
    pacman.render(screen)
    ghost.render(screen)
    ghost1.render(screen)
    ghost2.render(screen)
    ghost3.render(screen)
    text.render(screen)
    pygame.display.update()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            keydown = True
        if event.type == pygame.KEYDOWN and pygame.K_SPACE == event.key:
            pause = not pause


    if not pause:
        # Maze
        #maze.render(screen)

        for pill in pill_group.pills:
            if pacman.eat_pill(pill):
                pill.visible = False
                text.update_score(pill.points)

        # Pacman
        pacman.update(keydown)

        # Ghosts
        ghost.update()

        ghost1.update()

        ghost2.update()

        ghost3.update()

        keydown = False

    render()
    clock.tick(FRAME_RATE)
