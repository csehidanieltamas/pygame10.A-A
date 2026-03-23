import pygame
import settings


class Bird:

    @property
    def rect(self) -> pygame.Rect:
        return self._rect

    def __init__(self, x: int, y: int):
        self._y_vel: float = 0  # madár függőleges sebessége
        self._player_img: pygame.Surface = pygame.image.load(
            "imageSource/Chicken.png"
        ).convert_alpha()  # csirke kép betöltése
        self._player_img2: pygame.Surface = pygame.image.load(
            "imageSource/Chicken 2.png"
        ).convert_alpha()  # csirke kép betöltése, hol a másik lába van elöl
        self._rect: pygame.Rect = self._player_img.get_rect(
            topleft=(x, y)
        )  # madár hitboxa
        self.bird_leg: int = 1

    def draw(self, win: pygame.Surface):  # madár rajzolása
        if self.bird_leg == 1:
            win.blit(self._player_img2, self.rect)
        elif self.bird_leg == -1:
            win.blit(self._player_img, self.rect)

    def move(self) -> None:  # gravitáció szerint madár mozgatása
        self._y_vel += 0.5
        self._rect.y += int(self._y_vel)

    def jump(self) -> None:  # madár ugrása
        self._y_vel = settings.VEL  # sebesség iránya felfelé beállított erősséggel

    def freeze(
        self,
    ) -> None:  # madár lefagy, nem engedi ki a függvény kimenni a képernyőről
        self._y_vel = 0
        if self._rect.top <= 0:
            self._rect.top = 0
        if self._rect.bottom >= 980:
            self._rect.bottom = 980

    def bird_reset(self) -> None:  # madarat visszaállítja eredeti helyzetére
        self._y_vel = 0
        self._rect.x = 150
        self._rect.y = 200

    def leg_swap(self) -> None:  # madár lábait megcseréli
        self.bird_leg = self.bird_leg * -1
