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
        self._y: int = random.randint(
            500, 700
        )  # véletlenszerű helyt adunk a két cső közötti lyuknak
        self._player_img: pygame.Surface = pygame.image.load(
            "imageSource/Brick Pipe.png"
        ).convert_alpha()  # cső képének betöltése
        self._rect: pygame.Rect = self._player_img.get_rect(
            topleft=(x, self._y)
        )  # cső hitboxa
        self._toprect: pygame.Rect = self._player_img.get_rect(
            topleft=(x, self._y - settings.PIPE_GAP)
        )  # felső cső, második hitbox, bizonyos magassággal feljebb

    def move(self) -> None:  # csövek balra mozgatása
        for _ in range(settings.PIPE_VEL):
            self._rect.x -= 1
            self._toprect.x -= 1

    def draw(self, win: pygame.Surface) -> None:  # csövek rajzolása
        win.blit(
            pygame.transform.flip(self._player_img, False, True), self._toprect
        )  # felső cső
        win.blit(self._player_img, self._rect)  # alsó cső
