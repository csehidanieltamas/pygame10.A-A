import pygame
import settings
class Bird:

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    def __init__(self, x: int, y: int):
        self._y_vel: float = 0
        self._player_img = pygame.image.load(
            "imageSource/Chicken version 3.png"
        ).convert_alpha()
        self._rect = self._player_img.get_rect(topleft=(x, y))

    def draw(self, win: pygame.Surface):
        win.blit(self._player_img, self.rect)

    def move(self):
        self._y_vel += 0.5
        self._rect.y += int(self._y_vel)

    def jump(self):
        self._y_vel = settings.VEL

    def freeze(self):
        self._y_vel = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 980:
            self.rect.bottom = 980

    def bird_reset(self):
        self._y_vel = 0
        self._rect.x = 150
        self._rect.y = 200
