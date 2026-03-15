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
        self._player_img = pygame.image.load("imageSource/Brick Pipe.png").convert_alpha()
        self._rect = self._player_img.get_rect(topleft=(x, self._y))
        self._toprect = self._player_img.get_rect(topleft=(x, self._y - settings.PIPE_GAP))

    def move(self) -> None:
        self._rect.x -= settings.PIPE_VEL
        self._toprect.x -= settings.PIPE_VEL

    def draw(self, win: pygame.Surface) -> None:
        win.blit(pygame.transform.flip(self._player_img, False, True), self._toprect)
        win.blit(self._player_img, self._rect)
