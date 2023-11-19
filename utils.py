import pygame
import os
from pygame import Surface
from point import Point

def load_tileset(dir: str, size: Point) -> list[Surface]:
    files = [f.path for f in os.scandir(dir) if f.is_file()]
    files = sorted(files)
    tileset: list[Surface] = []

    for f in files:
        image = pygame.image.load(f).convert_alpha()
        tileset.append(pygame.transform.scale(image, size.asTuple()))
    return tileset
