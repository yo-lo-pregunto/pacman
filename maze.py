from node import Node
from constants import *
from point import Vector

class Maze():
    def __init__(self) -> None:
        self.spawn_loc = {} # Spawn location for each entity
        self.create_maze()
        self.connect_maze()

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
        self.nodes[-1].neighbors[RIGHT] = self.nodes[-2]
        self.nodes[-2].neighbors[LEFT] = self.nodes[-1]


    def render(self, screen):
        for n in self.nodes:
            n.render(screen)

    def get_spawn_loc(self, entity: str) -> Node:
        return self.spawn_loc[entity]
    
    def create_maze(self):
        self.nodes: list[Node] = [Node(422, 550, 0, [2, 3])]
        self.spawn_loc["Pacman"] = self.nodes[0]
        count = 1
        with open("./coordinates.txt") as f:
            for line in f.readlines():
                data, entities = parse_line(line)
                x, y = data[0], data[1]
                self.nodes.append(Node(x, y, count, data[2:]))
                count += 1
                if entities:
                    self.spawn_loc[entities.pop(0)] = self.nodes[-1]
                if self.nodes[0].position.x != x:
                    d = self.nodes[0].position.x - x
                    c = invert_constrains(data[2:])
                    self.nodes.append(Node(self.nodes[0].position.x + d, y, count, c))
                    count += 1
                    if entities:
                        self.spawn_loc[entities.pop(0)] = self.nodes[-1]

def invert_constrains(l: list[int]) -> list[int]:
    for i in range(len(l)):
        if l[i] == LEFT or l[i] == RIGHT:
            l[i] ^= 1
    return l

def parse_line(line: str) -> tuple[list[int], list[str]]:
    ints = []
    names = []
    for string in line.split():
        if string.isdigit():
            ints.append(int(string))
        else:
            names.append(string)
    return ints, names

