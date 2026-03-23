from game import Game


def main() -> None:
    game: Game = Game()  # objetkum a játékmenettel létrehozása
    game.difficulty()  # játékmenet elindul a nehézség választással


if __name__ == "__main__":
    main()
