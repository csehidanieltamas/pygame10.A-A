from game import Game

def main() -> None:
    game: Game = Game()
    game.difficulty()
    game.run()

if __name__ == "__main__":
    main()
