"""Bullet"""


import pygame


class Bullet:
    """Bullet"""
    def __init__(self, screen, tank) -> None:
        self.__screen = screen
        self.__color = (255, 255, 0) if tank.color == 'yellow' else (0, 255, 0)
        self.__width = 50
        self.__speed = 3
        self.__rotation = tank.rotation
        self.__image = ...

        if tank.rotation == 0:
            self.__x = tank.x + tank.image.get_width() / 2
            self.__y = tank.y - 50

        elif tank.rotation == 90:
            self.__x = tank.x + tank.image.get_width() / 2 - 30
            self.__y = tank.y + tank.image.get_height() / 2 - 1

        elif tank.rotation == 180:
            self.__x = tank.x + tank.image.get_width() / 2 - 2
            self.__y = tank.y - tank.image.get_height() / 2 + 150

        elif tank.rotation == 270:
            self.__x = tank.x + tank.image.get_width() / 2 + 30
            self.__y = tank.y + tank.image.get_height() / 2 + 1

    @property
    def rotation(self) -> int:
        """Get bullet rotation"""
        return self.__rotation

    @property
    def x(self) -> int:
        """Get bullet position on x"""
        return self.__x

    @property
    def y(self) -> int:
        """Get bullet position on y"""
        return self.__y

    @property
    def width(self) -> int:
        """Get bullet width"""
        return self.__width

    @property
    def image(self) -> pygame.rect.Rect:
        """Get bullet image"""
        return self.__image

    def update(self) -> None:
        """Update bullet coordinates"""
        if self.__rotation == 0:
            self.__y -= self.__speed

        elif self.__rotation == 90:
            self.__x -= self.__speed

        elif self.__rotation == 180:
            self.__y += self.__speed

        elif self.__rotation == 270:
            self.__x += self.__speed

    def draw(self) -> None:
        """Draw bullet"""
        if self.__rotation == 0:
            self.__image = pygame.draw.line(
                self.__screen, self.__color, (self.__x, self.__y),
                (self.__x, self.__y + self.__width), 2)

        elif self.__rotation == 90:
            self.__image = pygame.draw.line(
                self.__screen, self.__color, (self.__x, self.__y),
                (self.__x - self.__width, self.__y), 2)

        elif self.__rotation == 180:
            self.__image = pygame.draw.line(
                self.__screen, self.__color, (self.__x, self.__y),
                (self.__x, self.__y - self.__width), 2)

        elif self.__rotation == 270:
            self.__image = pygame.draw.line(
                self.__screen, self.__color, (self.__x, self.__y),
                (self.__x + self.__width, self.__y), 2)
