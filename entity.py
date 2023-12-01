import pygame
from constants import *
from point import Vector
from node import Node

class Entity():
    def __init__(self, node: Node, size: Vector = Vector(TILE_W, TILE_H)) -> None:
        self.velocity = Vector(0, 0)
        self.size = size
        self.source = node
        self.target = None
        self.set_position()
        self.image = None
        self.direction: int = STOP
        self.orientation = {}
        self.home = node
        self.compass = {
                STOP: Vector(0, 0),
                LEFT: Vector(-1, 0),
                RIGHT: Vector(1, 0),
                UP: Vector(0, -1),
                DOWN: Vector(0, 1),
                }

    def set_position(self):
        self.position = self.source.position.copy()

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        if self.image:
            adjust = self.position - (self.size / 2)
            screen.blit(self.image, adjust.asTuple())
