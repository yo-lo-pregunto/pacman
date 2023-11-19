from typing import TypeAlias

Size: TypeAlias = tuple[int, int]

WINDOWS_SIZE = (860, 820)
IMAGE_SIZE = (560, 620)
WINDOWS_TITLE = "󰮯 PAC - MAN 󰮯"

HEADER_LOC = (WINDOWS_SIZE[0] / 2, 50)

PACMAN_SPAW_LOC = [WINDOWS_SIZE[0] // 2,  560]

STOP = -1
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

# Game Constants
FRAME_RATE = 30
ANIMATION_FRAME_RATE = 2
SPEED = 2
N_NEIGHBORS = 4
