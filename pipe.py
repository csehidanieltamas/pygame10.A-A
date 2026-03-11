import random

import pygame

from settings import HEIGHT, WIDTH


class Pipe:
    pipe_surface: pygame = pygame.image.load("imageSource/pipe.jpg")
    pipe_surface: pygame = pygame.transform.scale2x(pipe_surface)
    PIPE_LIST: list[pygame | None | str | int | bool | float] = []
    SPAWNPIPE: pygame = pygame.USEREVENT

    _x_pos: int
    _height: int

    def __init__(self, x: int) -> None:
        self._x_pos = x
        self._height = random.randint(100, HEIGHT - 200)  # --> véletlen 'y' koordináta

    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.pipe_surface, (self._x_pos, self._height - self.pipe_surface.get_height()))
        flipped_pipe: pygame.transform.flip(self.pipe_surface, False, True)
        
