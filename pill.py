import pygame
from typing import Self
from constants import *
from entity import Entity
from point import Vector
from node import Node
import random
from datetime import datetime

class Pill():
    RADIUS = 2
    DIAMETER = RADIUS * 2
    SEP = 5.5
    TOTAL_SIZE = int(DIAMETER + SEP * 2)
    def __init__(self, x: int, y: int) -> None:
        self.position = Vector(x, y)
        self.neighbors: list[Self | None] = [None for _ in range(N_NEIGHBORS + 1)]
        self.neighbors[STOP] = self
        self.color = WHITE
        self.radius = Pill.RADIUS
        self.visible = True
        self.points = 10
        self.type = NORMAL

    def render(self, screen: pygame.Surface):
        if self.visible:
            pygame.draw.circle(screen, self.color, self.position.asTuple(), self.radius)

class PowerPill(Pill):
    PP_LOCATION = [Vector(194-150, 145), Vector(194-150, 676),
                   Vector(670-150, 145), Vector(670-150, 676)]
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.points = 100
        self.radius = Pill.RADIUS * 2
        self.hidden = False
        self.counter = 0
        self.frame_max = 10
        self.type = POWER

    def update(self):
        if not self.visible:
            return
        self.counter += 1
        if self.counter == self.frame_max:
            self.hidden = not self.hidden
            self.counter = 0

    def render(self, screen: pygame.Surface):
        if not self.hidden and self.visible:
            pygame.draw.circle(screen, self.color, self.position.asTuple(), self.radius)

class PillGroup():
    def __init__(self, nodes: list[Node]) -> None:
        self.create_pill_group(nodes)

    def create_pill_group(self, nodes: list[Node]) -> None:
        self.pills: list[Pill | PowerPill] = []
        self.power_pills: list[PowerPill] = []
        self.total_points = 0
        for node in nodes:
            if node.ghost_home or node.is_portal:
                continue

            if node.position in PowerPill.PP_LOCATION:
                pp = PowerPill(*node.position.asTuple())
                self.pills.append(pp)
                self.power_pills.append(pp)
            else:
                self.pills.append(Pill(node.position.x, node.position.y))

            if node.neighbors[RIGHT] and not node.neighbors[RIGHT].is_portal:
                self.add_pill(node, RIGHT)

            if node.neighbors[DOWN] and not node.neighbors[DOWN].ghost_home:
                self.add_pill(node, DOWN, 1)

    def render(self, screen: pygame.Surface):
        for pill in self.pills:
            pill.render(screen)

    def add_pill(self, node: Node, direction: int, axis: int = 0) -> None:
        position = node.position.asList()
        target = node.neighbors[direction].position.asTuple()
        position[axis] += Pill.TOTAL_SIZE
        while position[axis] < target[axis] - (TILE_W / 2):
            self.pills.append(Pill(*position))
            position[axis] += Pill.TOTAL_SIZE

    def update(self):
        for pp in self.power_pills:
            pp.update()
    def restart(self):
        for pill in self.pills:
            pill.visible = True
