import pygame

WINDOWS_SIZE = (860, 820)
WINDOWS_TITLE = "PAC - MAN"

HEADER_LOC = (WINDOWS_SIZE[0] / 2, 50)

PACMAN_SPAW_LOC = (WINDOWS_SIZE[0] // 2,  570)

FRAME_RATE = 60

class Object(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, w: int, h: int, image: str) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.image = pygame.image.load(image).convert()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center = (x, y))


# Image path
BACKGROUND = "./graphs/maze.png"

# Init the enginee
pygame.init()

window = pygame.display.set_mode(WINDOWS_SIZE)
clock = pygame.time.Clock()
font = pygame.font.Font("./fonts/FiraCodeNerdFont-Bold.ttf", 50)

# Header
header = font.render(WINDOWS_TITLE, False, "#fdff00")
header_rect = header.get_rect(center = HEADER_LOC)

pygame.display.set_caption(WINDOWS_TITLE)

# Background
bg = pygame.image.load(BACKGROUND).convert()

# Player
pacman = pygame.sprite.GroupSingle()
pacman.add(Object(PACMAN_SPAW_LOC[0], PACMAN_SPAW_LOC[1], 12, 12, "./graphs/pac man & life counter & death/pac man/pac_man_0.png"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.blit(bg, (150, 100))
    window.blit(header, header_rect)

    # Pacman
    pacman.draw(window)

    pygame.display.update()
    clock.tick(FRAME_RATE)
