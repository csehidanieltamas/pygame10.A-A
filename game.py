import sys

import pygame

from bird import Bird
from pipe import Pipe
from settings import FPS, HEIGHT, WHITE, WIDTH


class Game:
    print("teszt")

    def run(self) -> None:
        run: bool = True
        clock: pygame.time.Clock = pygame.time.Clock()

        while run:
            ketto_mp_timer: int = 0
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

                if self.bird.rect.y <= 0 or self.bird.rect.y >= 920:
                    run = False
                    pygame.quit()
                    sys.exit()

            if  ketto_mp_timer > 120:
                self.pipes.append(Pipe(2000))
                ketto_mp_timer = 0

            self.bird.move()
            for p in self.pipes:
                p.move()
            ketto_mp_timer += 1

            lost: bool = False
            lose_text: str = "Meghaltál"
            #            if self.bird.colliderect(self.pipe):
            #                lost = True

            if lost:
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
            pygame.display.update()
        pygame.quit()

    def __init__(self) -> None:
        pygame.init()
        self.score: int = 0
        self.keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
        self.SCORE_FONT = pygame.font.SysFont("comicsans", 50)
        self.WIN: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.bg = pygame.image.load("imageSource/Background.png").convert()
        self.bird: Bird = Bird(
            200, 200
        )  # ezek a paraméterek még nem jók ,csak tesztnek
        self.pipes: list[Pipe] = []
