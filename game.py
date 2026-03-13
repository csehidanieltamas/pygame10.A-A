# import sys

import pygame
from bg import Bg
from bird import Bird
from pipe import Pipe
import settings


class Game:
    def difficulty(self) -> None:
        choosing: bool = True
        #menu_font = pygame.font.SysFont("comicsans", 50)
        while choosing:
            self.bg.draw(self.WIN)

            title = self.SCORE_FONT.render("Válassz nehézséget!", 1, settings.WHITE)
            easy = self.SCORE_FONT.render("1 / E - Könnyű", 1, settings.WHITE)
            medium = self.SCORE_FONT.render("2 / M - Közepes", 1, settings.WHITE)
            hard = self.SCORE_FONT.render("3 / H - Nehéz", 1, settings.WHITE)

            self.WIN.blit(title, (settings.WIDTH // 2 - title.get_width() // 2, settings.HEIGHT // 2 - 150))
            self.WIN.blit(easy, (settings.WIDTH // 2 - easy.get_width() // 2, settings.HEIGHT // 2 - 50))
            self.WIN.blit(medium, (settings.WIDTH // 2 - medium.get_width() // 2, settings.HEIGHT // 2 + 50))
            self.WIN.blit(hard, (settings.WIDTH // 2 - hard.get_width() // 2, settings.HEIGHT // 2 + 150))

            pygame.display.update()

            # Wait for player input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 or event.key == pygame.K_e:
                        settings.PIPE_VEL = 5
                        settings.PIPE_GAP = 900
                        choosing = False
                    elif event.key == pygame.K_2 or event.key == pygame.K_m:
                        settings.PIPE_VEL = 10
                        settings.PIPE_GAP = 800
                        choosing = False
                    elif event.key == pygame.K_3 or event.key == pygame.K_h:
                        settings.PIPE_VEL = 15
                        settings.PIPE_GAP = 700
                        choosing = False

    def run(self) -> None:
        run: bool = True
        lost: bool = False
        pont: int = 0
        clock: pygame.time.Clock = pygame.time.Clock()
        timer: int = 0

        while run:
            clock.tick(settings.FPS)
            self.bg.move()
            self.bg.draw(self.WIN)
            self.bird.draw(self.WIN)

            for p in self.pipes:
                p.draw(self.WIN)

            text = self.SCORE_FONT.render(str(pont), 1, settings.WHITE)
            self.WIN.blit(text, (50, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.bird.jump()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if not lost:
                        self.bird.jump()
                    else:
                        lost = False
                        self.bird.bird_reset()
                        self.pipes.clear()
                        pont = 0

            if timer % 90 == 0:
                pont += 1

            if timer > 90:
                self.pipes.append(Pipe(2000))
                timer = 0

            for p in self.pipes:
                if self.bird.rect.colliderect(p.rect) or self.bird.rect.colliderect(
                    p.toprect
                ):
                    lost = True

            if self.bird.rect.top <= 0 or self.bird.rect.bottom >= settings.HEIGHT:
                lost = True

            if not lost:
                self.bird.move()
                for p in self.pipes:
                    p.move()
                timer += 1
            else:
                self.bird.freeze()

            if lost:
                lose_text: str = "Meghaltál"
                text = self.SCORE_FONT.render(lose_text, 1, settings.WHITE)
                self.WIN.blit(
                    text,
                    (
                        settings.WIDTH // 2 - text.get_width() // 2,
                        settings.HEIGHT // 2 - text.get_height() // 2,
                    ),
                )

            pygame.display.update()
        pygame.quit()

    def __init__(self) -> None:
        pygame.init()
        self.score: int = 0
        self.keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
        self.SCORE_FONT: pygame.font.Font = pygame.font.SysFont("comicsans", 100)
        self.WIN: pygame.Surface = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.bird: Bird = Bird(
            150, 200
        )  # ezek a paraméterek még nem jók ,csak tesztnek
        self.pipes: list[Pipe] = []
        self.bg: Bg = Bg()
