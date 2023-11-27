import pygame

from point import Vector


class Text():
    def __init__(self, x: int, y: int, text: str, size: int, visible: bool, color: str) -> None:
        self.font = pygame.font.Font("./fonts/FiraCodeNerdFont-Bold.ttf", size)
        self.position = Vector(x, y)
        self.color = color
        self.text = text
        self.visible = visible
        self.label = self.font.render(self.text, False, self.color)
        self.rect = self.label.get_rect(center = self.position.asTuple())

    def render(self, screen: pygame.Surface):
        if self.visible:
            screen.blit(self.label, self.rect)

    def set_text(self, new_text: str) -> None:
        self.text = str(new_text)
        self.label = self.font.render(self.text, True, self.color, "#000000")

class TextGroup():
    def __init__(self) -> None:
        self.texts: dict[str, Text] = {}
        self.set_all_text()

    def set_all_text(self) -> None:
        self.texts["Title"] = Text(860 // 2, 50,  "󰮯 PAC - MAN 󰮯", 50, True, "#fdff00")
        self.texts["Score_txt"] = Text(40, 120, "Score:", 20, True, "#ffffff")
        self.texts["Score"] = Text(50, 140, "0".zfill(8), 20, True, "#ffffff")

    def render(self, screen):
        for _, text in self.texts.items():
            text.render(screen)

    def update_score(self, value):
        new_value = int(self.texts["Score"].text) + value
        self.texts["Score"].set_text(str(new_value).zfill(8))
        print(new_value)

            
