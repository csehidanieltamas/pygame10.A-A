from datetime import datetime


class Highscore:
    __actual_date: str = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    __score: int
    __gamemode: str

    def __init__(self, score: int, gamemode: str) -> None:
        self.__score = score
        self.__gamemode = gamemode

    def highscore_kiírás(self) -> None:
        with open("Highscore.txt", "a", encoding="utf-8") as file:
            file.write(
                f"Pont: {self.__score}, Nehézség: {self.__gamemode}, Dátum: {self.__actual_date}\n"
            )
