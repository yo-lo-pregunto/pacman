import pygame

from point import Vector


class Text():
    def __init__(self, x: int, y: int, text: str, size: int, visible: bool, color: str) -> None:
        self.font = pygame.font.Font("./fonts/FiraCodeNerdFont-Bold.ttf", size)
        self.position = Vector(x, y)
        self.color = color
        self.set_text(text)
        self.visible = visible
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
        #self.texts["Title"] = Text(860 // 2, 50,  "󰮯 PAC - MAN 󰮯", 50, True, "#fdff00")
        self.texts["Score_txt"] = Text(40, 20, "Score:", 20, True, "#ffffff")
        self.texts["Score"] = Text(50, 40, "0".zfill(8), 20, True, "#ffffff")
        self.texts["Lives_txt"] = Text(40, 60, "Lives:", 20, True, "#ffffff")
        self.texts["Lives"] = Text(50, 80, "5".zfill(8), 20, True, "#ffffff")
        self.texts["Ready!"] = Text(280, 439, "Ready!", 20, True, "#fdff00")
        self.texts["Pause!"] = Text(280, 439, "Pause!", 20, False, "#fdff00")
        self.texts["Gameover!"] = Text(280, 439, "Gameover!", 20, False, "#fdff00")

    def render(self, screen):
        for _, text in self.texts.items():
            text.render(screen)

    def update_score(self, value):
        new_value = int(self.texts["Score"].text) + value
        self.texts["Score"].set_text(str(new_value).zfill(8))

    def reset_score(self):
        self.texts["Score"].set_text("0".zfill(8))

    def update_lives(self, lives: int) -> None:
        self.texts["Lives"].set_text(str(lives).zfill(8))

    def get_score(self) -> int:
        return int(self.texts["Score"].text)

    def hide(self):
        self.texts["Ready!"].visible = False
        self.texts["Pause!"].visible = False
        self.texts["Gameover!"].visible = False

    def show_text(self, key):
        self.hide()
        if key in self.texts:
            self.texts[key].visible = True


            
