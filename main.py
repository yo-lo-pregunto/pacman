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
"""
1. 300, 558
2. 600, 558
3. 300, 200
4. 600, 200
5. 430, 350
pacman point = 430,558
distance between walls = 28
"""
maze = Maze()
#node = Node(Point(430, 558))
#node1 = Node(Point(300, 558))
#node2 = Node(Point(600, 558))
#node3 = Node(Point(300, 200))
#node4 = Node(Point(600, 200))
#node5 = Node(Point(430, 350))
#node6 = Node(Point(600, 350))
## Connect
#node.add_neighbor(node1.position, RIGHT)
#node.add_neighbor(node2.position, LEFT)
#node.add_neighbor(node5.position, UP)
#node1.add_neighbor(node.position, RIGHT)
#node1.add_neighbor(node3.position, UP)
#node3.add_neighbor(node1.position, DOWN)
#node3.add_neighbor(node4.position, RIGHT)
#node4.add_neighbor(node3.position, LEFT)
#node4.add_neighbor(node6.position, DOWN)
#node2.add_neighbor(node.position, LEFT)
#node2.add_neighbor(node6.position, UP)
#node5.add_neighbor(node.position, DOWN)
#node5.add_neighbor(node6.position, RIGHT)
#node6.add_neighbor(node5.position, LEFT)
#node6.add_neighbor(node2.position, DOWN)

# Player
spawn = maze.get_spawn_loc(PACMAN)
pacman = Pacman(spawn, "./graphs/pac man & life counter & death/pac man/")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            keydown = True

    screen.blit(bg, (150, 100))
    screen.blit(header, header_rect)

    #Node
    #node.render(window)
    #node1.render(window)
    #node2.render(window)
    #node3.render(window)
    #node4.render(window)
    #node5.render(window)
    #node6.render(window)
    # Maze
    maze.render(screen)

    # Pacman
    pacman.update(keydown)
    pacman.render(screen)

    keydown = False
    pygame.display.update()
    clock.tick(FRAME_RATE)
