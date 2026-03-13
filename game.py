# import sys

import pygame
from bg import Bg
from bird import Bird
from pipe import Pipe
from settings import FPS, HEIGHT, WIDTH, WHITE


class Game:
    print("teszt")

    def run(self) -> None:
        run: bool = True
        lost: bool = False
        clock: pygame.time.Clock = pygame.time.Clock()
        ketto_mp_timer: int = 0

        while run:
            clock.tick(FPS)
            self.bg.move()
            self.bg.draw(self.WIN)
            self.bird.draw(self.WIN)
            for p in self.pipes:
                p.draw(self.WIN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.bird.jump()

                if event.type == pygame.KEYDOWN and event.button == 1:
                    if not lost:
                        self.bird.jump()
                    else:
                        lost = False
                        self.bird.bird_reset()
                        self.pipes.clear()

            if ketto_mp_timer > 90:
                self.pipes.append(Pipe(2000))
                ketto_mp_timer = 0

            for p in self.pipes:
                if self.bird.rect.colliderect(p.rect) or self.bird.rect.colliderect(
                    p.toprect
                ):
                    lost = True

            if self.bird.rect.top <= 0 or self.bird.rect.bottom >= HEIGHT:
                lost = True

            if not lost:
                self.bird.move()
                for p in self.pipes:
                    p.move()
                ketto_mp_timer += 1
            else:
                self.bird.freeze()

            if lost:
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
        self.bird: Bird = Bird(
            150, 200
        )  # ezek a paraméterek még nem jók ,csak tesztnek
        self.pipes: list[Pipe] = []
        self.bg = Bg()
