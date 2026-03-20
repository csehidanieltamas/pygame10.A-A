import pygame
from settings import WIDTH


class Bg:
    def __init__(self) -> None:
        self._x: int = 0 # háttér vízszintes pozíciója
        self._player_img: pygame.Surface = pygame.image.load(
            "imageSource/Background.png"
        ) # háttér kép betöltése

    def move(self) -> None: # háttér mozgatása lassan balra
        self._x -= 1
        if self._x <= -WIDTH:
            self._x = 0

    def draw(self, win: pygame.Surface) -> None: # háttér rajzolása
        win.blit(self._player_img, (self._x, 0))
        win.blit(self._player_img, (self._x + WIDTH, 0))
        # két háttér, az egyik egy képernyővel balra a tökéletes kapcsolódásért
