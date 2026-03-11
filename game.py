import pygame
from bird import Bird
from pipe import Pipe
from settings import (
    WHITE,
    WIDTH,
    HEIGHT, 
    FPS,
)


class Game:
    print("teszt")
    def run(self) -> None:
        run: bool = True
        clock: pygame.time.Clock = pygame.time.Clock()

        self.score: int = 0

        while run:
            clock.tick(FPS)
            self.WIN.blit(self.bg, (0,0))
            self.bird.draw(self.WIN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == SPAWNPIPE:
                    PIPE_LIST.append

            self.keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
            self.bird.move()
            self.pipe.move()

            lost: bool = False
            lose_text: str = "Meghaloltál"
            if self.bird.colliderect(self.pipe):
                lost = True

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
        self.SCORE_FONT = pygame.font.SysFont("comicsans", 50)
        self.WIN: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.bg = pygame.image.load("imageSourcse/bg.jpg").convert()
        self.bird: Bird = Bird(50, 50) #ezek a paraméterek még nem jók ,csak tesztnek
        self.pipe: Pipe = Pipe(50)
