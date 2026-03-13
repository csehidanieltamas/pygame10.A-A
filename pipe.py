import random
import pygame
from settings import PIPE_VEL, PIPE_GAP


class Pipe:
    def __init__(self, x: int) -> None:
        self.y: int = random.randint(400,800)
        self.passed: bool = False
        self.player_img = pygame.image.load("imageSource/Brick Pipe.png").convert_alpha()
        self.rect = self.player_img.get_rect(topleft=(x,self.y))
        self.toprect = self.player_img.get_rect(topleft=(x, self.y - PIPE_GAP))

    def move(self) -> None:
        self.rect.x -= PIPE_VEL
        self.toprect.x -= PIPE_VEL

    def draw(self, win: pygame.Surface) -> None:
        win.blit(pygame.transform.flip(self.player_img, False, True), self.toprect)
        win.blit(self.player_img, self.rect)
