"""Block"""


import pygame


class Block:
    """Block"""
    def __init__(self, screen, x, y) -> None:
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__size = (80, 80)
        self.__color = (255, 255, 255)

        self.__image_rect = pygame.rect.Rect(
            self.__x, self.__y, self.__size[0],
            self.__size[1])

    @property
    def x(self) -> int:
        """Get block position on x"""
        return self.__x

    @property
    def y(self) -> int:
        """Get block position on y"""
        return self.__y

    @property
    def image_rect(self) -> pygame.rect.Rect:
        """Get block image rect"""
        return self.__image_rect

    def draw(self):
        """Draw block on the screen"""
        pygame.draw.rect(self.__screen, self.__color, self.__image_rect)
