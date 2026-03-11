import random
import pygame
from bird import Bird
from settings import HEIGHT, PIPE_VEL, PIPE_GAP

class Pipe:
    PIPE_IMAGE: pygame.Surface = pygame.transform.scale2x(pygame.image.load("imageSource/pipe.jpg"))
    FLIPPED_PIPE: pygame.Surface = pygame.transform.flip(PIPE_IMAGE, False, True)

    def __init__(self, x: int) -> None:
        self.x: int = x
        self.passed: bool = False
        
        self.height: int = random.randint(100, HEIGHT - 300) 

        self.top_y: int = self.height - self.PIPE_IMAGE.get_height()
        
        self.bottom_y: int = self.height + PIPE_GAP

    def move(self) -> None:
        self.x -= PIPE_VEL

    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.FLIPPED_PIPE, (self.x, self.top_y))
        win.blit(self.PIPE_IMAGE, (self.x, self.bottom_y))

    def collide(self, bird: Bird) -> bool:
        bird_rect: pygame.Rect = pygame.Rect(
            int(bird.x - bird.radius), 
            int(bird.y - bird.radius), 
            bird.radius * 2, 
            bird.radius * 2
        )
        
        top_rect: pygame.Rect = pygame.Rect(self.x, self.top_y, self.FLIPPED_PIPE.get_width(), self.FLIPPED_PIPE.get_height())
        bottom_rect: pygame.Rect = pygame.Rect(self.x, self.bottom_y, self.PIPE_IMAGE.get_width(), self.PIPE_IMAGE.get_height())
        
        if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
            return True
        return False
