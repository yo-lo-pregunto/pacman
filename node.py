from constants import N_NEIGHBORS
from point import Point
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Node():
    def __init__(self, position: Point) -> None:
        self.position = position
        self.neighbors: list[Point | None] = [None for _ in range(N_NEIGHBORS)]

    def add_neighbor(self, neighboard: Point, location: int) -> None:
        if location < N_NEIGHBORS:
            self.neighbors[location] = neighboard

    def render(self, screen: pygame.Surface):
        line_start = self.position.asTuple()
        for n in range(N_NEIGHBORS):
            if self.neighbors[n] is not None:
                line_end = self.neighbors[n].asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end)
                pygame.draw.circle(screen, RED, self.position.asTuple(), 7)
                pygame.draw.line(screen, (0, 255, 0), (365, 543), (365, 572))
                pygame.draw.line(screen, (255, 0, 0), (328, 580), (356, 580))

