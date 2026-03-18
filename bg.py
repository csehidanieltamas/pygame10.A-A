import pygame
from settings import WIDTH


class Bg:
    def __init__(self) -> None:
        self._x: int = 0
        self._player_img: pygame.Surface = pygame.image.load(
            "imageSource/Background.png"
        )

    def move(self) -> None:
        self._x -= 1
        if self._x <= -WIDTH:
            self._x = 0

    def draw(self, win: pygame.Surface) -> None:
        win.blit(self._player_img, (self._x, 0))
        win.blit(self._player_img, (self._x + WIDTH, 0))
