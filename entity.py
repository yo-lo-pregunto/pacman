import pygame
from constants import *
from point import Vector
from node import Node

class Entity():
    def __init__(self, node: Node, size: Vector) -> None:
        self.velocity = Vector(0, 0)
        self.size = size
        self.source = node
        self.set_position()
        self.image = None
        self.direction: int = STOP
        self.orientation = {}

    def set_position(self):
        self.position = self.source.position.copy()

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        if self.image:
            screen.blit(self.image, self.position.asTuple())
