import pygame
from settings import VEL


class Bird:
    def __init__(self, x: int, y: int):
        self.x: float = x
        self.y: float = y
        self.y_vel: float = 0
        self.player_img = pygame.image.load("imageSource/Flappy Bird Chicken.png").convert_alpha()

    def draw(self, win: pygame.Surface):
        win.blit(self.player_img, (self.x, self.y))

    def move(self):
        self.y_vel -= 10
        self.y += self.y_vel


    def jump(self):
        self.y_vel = VEL
