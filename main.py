from constants import *
from ghost import Ghosts
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

spawn = []
spawn.append(maze.get_spawn_loc("Huayra"))
spawn.append(maze.get_spawn_loc("Pancracio"))
spawn.append(maze.get_spawn_loc("Tiburcio"))
spawn.append(maze.get_spawn_loc("Petra"))

ghosts = Ghosts(spawn)

pill_group = PillGroup(maze.nodes)

text = TextGroup()

pause = True

def render():
    global screen
    screen.blit(bg, (150, 100))
    pill_group.render(screen)
    pacman.render(screen)
    ghosts.render(screen)
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
        for ghost in ghosts.ghosts.values():
            ghost.update()
            if pacman.check_collision(ghost.position):
                print("Looser")
                exit()

        keydown = False

    render()
    clock.tick(FRAME_RATE)
