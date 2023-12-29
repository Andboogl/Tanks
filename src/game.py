"""Game module"""


import pygame
import settings
import objects
import handlers


class Game:
    """Game class"""
    def __init__(self) -> None:
        self.__screen = pygame.display.set_mode(settings.window_size)
        pygame.display.set_caption(settings.window_caption)
        pygame.display.set_icon(settings.window_icon)
        self.__clock = pygame.time.Clock()

        self.__yellow_tank = objects.Tank(self.__screen, 100, 100, 'yellow')
        self.__green_tank = objects.Tank(self.__screen, 500, 500, 'green')

        # Tanks handlers
        self.__yellow_tank_handler = handlers.YellowTankHandler(self.__screen, self.__yellow_tank)
        self.__green_tank_handler = handlers.GreenTankHandler(self.__screen, self.__green_tank)

    def main_loop(self) -> None:
        """Game mainloop"""
        while True:
            self.__screen.fill(settings.window_background_color)

            self.__yellow_tank_handler.draw()
            self.__yellow_tank_handler.movement()

            self.__green_tank_handler.movement()
            self.__green_tank_handler.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)

                elif event.type == pygame.KEYDOWN:
                    self.__yellow_tank_handler.rotation_and_shooting(event)
                    self.__green_tank_handler.rotation_and_shooting(event)

            self.__clock.tick(settings.fps)
            pygame.display.update()
