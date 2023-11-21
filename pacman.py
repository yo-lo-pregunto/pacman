from pygame.math import VectorIterator
from animation import Animation
from constants import *
from entity import Entity
from point import Vector
from utils import load_tileset
from node import Node
import pygame

class Pacman(Entity):
    def __init__(self, node: Node, direction: str,
                 size: Vector = Vector(TILE_W, TILE_H)) -> None:

        super().__init__(node, size)
        self.tileset = load_tileset(direction, size)
        self.animation = Animation(0, [*range(len(self.tileset))])
        self.image = self.tileset[0]
        self.direction = LEFT
        self.target = self.source.neighbors[self.direction]
        self.velocity = Vector(-SPEED, 0)
        self.edges = [self.direction, self.direction ^ 1]

    def get_input(self, keydown) -> tuple[int, Vector]:
        if not keydown:
            return STOP, self.velocity

        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            return UP, Vector(0, -SPEED)
        if keys[pygame.K_j]:
            return DOWN,Vector(0, SPEED) 
        if keys[pygame.K_l]:
            return RIGHT, Vector(SPEED, 0)
        if keys[pygame.K_h]:
            return LEFT, Vector(-SPEED, 0)
        return STOP, self.velocity

    def update_image(self) -> pygame.Surface:
        new_frame = self.animation.get_frame()
        new_image = self.tileset[new_frame]

        if self.direction == LEFT:
            new_image = pygame.transform.flip(new_image, True, False)

        return new_image


    def rotate(self, image: pygame.Surface):
        if self.direction == UP:
            image = pygame.transform.rotate(image, 90)
        elif self.direction == DOWN:
            image = pygame.transform.rotate(image, -90)
        return image

    def update(self, keydown: int):

        direction, velocity = self.get_input(keydown)

        if self.source.neighbors[direction] and direction != STOP:
            print(f"direction: {direction}")
            self.position = self.source.neighbors[direction].position.copy()
            print("new loc", self.position)
            self.source = self.source.neighbors[direction]

        self.direction = STOP

        image = self.update_image()
        self.image = self.rotate(image)
