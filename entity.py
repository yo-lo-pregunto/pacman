import pygame
from pygame import Surface
from constants import *
from point import Point

class Object():
    def __init__(self, pos: Point, size: Size, image: Surface) -> None:
        super().__init__()
        self.pos = pos
        self.size = size
        self.direction = STOP
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect(center = self.pos)

class Entity():
    def __init__(self, pos: Point, size: Point) -> None:
        self.velocity = Point(0, 0)
        self.size = size
        self.pos = pos 
        self.pos.y -= (size.y // 2)
        self.pos.x -= (size.x // 2)
        self.image = None
        self.direction: int = STOP
        self.orientation = {}

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        if self.image:
            screen.blit(self.image, self.pos.asTuple())
