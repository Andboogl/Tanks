"""Green tank handling"""


import pygame
import settings
import objects


class GreenTankHandler:
    """Green tank handler"""
    def __init__(self, screen, green_tank) -> None:
        self.__screen = screen
        self.__green_tank = green_tank
        self.green_tank_bullets = []

    @property
    def bullets(self) -> list:
        """Get green tank bullets"""
        return self.green_tank_bullets

    def movement(self, blocks_list) -> None:
        """Green tank movement"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            can_move = True

            for block in blocks_list:
                if self.__green_tank.image_rect.colliderect(block.image_rect):
                    if not self.__green_tank.y - 2 < block.y:
                        self.__green_tank.move_tank('down')
                        can_move = False

            if can_move:
                self.__green_tank.move_tank('top')

        elif keys[pygame.K_LEFT]:
            can_move = True

            for block in blocks_list:
                if self.__green_tank.image_rect.colliderect(block.image_rect):
                    if not self.__green_tank.x - 2 < block.x:
                        self.__green_tank.move_tank('right')
                        can_move = False

            if can_move:
                self.__green_tank.move_tank('left')

        elif keys[pygame.K_DOWN]:
            can_move = True

            for block in blocks_list:
                if self.__green_tank.image_rect.colliderect(block.image_rect):
                    if not self.__green_tank.y + 2 > block.y:
                        self.__green_tank.move_tank('top')
                        can_move = False

            if can_move:
                self.__green_tank.move_tank('down')

        elif keys[pygame.K_RIGHT]:
            can_move = True

            for block in blocks_list:
                if self.__green_tank.image_rect.colliderect(block.image_rect):
                    if not self.__green_tank.x + 2 > block.x:
                        self.__green_tank.move_tank('left')
                        can_move = False

            if can_move:
                self.__green_tank.move_tank('right')

    def rotation_and_shooting(self, event) -> None:
        """Green tank keyboard handling"""
        if event.key == pygame.K_UP:
            self.__green_tank.rotate_tank(settings.top_rotation)

        elif event.key == pygame.K_LEFT:
            self.__green_tank.rotate_tank(settings.left_rotation)

        elif event.key == pygame.K_DOWN:
            self.__green_tank.rotate_tank(settings.down_rotation)

        elif event.key == pygame.K_RIGHT:
            self.__green_tank.rotate_tank(settings.right_rotation)

        elif event.key == pygame.K_RETURN:
            self.green_tank_bullets.append(objects.Bullet(self.__screen, self.__green_tank))

    def draw(self) -> None:
        """Draw green tank and its bullets"""
        self.__green_tank.draw()

        for bullet in self.green_tank_bullets:
            bullet.draw()
            bullet.update()

            # Bullet deletion
            if bullet.rotation == 0:
                if bullet.y + bullet.width < 0:
                    self.green_tank_bullets.remove(bullet)

            elif bullet.rotation == 90:
                if bullet.x < 0:
                    self.green_tank_bullets.remove(bullet)

            elif bullet.rotation == 180:
                if bullet.y - bullet.width > settings.window_size[1]:
                    self.green_tank_bullets.remove(bullet)

            elif bullet.rotation == 270:
                if bullet.x - bullet.width > settings.window_size[0]:
                    self.green_tank_bullets.remove(bullet)
