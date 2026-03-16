import pygame
from bg import Bg
from bird import Bird
from pipe import Pipe
import settings
class Game:
    def difficulty(self) -> None:
        choosing: bool = True
        while choosing:
            self._bg.draw(self._WIN)

            title = self._SCORE_FONT.render("Válassz nehézséget!", 1, settings.WHITE)
            easy = self._SCORE_FONT.render("1 / E - Könnyű", 1, settings.WHITE)
            medium = self._SCORE_FONT.render("2 / M - Közepes", 1, settings.WHITE)
            hard = self._SCORE_FONT.render("3 / H - Nehéz", 1, settings.WHITE)
            extreme = self._SCORE_FONT.render("4 / X - Extrém", 1, settings.WHITE)

            self._WIN.blit(
                title,
                (
                    settings.WIDTH // 2 - title.get_width() // 2,
                    settings.HEIGHT // 2 - 350,
                ),
            )
            self._WIN.blit(
                easy,
                (
                    settings.WIDTH // 2 - easy.get_width() // 2,
                    settings.HEIGHT // 2 - 150,
                ),
            )
            self._WIN.blit(
                medium,
                (
                    settings.WIDTH // 2 - medium.get_width() // 2,
                    settings.HEIGHT // 2 - 50,
                ),
            )
            self._WIN.blit(
                hard,
                (
                    settings.WIDTH // 2 - hard.get_width() // 2,
                    settings.HEIGHT // 2 + 50,
                ),
            )
            self._WIN.blit(
                extreme,
                (
                    settings.WIDTH // 2 - extreme.get_width() // 2,
                    settings.HEIGHT // 2 + 150,
                ),
            )

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._Run = False
                    choosing = False
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
                    elif event.key == pygame.K_4 or event.key == pygame.K_x:
                        settings.PIPE_VEL = 25
                        settings.PIPE_GAP = 700
                        choosing = False

    def run(self) -> None:
        lost: bool = False
        score: int = 0
        clock: pygame.time.Clock = pygame.time.Clock()
        timer: int = 0

        while self._Run:
            clock.tick(settings.FPS)
            self._bg.move()
            self._bg.draw(self._WIN)
            self._bird.draw(self._WIN)

            for p in self._pipes:
                p.draw(self._WIN)
            
            if timer % 90 == 0:
                score += 1

            text = self._SCORE_FONT.render(str(score), 1, settings.WHITE)
            self._WIN.blit(text, (50, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._Run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self._bird.jump()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not lost:
                        self._bird.jump()
                    else:
                        lost = False
                        self._bird.bird_reset()
                        self._pipes.clear()
                        score = 0

            if timer > 90:
                self._pipes.append(Pipe(2000))
                timer = 0

            for p in self._pipes:
                if self._bird.rect.colliderect(p.rect) or self._bird.rect.colliderect(p.toprect):
                    lost = True

            if self._bird.rect.top <= 0 or self._bird.rect.bottom >= settings.HEIGHT:
                lost = True

            if not lost:
                self._bird.move()
                for p in self._pipes:
                    p.move()
                timer += 1
            else:
                self._bird.freeze()

            if lost:
                lose_text: str = "Meghaltál"
                text1 = self._SCORE_FONT.render(lose_text, 1, settings.WHITE)
                self._WIN.blit(
                    text1,
                    (
                        settings.WIDTH // 2 - text1.get_width() // 2,
                        settings.HEIGHT // 2 - text1.get_height() // 2,
                    ),
                )
                text2 = self._SCORE_FONT2.render(
                    "Nyomj egy egérgombot az újrakezdéshez!", 1, settings.WHITE
                )
                self._WIN.blit(
                    text2,
                    (
                        settings.WIDTH // 2 - text2.get_width() // 2,
                        settings.HEIGHT // 2 - text2.get_height() // 2 + 100,
                    ),
                )

            pygame.display.update()
        pygame.quit()

    def __init__(self) -> None:
        pygame.init()
        self._score: int = 0
        self._keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
        self._SCORE_FONT: pygame.font.Font = pygame.font.SysFont("comicsans", 100)
        self._SCORE_FONT2: pygame.font.Font = pygame.font.SysFont("comicsans", 50)
        self._WIN: pygame.Surface = pygame.display.set_mode(
            (settings.WIDTH, settings.HEIGHT)
        )
        self._bird: Bird = Bird(150, 200)
        self._pipes: list[Pipe] = []
        self._bg: Bg = Bg()
        self._Run: bool = True
        pygame.mixer.music.load("MusicAssets/Flappy Bird Background Music.mp3")
        pygame.mixer.music.play(-1)
