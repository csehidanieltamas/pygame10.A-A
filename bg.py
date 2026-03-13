import pygame
from settings import WIDTH

class Bg:
    def __init__(self) -> None:
        self.x: int = 0
        self.player_img = pygame.image.load("imageSource/Background.png")#.convert_alpha()

    def move(self) -> None:
        self.x -= 1

    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.player_img, (self.x, 0))
        win.blit(self.player_img, (self.x + WIDTH, 0))
