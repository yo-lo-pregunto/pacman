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
        self.old_direction = RIGHT
        self.direction = RIGHT
        self.target = self.source.neighbors[self.direction]
        self.find_next_direction()
        self.compass = {
                STOP: Vector(0, 0),
                LEFT: Vector(-1, 0),
                RIGHT: Vector(1, 0),
                UP: Vector(0, -1),
                DOWN: Vector(0, 1),
                }
        self.speed = SPEED
        self.velocity = Vector(-SPEED, 0)
        self.edges = [self.direction, self.direction ^ 1]

    def get_input(self, keydown) -> int:
        if not keydown:
            return STOP

        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            return UP
        if keys[pygame.K_j]:
            return DOWN
        if keys[pygame.K_l]:
            return RIGHT
        if keys[pygame.K_h]:
            return LEFT
        return STOP

    def update_image(self) -> pygame.Surface:
        new_frame = self.animation.get_frame()
        new_image = self.tileset[new_frame]

        if self.old_direction == LEFT or self.direction == LEFT:
            new_image = pygame.transform.flip(new_image, True, False)

        return new_image


    def rotate(self, image: pygame.Surface):
        if self.old_direction == UP or self.direction == UP:
            image = pygame.transform.rotate(image, 90)
        elif self.old_direction == DOWN or self.direction == DOWN:
            image = pygame.transform.rotate(image, -90)
        return image

    def update(self, keydown: int):

        self.position += self.compass[self.direction] * self.speed
        image = self.update_image()
        self.image = self.rotate(image)

        direction = self.get_input(keydown)

        if direction == self.direction ^ 1:
            self.direction = direction
            self.old_direction = self.direction
            self.source, self.target = self.target, self.source
            self.find_next_direction()
        else:
            if self.target.neighbors[direction] and direction != STOP:
                self.next_direction = direction
                self.old_direction = self.direction

        d = self.position.magnitude(self.target.position)

        if d <= self.speed:
            self.source, self.target = self.target, self.target.neighbors[self.next_direction]
            if self.next_direction != STOP:
                self.old_direction = self.next_direction
            self.direction = self.next_direction
            self.find_next_direction()

    def find_next_direction(self):
        if self.target.neighbors[self.direction]:
            self.next_direction = self.direction
        else:
            self.next_direction = STOP

