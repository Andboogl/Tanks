"""Game module"""


import pygame
import settings
import objects
import handlers
from won_menu import WonMenu


class Game:
    """Game class"""
    def __init__(self) -> None:
        pygame.init()

        self.__screen = pygame.display.set_mode(settings.window_size)
        pygame.display.set_caption(settings.window_caption)
        pygame.display.set_icon(settings.window_icon)
        self.__clock = pygame.time.Clock()

        # Tanks
        self.__yellow_tank = objects.Tank(self.__screen, 1125, 10, 'yellow')
        self.__green_tank = objects.Tank(self.__screen, 1125, 725, 'green')

        # Blocks
        self.__blocks = [
            objects.Block(self.__screen, 79, 99),
            objects.Block(self.__screen, 260, 100),
            objects.Block(self.__screen, 99, 297),
            objects.Block(self.__screen, 397, 167),
            objects.Block(self.__screen, 418, 386),
            objects.Block(self.__screen, 99, 555),
            objects.Block(self.__screen, 300, 584),
            objects.Block(self.__screen, 300, 300),
            objects.Block(self.__screen, 200, 200),
            objects.Block(self.__screen, 560, 504),
            objects.Block(self.__screen, 661, 337),
            objects.Block(self.__screen, 833, 466),
            objects.Block(self.__screen, 816, 233),
            objects.Block(self.__screen, 816, 233),
            objects.Block(self.__screen, 833, 466),
            objects.Block(self.__screen, 1090, 337),
            objects.Block(self.__screen, 1090, 337),
            objects.Block(self.__screen, 1090, 337),
            objects.Block(self.__screen, 1090, 337),
            objects.Block(self.__screen, 1090, 337),
        ]

        self.__play_mode = 'Playing'
        self.__who_won = None

        # Tanks handlers
        self.__yellow_tank_handler = handlers.YellowTankHandler(self.__screen, self.__yellow_tank)
        self.__green_tank_handler = handlers.GreenTankHandler(self.__screen, self.__green_tank)

    def main_loop(self) -> None:
        """Game mainloop"""
        while True:
            if self.__play_mode == 'Playing':
                self.__screen.fill(settings.window_background_color)

                self.__yellow_tank_handler.draw()
                self.__yellow_tank_handler.movement(self.__blocks)

                self.__green_tank_handler.movement(self.__blocks)
                self.__green_tank_handler.draw()

                # Drawing blocks
                for block in self.__blocks:
                    block.draw()

                # Green tank bullet kill
                for bullet in self.__green_tank_handler.bullets:
                    if bullet.image.colliderect(
                            self.__yellow_tank.image.get_rect(
                                topleft=(self.__yellow_tank.x, self.__yellow_tank.y))):
                        self.__play_mode = 'Won'
                        won_menu = WonMenu(self.__screen, 'green')
                        pygame.mixer.Sound('sounds/won.mp3').play()

                # Yellow tank bullet kill
                for bullet in self.__yellow_tank_handler.bullets:
                    if bullet.image.colliderect(
                            self.__green_tank.image.get_rect(
                                topleft=(self.__green_tank.x, self.__green_tank.y))):
                        self.__play_mode = 'Won'
                        won_menu = WonMenu(self.__screen, 'yellow')
                        pygame.mixer.Sound('sounds/won.mp3').play()

                # Bullet destroys block
                try:
                    for bullet in self.__yellow_tank_handler.bullets:
                        for block in self.__blocks:
                            if bullet.image.colliderect(block.image_rect):
                                self.__blocks.remove(block)
                                self.__yellow_tank_handler.bullets.remove(bullet)
                                pygame.mixer.Sound('sounds/destroying_block.mp3').play()

                    for bullet in self.__green_tank_handler.bullets:
                        for block in self.__blocks:
                            if bullet.image.colliderect(block.image_rect):
                                self.__blocks.remove(block)
                                self.__green_tank_handler.bullets.remove(bullet)
                                pygame.mixer.Sound('sounds/destroying_block.mp3').play()

                # If the bullet hits two blocks at once
                except (Exception, ValueError):
                    pass

            elif self.__play_mode == 'Won':
                self.__play_mode = won_menu.draw()

                if self.__play_mode == 'Playing':
                    self.__init__()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit(0)

                if self.__play_mode == 'Playing':
                    if event.type == pygame.KEYDOWN:
                        self.__yellow_tank_handler.rotation_and_shooting(event)
                        self.__green_tank_handler.rotation_and_shooting(event)

            self.__clock.tick(settings.fps)
            pygame.display.update()
