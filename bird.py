import pygame
from settings import VEL


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
        self.y_vel = VEL
