"""Tank"""


import os
import pygame
import settings


class Tank:
    """Tank"""
    def __init__(self, screen, x: int, y: int, color: str) -> None:
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__size = (70, 70)
        self.__rotation = 0
        self.__speed = 2
        self.__color = color

        # Tank image path
        self.__image_path = os.path.join('images', 'yellow_tank.png')\
            if color.lower() == 'yellow'\
            else os.path.join('images', 'green_tank.png')

        self.__image = pygame.transform.scale(
            pygame.image.load(self.__image_path), self.__size)

    @property
    def color(self):
        return self.__color

    @property
    def x(self) -> int:
        """Get tank x coordinates"""
        return self.__x

    @property
    def y(self) -> int:
        """Get tank y coordinates"""
        return self.__y

    @property
    def image(self):
        """Get tank image"""
        return self.__image

    @property
    def rotation(self) -> int:
        """Get tank rotation"""
        return self.__rotation

    @property
    def color(self) -> str:
        """Get tank color"""
        return self.__color

    def rotate_tank(self, rotation: int) -> None:
        """Rotate tank"""
        self.__rotation = rotation

    def move_tank(self, where: str) -> None:
        """Move tank"""
        where = where.lower()

        if where == 'left':
            if self.__x > 0:
                self.__x -= self.__speed

        elif where == 'right':
            if self.__x + self.__image.get_width() < settings.window_size[0]:
                self.__x += self.__speed

        elif where == 'top':
            if self.__y > 0:
                self.__y -= self.__speed

        elif where == 'down':
            if self.__y + self.__image.get_height() < settings.window_size[1]:
                self.__y += self.__speed

    def draw(self) -> None:
        """Draw tank on the screen"""
        self.__screen.blit(pygame.transform.rotate(self.__image, self.__rotation), (self.__x, self.__y))
