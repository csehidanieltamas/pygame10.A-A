import pygame
import settings


class Bird:

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    @property
    def rect2(self) -> pygame.Rect:
        return self._rect2

    def __init__(self, x: int, y: int):
        self._y_vel: float = 0
        self._player_img: pygame.Surface = pygame.image.load(
            "imageSource/Chicken.png"
        ).convert_alpha()
        self._player_img2: pygame.Surface = pygame.image.load(
            "imageSource/Chicken 2.png"
        ).convert_alpha()
        self._rect: pygame.Rect = self._player_img.get_rect(topleft=(x, y))
        self._rect2: pygame.Rect = self._player_img2.get_rect(topleft=(x, y))
        self.bird_leg: int = 1

    def draw(self, win: pygame.Surface):
        if self.bird_leg == 1:
            win.blit(self._player_img2, self.rect2)
        elif self.bird_leg == -1:
            win.blit(self._player_img, self.rect)

    def move(self) -> None:
        self._y_vel += 0.5
        self._rect.y += int(self._y_vel)
        self._rect2.y += int(self._y_vel)

    def jump(self) -> None:
        self._y_vel = settings.VEL

    def freeze(self) -> None:
        self._y_vel = 0
        if self._rect.top <= 0:
            self._rect.top = 0
        if self._rect.bottom >= 980:
            self._rect2.bottom = 980
        if self._rect2.top <= 0:
            self._rect2.top = 0
        if self._rect2.bottom >= 980:
            self._rect2.bottom = 980

    def bird_reset(self) -> None:
        self._y_vel = 0
        self._rect.x = 150
        self._rect.y = 200
        self._rect2.x = 150
        self._rect2.y = 200

    def leg_swap(self) -> None:
        self.bird_leg = self.bird_leg * -1
