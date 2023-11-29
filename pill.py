import pygame
from typing import Self
from constants import *
from entity import Entity
from point import Vector
from node import Node
import random
from datetime import datetime

class Pill():
    def __init__(self, x: int, y: int) -> None:
        self.position = Vector(x, y)
        self.neighbors: list[Self | None] = [None for _ in range(N_NEIGHBORS + 1)]
        self.neighbors[STOP] = self
        self.color = WHITE
        self.radius = 4
        self.visible = True
        self.points = 10
        self.typek = NORMAL

    def render(self, screen: pygame.Surface):
        if self.visible:
            adjust = self.position + Vector(8, 8)
            pygame.draw.circle(screen, self.color, adjust.asTuple(), self.radius)

class PowerPill(Pill):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.points = 100
        self.color = (0, 255, 0)
        self.radius = 8


class PillGroup():
    def __init__(self, nodes: list[Node]) -> None:
        self.create_pill_group(nodes)

    def create_pill_group(self, nodes: list[Node]) -> None:
        self.pills: list[Pill | PowerPill] = []
        d = nodes[0].position.x - 185
        self.power_pills: list[PowerPill] = []
        for node in nodes:
            if node.ghost_home:
                continue

            if node.position == Vector(659, 140):
                pp = PowerPill(659, 140)
                self.pills.append(pp)
                self.power_pills.append(pp)
            elif node.position == Vector(659, 670):
                pp = PowerPill(659, 670)
                self.pills.append(pp)
                self.power_pills.append(pp)
            elif node.position == Vector(185, 140):
                pp = PowerPill(185, 140)
                self.pills.append(pp)
                self.power_pills.append(pp)
            elif node.position == Vector(185, 670):
                pp = PowerPill(185, 670)
                self.pills.append(pp)
                self.power_pills.append(pp)

            if node.neighbors[RIGHT] and not node.is_portal and not node.neighbors[RIGHT].is_portal:
                distance = node.position.magnitude(node.neighbors[RIGHT].position)
                n = distance // 16
                x = node.position.x
                for i in range(0, n - 1):
                    self.pills.append(Pill(x + (16 * i), node.position.y))
            if node.neighbors[DOWN] and not node.neighbors[DOWN].ghost_home:
                distance = node.position.magnitude(node.neighbors[DOWN].position)
                n = distance // 16
                y = node.position.y
                for i in range(1, n ):
                    self.pills.append(Pill(node.position.x, y + (16*i)))
            if node.neighbors[UP] and not node.neighbors[RIGHT]:
                self.pills.append(Pill(node.position.x, node.position.y))
        self.pills[0].visible = False
        self.total_points = len(self.pills) * self.pills[0].points
        print("Max point:", self.total_points)

    def render(self, screen: pygame.Surface):
        for pill in self.pills:
            pill.render(screen)
