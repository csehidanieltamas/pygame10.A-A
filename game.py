import pygame
from bird import Bird
from pipe import Pipe
from settings import (
    WHITE,
    BLACK,
    WIDTH,
    HEIGHT,
    PADDLE_HEIGHT,
    PADDLE_WIDTH,
    WINNING_SCORE,
    BALL_RADIUS,
    FPS,
    VEL,
    MAX_VEL
)


class Game:

    def run(self) -> None:
        run: bool = True
        clock: pygame.time.Clock = pygame.time.Clock()

        bird = Bird(50, 50)

        score: int = 0

        while run:
            clock.tick(FPS)
            bird.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
            self.handle_paddle_movement(keys, left_paddle, right_paddle)

            ball.move()
            self.handle_collision(ball, left_paddle, right_paddle)

            if ball.x < 0:
                right_score += 1
                ball.reset()
            elif ball.x > WIDTH:
                left_score += 1
                ball.reset()

            won: bool = False
            win_text: str = ""
            if left_score >= WINNING_SCORE:
                won = True
                win_text = "Left Player Won!"
            elif right_score >= WINNING_SCORE:
                won = True
                win_text = "Right Player Won!"

            if won:
                text = self.SCORE_FONT.render(win_text, 1, WHITE)
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
        self.SCORE_FONT = pygame.font.SysFont("comicsans", 50)
        self.WIN: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))