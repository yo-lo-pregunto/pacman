import pygame
from typing import Self
from constants import *
from entity import Entity
from point import Vector
from node import Node

class Pill():
    def __init__(self, x: int, y: int) -> None:
        self.position = Vector(x, y)
        self.neighbors: list[Self | None] = [None for _ in range(N_NEIGHBORS + 1)]
        self.neighbors[STOP] = self
        self.color = WHITE
        self.radius = 2
        self.visible = True
        self.points = 10

    def render(self, screen: pygame.Surface):
        if self.visible:
            adjust = self.position + Vector(8, 8)
            pygame.draw.circle(screen, self.color, adjust.asTuple(), self.radius)


class PillGroup():
    def __init__(self, nodes: list[Node]) -> None:
        self.pills: list[Pill] = []
        for node in nodes:
            if node.ghost_home:
                continue
            if node.neighbors[RIGHT] and not node.is_portal and not node.neighbors[RIGHT].is_portal:
                distance = node.position.magnitude(node.neighbors[RIGHT].position)
                n = distance // 8
                x = node.position.x
                for i in range(n):
                    self.pills.append(Pill(x + (8 * i), node.position.y))
            if node.neighbors[DOWN] and not node.neighbors[DOWN].ghost_home:
                distance = node.position.magnitude(node.neighbors[DOWN].position)
                n = distance // 8
                y = node.position.y
                for i in range(1, n):
                    self.pills.append(Pill(node.position.x, y + (8*i)))
            if node.neighbors[UP]:
                self.pills.append(Pill(node.position.x, node.position.y))
        self.pills[0].visible = False
        self.total_points = len(self.pills) * self.pills[0].points

    def render(self, screen: pygame.Surface):
        for pill in self.pills:
            pill.render(screen)
