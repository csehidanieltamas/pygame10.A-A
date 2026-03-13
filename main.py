from game import Game
import settings


def main() -> None:
    nehezseg: str = input('Add meg a nehézséget (Könnyű = "e";"1" / Közepes = "m";"2" / Nehéz = "h";"3"): ')
    if nehezseg == "1" or nehezseg == "e":
        settings.PIPE_VEL = 5
        settings.PIPE_GAP = 900
    elif nehezseg == "2" or nehezseg == "m":
        settings.PIPE_VEL = 10
        settings.PIPE_GAP = 800
    elif nehezseg == "3" or nehezseg == "h":
        settings.PIPE_VEL = 15
        settings.PIPE_GAP = 700
    game: Game = Game()
    game.run()


if __name__ == "__main__":
    main()
