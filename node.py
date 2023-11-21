from typing import Self
from constants import *
from point import Vector
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Node():
    def __init__(self, x: int, y: int, index: int, constrains: list[int]) -> None:
        self.index = index
        self.position = Vector(x, y)
        self.constrains = constrains
        self.neighbors: list[Self | None] = [None for _ in range(N_NEIGHBORS)]

    def add_neighbor(self, neighboard: Self, location: int) -> None:
        if location in self.constrains:
            return
        if not self.neighbors[location]:
            self.neighbors[location] = neighboard
        else:
            d1 = self.position.magnitude(neighboard.position)
            d2 = self.position.magnitude(self.neighbors[location].position)
            if d1 < d2:
                self.neighbors[location] = neighboard

    def render(self, screen: pygame.Surface):
        line_start = self.position.asTuple()
        pygame.draw.circle(screen, RED, self.position.asTuple(), 7)
        for n in range(N_NEIGHBORS):
            if self.neighbors[n] is not None:
                line_end = self.neighbors[n].position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end)
