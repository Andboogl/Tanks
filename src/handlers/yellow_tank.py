"""Yellow tank handling"""


import pygame
import settings
import objects


class YellowTankHandler:
    """Yellow tank handler"""
    def __init__(self, screen, yellow_tank) -> None:
        self.__screen = screen
        self.__yellow_tank = yellow_tank
        self.__yellow_tank_bullets = []

    def movement(self) -> None:
        """Yellow tank movement"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.__yellow_tank.move_tank('top')

        elif keys[pygame.K_a]:
            self.__yellow_tank.move_tank('left')

        elif keys[pygame.K_s]:
            self.__yellow_tank.move_tank('down')

        elif keys[pygame.K_d]:
            self.__yellow_tank.move_tank('right')

    def rotation_and_shooting(self, event) -> None:
        """Yellow tank keyboard handling"""
        if event.key == pygame.K_w:
            self.__yellow_tank.rotate_tank(settings.top_rotation)

        elif event.key == pygame.K_a:
            self.__yellow_tank.rotate_tank(settings.left_rotation)

        elif event.key == pygame.K_s:
            self.__yellow_tank.rotate_tank(settings.down_rotation)

        elif event.key == pygame.K_d:
            self.__yellow_tank.rotate_tank(settings.right_rotation)

        elif event.key == pygame.K_SPACE:
            if len(self.__yellow_tank_bullets) <= 0:
                self.__yellow_tank_bullets.append(objects.Bullet(self.__screen, self.__yellow_tank))

    def draw(self) -> None:
        """Draw yellow tank and its bullets"""
        self.__yellow_tank.draw()

        for bullet in self.__yellow_tank_bullets:
            bullet.draw()
            bullet.update()

            # Bullet deletion
            if bullet.rotation == 0:
                if bullet.y + bullet.width < 0:
                    self.__yellow_tank_bullets.remove(bullet)

            elif bullet.rotation == 90:
                if bullet.x < 0:
                    self.__yellow_tank_bullets.remove(bullet)

            elif bullet.rotation == 180:
                if bullet.y - bullet.width > settings.window_size[1]:
                    self.__yellow_tank_bullets.remove(bullet)

            elif bullet.rotation == 270:
                if bullet.x - bullet.width > settings.window_size[0]:
                    self.__yellow_tank_bullets.remove(bullet)
