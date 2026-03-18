import random
import pygame
import settings


class Pipe:

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    @property
    def toprect(self) -> pygame.Rect:
        return self._toprect

    def __init__(self, x: int) -> None:
        self._y: int = random.randint(500, 700)
        self._passed: bool = False
        self._player_img: pygame.Surface = pygame.image.load(
            "imageSource/Brick Pipe.png"
        ).convert_alpha()
        self._rect: pygame.Rect = self._player_img.get_rect(topleft=(x, self._y))
        self._toprect: pygame.Rect = self._player_img.get_rect(
            topleft=(x, self._y - settings.PIPE_GAP)
        )

    def move(self) -> None:
        for _ in range(settings.PIPE_VEL):
            self._rect.x -= 1
            self._toprect.x -= 1

    def draw(self, win: pygame.Surface) -> None:
        win.blit(pygame.transform.flip(self._player_img, False, True), self._toprect)
        win.blit(self._player_img, self._rect)
