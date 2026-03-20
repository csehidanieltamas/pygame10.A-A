import pygame
from bg import Bg
from bird import Bird
from highscore import Highscore
from pipe import Pipe
import settings


class Game:
    def difficulty(self) -> None:
        while self._choosing:
            self._bg.draw(self._WIN)

            # szövegek létrehozása
            title: pygame.Surface = self._SCORE_FONT.render(
                "Válassz nehézséget!", 1, settings.WHITE
            )
            easy: pygame.Surface = self._SCORE_FONT.render(
                "1 / E - Könnyű", 1, settings.WHITE
            )
            medium: pygame.Surface = self._SCORE_FONT.render(
                "2 / M - Közepes", 1, settings.WHITE
            )
            hard: pygame.Surface = self._SCORE_FONT.render(
                "3 / H - Nehéz", 1, settings.WHITE
            )
            extreme: pygame.Surface = self._SCORE_FONT.render(
                "4 / X - Extrém", 1, settings.WHITE
            )

            # szövegek kiírása
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
                    self._choosing = False
                    pygame.quit()

                # beállítások módosítása nehézség alapján
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 or event.key == pygame.K_e:
                        settings.PIPE_VEL = 5
                        settings.PIPE_GAP = 900
                        self._diff = "Könnyű"
                    elif event.key == pygame.K_2 or event.key == pygame.K_m:
                        settings.PIPE_VEL = 10
                        settings.PIPE_GAP = 800
                        self._diff = "Közepes"
                    elif event.key == pygame.K_3 or event.key == pygame.K_h:
                        settings.PIPE_VEL = 15
                        settings.PIPE_GAP = 700
                        self._diff = "Nehéz"
                    elif event.key == pygame.K_4 or event.key == pygame.K_x:
                        settings.PIPE_VEL = 25
                        settings.PIPE_GAP = 700
                        self._diff = "Extrém"

                    # átváltás a játékra
                    self._choosing = False
                    self._Run = True
                    self._run()

    def _run(self) -> None:
        while self._Run:
            self._clock.tick(settings.FPS) # játék futtatása beállított sebességgel
            self._bg.move() # háttér mozgatása
            self._bg.draw(self._WIN) # háttér rajzolása
            self._bird.draw(self._WIN) # madár rajzolása

            for p in self._pipes: # csövek rajzolása
                p.draw(self._WIN)
            if self._timer % 90 == 0: # pont adás és hang hozzá
                self._score += 1
                self._score_sound.play()

            text: pygame.Surface = self._SCORE_FONT.render(
                str(self._score), 1, settings.WHITE
            )
            self._WIN.blit(text, (50, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # kilépés
                    self._Run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: # ugrás / újraéledés
                        if not self._lost:
                            self._bird.leg_swap()
                            self._bird.jump()
                        else:
                            self._lost = False
                            self._bird.bird_reset()
                            self._pipes.clear()
                            h: Highscore = Highscore(self._score, self._diff)
                            h.highscore_kiírás()
                            self._score = 0

                if event.type == pygame.MOUSEBUTTONDOWN: # ugrás / játékmód váltás
                    if event.button == 1:
                        if self._lost:
                            self._lost = False
                            self._bird.bird_reset()
                            self._pipes.clear()
                            h: Highscore = Highscore(self._score, self._diff)
                            h.highscore_kiírás()
                            self._score = 0
                            self._Run = False
                            self._choosing = True
                        else:
                            self._bird.leg_swap()
                            self._bird.jump()

            if self._timer > 90: # csövek létrehozása 90 ms-onként
                self._pipes.append(Pipe(2000))
                self._timer = 0

            for p in self._pipes: # ütközés észlelése -> halál?
                if (
                    self._bird.rect.colliderect(p.rect)
                    or self._bird.rect.colliderect(p.toprect)
                ):
                    self._lost = True

            if self._bird.rect.top <= 0 or self._bird.rect.bottom >= settings.HEIGHT: # talaj/tető érintése -> halál?
                self._lost = True

            if not self._lost: # csövek és madár mozgatása ha él a madár
                self._bird.move()
                for p in self._pipes:
                    p.move()
                self._timer += 1
            else: # fagyasztás, ha halott
                self._bird.freeze()

            if self._lost: # madár halála esetén halálüzenet kiírása
                self._WIN.blit(
                    self._text1,
                    (
                        settings.WIDTH // 2 - self._text1.get_width() // 2,
                        settings.HEIGHT // 2 - self._text1.get_height() // 2 - 200,
                    ),
                )
                self._WIN.blit(
                    self._text2,
                    (
                        settings.WIDTH // 2 - self._text2.get_width() // 2,
                        settings.HEIGHT // 2 - self._text2.get_height() // 2,
                    ),
                )
                self._WIN.blit(
                    self._text3,
                    (
                        settings.WIDTH // 2 - self._text3.get_width() // 2,
                        settings.HEIGHT // 2 - self._text3.get_height() // 2 + 100,
                    ),
                )

            pygame.display.update()
        self.difficulty()
        pygame.quit()

    def __init__(self) -> None:
        pygame.init() # pygame inicializálása
        self._diff: str = ""
        self._lost: bool = False # bool, elmondja vesztettünk-e
        self._score: int = 0 # pontok inicializálása
        self._timer: int = 0 # időzítő pontadáshoz inicializálása
        self._clock: pygame.time.Clock = pygame.time.Clock() # óra inicializálása
        self._keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed() # billentyűzet inicializálása
        self._SCORE_FONT: pygame.font.Font = pygame.font.SysFont("comicsans", 100) # első betűtípus inicializálása
        self._SCORE_FONT2: pygame.font.Font = pygame.font.SysFont("comicsans", 50) # második betűtípus inicializálása
        self._text1: pygame.Surface = self._SCORE_FONT.render("Meghaltál", 1, settings.WHITE) # első halálszöveg inicializálása
        self._text2: pygame.Surface = self._SCORE_FONT2.render("Nyomj egy space-t az újrakezdéshez!", 1, settings.WHITE) # második halálszöveg inicializálása
        self._text3: pygame.Surface = self._SCORE_FONT2.render("Nyomj egy egérgombot a nehézség változtatásához!",1,settings.WHITE,) # harmadik halálszöveg inicializálása
        self._WIN: pygame.Surface = pygame.display.set_mode(
            (settings.WIDTH, settings.HEIGHT)
        ) # képernyő inicializálása
        self._bird: Bird = Bird(150, 200) # madár inicializálása
        self._pipes: list[Pipe] = [] # csövek listájának inicializálása
        self._bg: Bg = Bg() # háttér inicializálása
        self._Run: bool = True # bool ami eldönti, hogy lefusson-e a játék
        self._choosing: bool = True # bool ami eldönti, hogy választjuk e a nehézséget
        pygame.mixer.music.load("MusicAssets/Flappy Bird Background Music.mp3") # háttérzene inicializálása
        pygame.mixer.music.play(-1) # háttérzene lejátszása
        self._score_sound: pygame.mixer.Sound = pygame.mixer.Sound("MusicAssets/Score Sound Effect.mp3") # pont szerzési hang inicializálása
