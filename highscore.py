from datetime import datetime


class Highscore:
    __aktuális_dátum: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    __score: int
    __gamemode: str | None

    def __init__(self, score: int, gamemode: str | None) -> None:
        self.__score = score
        self.__gamemode = gamemode

    def highscore_kiírás(self) -> None:
        with open("Highscore.txt", "a", encoding="utf-8") as file:
            file.write(
                f"Pont: {self.__score}, Nehézség: {self.__gamemode}, Dátum: {self.__aktuális_dátum}\n"
            )
