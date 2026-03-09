import pygame
from settings import COLOR, MAX_VEL

class Bird:
    def __init__(self, x: int, y: int, radius: int):
        self.x: float = x
        self.y: float = y
        self.radius = radius
        self.y_vel: float = MAX_VEL

    def draw(self, win: pygame.Surface):
        pygame.draw.circle(win, COLOR, (self.x, self.y), self.radius)


    def move(self):
        self.y += self.y_vel

    
