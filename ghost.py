import pygame
from constants import *
from entity import Entity
from point import Vector
from node import Node
from utils import load_tileset
from animation import Animation
import random
from datetime import datetime

class Ghost(Entity):
    def __init__(self, node: Node, directory: str) -> None:
        random.seed(datetime.now().timestamp())
        super().__init__(node)
        self.tileset = load_tileset(directory)
        self.reset()
        self.speed = SPEED
        self.prey_time = FRAME_RATE * 7
        self.prey_count = 0
        self.points = 200

    def reset(self):
        self.state = HUNTER
        self.image = self.tileset[self.state]
        self.position = self.home.position.copy()
        self.direction = STOP
        self.source = self.home
        self.target = self.source.neighbors[self.direction]

    def update_image(self) -> pygame.Surface:
        new_image = self.tileset[self.state]

        if self.direction == LEFT:
            new_image = pygame.transform.flip(new_image, True, False)

        return new_image

    def hunting(self):
        self.speed = SPEED
        self.state = HUNTER

    def prey(self):
        self.speed = SPEED - 1
        self.state = PREY

    def update_mode(self):
        if self.state == HUNTER:
            return
        self.prey_count += 1
        if self.prey_count > self.prey_time:
            self.hunting()

    def update(self):
        self.position += self.compass[self.direction] * self.speed
        self.update_mode()
        image = self.update_image()
        self.image = image

        d = self.position.magnitude(self.target.position)

        if d <= self.speed:
            self.position = self.target.position.copy()
            self.source  = self.target
            if self.source.is_portal:
                self.source = self.source.neighbors[self.direction]
                self.target = self.source.neighbors[self.direction]
                self.position = self.source.position.copy()
            else:
                direction = random.randint(0, 4)
                while not self.source.neighbors[direction]:
                    direction = random.randint(0, 4)
                self.target = self.source.neighbors[direction]
                self.direction = direction

    def go_home(self):
        self.position = self.home.position.copy()
        self.direction = STOP
        self.source = self.home
        self.target = self.source.neighbors[self.direction]
        self.hunting()

class Ghosts():
    def __init__(self, nodes: list[Node]) -> None:
        self.ghosts: dict[str, Ghost] = {}
        self.ghosts["Huayra"] = Ghost(nodes[0], "./graphs/ghost/blue ghost/")
        self.ghosts["Pancracio"] = Ghost(nodes[1], "./graphs/ghost/orange ghost/")
        self.ghosts["Tuburcio"] = Ghost(nodes[2], "./graphs/ghost/red ghost/")
        self.ghosts["Petra"] = Ghost(nodes[3], "./graphs/ghost/pink ghost/")

    def render(self, screen: pygame.Surface) -> None:
        for ghost in self.ghosts.values():
            ghost.render(screen)

    def state(self, state):
        for ghost in self.ghosts.values():
            if state == HUNTER:
                ghost.hunting()
            else:
                ghost.prey()

    def update_points(self):
        for ghost in self.ghosts.values():
            ghost.points *= 2

    def reset_points(self):
        for ghost in self.ghosts.values():
            ghost.points = 200

    def reset(self):
        for ghost in self.ghosts.values():
            ghost.reset()
