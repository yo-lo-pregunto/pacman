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
        self.animation = Animation(0, [range(len(self.tileset))])
        self.direction = STOP
        self.old_direction = STOP
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

    def update_image(self) -> pygame.Surface:
        new_frame = self.animation.get_frame()
        new_image = self.tileset[new_frame]

        if self.old_direction == LEFT or self.direction == LEFT:
            new_image = pygame.transform.flip(new_image, True, False)


        return new_image

    def find_next_direction(self):
        if self.target.neighbors[self.direction]:
            self.next_direction = self.direction
        else:
            self.next_direction = STOP

    def update(self):
        self.position += self.compass[self.direction] * self.speed
        image = self.update_image()
        self.image = image

        d = self.position.magnitude(self.target.position)

        if d <= self.speed:
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

        
