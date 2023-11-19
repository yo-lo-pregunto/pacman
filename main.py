from constants import *
from pacman import Pacman
from point import Point
from node import Node
import pygame

# Image path
BACKGROUND = "./graphs/maze_2.png"

# Init the enginee
pygame.init()

window = pygame.display.set_mode(WINDOWS_SIZE, pygame.NOFRAME)
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

# Player
pacman = Pacman(Point(WINDOWS_SIZE[0] // 2,  558), "./graphs/pac man & life counter & death/pac man/")

# Nodes
"""
pacman point = 430,558
distance between walls = 29
"""
node = Node(Point(430, 558))
node.add_neighbor(Point(430, 600), DOWN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            keydown = True

    window.blit(bg, (150, 100))
    window.blit(header, header_rect)

    #Node
    node.render(window)

    # Pacman
    pacman.update(keydown)
    pacman.render(window)

    keydown = False
    pygame.display.update()
    clock.tick(FRAME_RATE)
