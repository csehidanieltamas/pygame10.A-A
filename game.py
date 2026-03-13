#import sys

import pygame

from bird import Bird
from pipe import Pipe
from settings import FPS, HEIGHT, WHITE, WIDTH


class Game:
    print("teszt")

    def run(self) -> None:
        run: bool = True
        lost: bool = False
        clock: pygame.time.Clock = pygame.time.Clock()

        while run:
            clock.tick(FPS)
            self.WIN.blit(self.bg, (0, 0))
            self.bird.draw(self.WIN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.bird.jump()

            if self.bird.rect.top <= 0 or self.bird.rect.bottom >= HEIGHT:
                lost = True

            if not lost:
                self.bird.move()
                self.pipe.move()
            else:
                self.bird.freeze()
                lose_text: str = "Meghaltál"
                text = self.SCORE_FONT.render(lose_text, 1, WHITE)
                self.WIN.blit(
                    text,
                    (
                        WIDTH // 2 - text.get_width() // 2,
                        HEIGHT // 2 - text.get_height() // 2,
                    ),
                )

            
            pygame.display.update()
        pygame.quit()

    def __init__(self) -> None:
        pygame.init()
        self.score: int = 0
        self.keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
        self.SCORE_FONT = pygame.font.SysFont("comicsans", 100)
        self.WIN: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.bg = pygame.image.load("imageSource/Background.png").convert()
        self.bird: Bird = Bird(
            150, 200
        )  # ezek a paraméterek még nem jók ,csak tesztnek
        self.pipe: Pipe = Pipe(50)
