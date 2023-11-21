from node import Node
from constants import *
from point import Vector

class Maze():
    def __init__(self) -> None:
        self.nodes: list[Node] = [] # Node list
        self.spawn_loc: list[Node] = [] # Spawn location for each entity
        nodes = [(292, 192),
                (584, 192),
                (422, 342),
                (584, 342),
                (292, 550),
                (422, 550),
                (584, 550)]
        for i, loc in enumerate(nodes):
            x, y = loc
            self.nodes.append(Node(x, y, i))
        self.connect_maze()
        self.spawn_loc.append(self.nodes[0])

    def connect_maze(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if j == i:
                    continue
                if self.nodes[i].position.x == self.nodes[j].position.x:
                    if self.nodes[i].position.y < self.nodes[j].position.y:
                        self.nodes[i].add_neighbor(self.nodes[j], DOWN)
                    else:
                        self.nodes[i].add_neighbor(self.nodes[j], UP)
                elif self.nodes[i].position.y == self.nodes[j].position.y:
                    if self.nodes[i].position.x < self.nodes[j].position.x:
                        self.nodes[i].add_neighbor(self.nodes[j], RIGHT)
                    else:
                        self.nodes[i].add_neighbor(self.nodes[j], LEFT)

    def render(self, screen):
        for n in self.nodes:
            n.render(screen)

    def get_spawn_loc(self, entity_id: int) -> Node:
        return self.spawn_loc[entity_id]
    
    def createMaze(self):
        self.nodes: list[Node] = []
        with open("./coordinates.txt") as f:
            for i, line in enumerate(f.readlines()):
                data = line.split()
                self.nodes.append(Node(int(data[0]), int(data[1]), i))
                print(data)

