import pygame
import settings


class Bird:
    def __init__(self, x: int, y: int):
        self.y_vel: float = 0
        self.player_img = pygame.image.load(
            "imageSource/Chicken version 3.png"
        ).convert_alpha()
        self.rect = self.player_img.get_rect(topleft=(x, y))

    def draw(self, win: pygame.Surface):
        win.blit(self.player_img, self.rect)

    def move(self):
        self.y_vel += 0.5
        self.rect.y += int(self.y_vel)

    def jump(self):
        self.y_vel = settings.VEL

    def freeze(self):
        self.y_vel = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 980:
            self.rect.bottom = 980

    def bird_reset(self):
        self.y_vel = 0
        self.rect.x = 150
        self.rect.y = 200
