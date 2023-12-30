"""Won menu"""


import pygame
import settings


class WonMenu:
    """Won menu"""
    def __init__(self, screen, who_won) -> None:
        self.__screen = screen
        self.__title_text = 'Green won!' if who_won == 'green' else 'Yellow won!'
        self.__title_color = (0, 255, 0) if who_won == 'green' else (255, 255, 0)
        self.__title_font = pygame.font.Font('fonts/RubikLines.ttf', 80)
        self.__play_again_font = pygame.font.Font('fonts/RubikLines.ttf', 50)

    def draw(self) -> str:
        """Draw won menu"""
        self.__screen.fill(settings.window_background_color)

        # Title
        title_text = self.__title_font.render(self.__title_text, True, self.__title_color)
        title_x = settings.window_size[0] / 2 - (title_text.get_width() / 2)
        title_y = 10
        self.__screen.blit(
            title_text,
            (title_x, title_y)
        )

        # Play again button
        play_again_text = self.__play_again_font.render('Play again', True, settings.text_color)
        play_again_text_x = settings.window_size[0] / 2 - (play_again_text.get_width() / 2)
        play_again_text_y = settings.window_size[1] / 2 - (play_again_text.get_height() / 2)
        play_again_text_rect = play_again_text.get_rect(topleft=(play_again_text_x, play_again_text_y))
        self.__screen.blit(play_again_text, (play_again_text_x, play_again_text_y))

        # If user clicked on text play again
        if play_again_text_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return 'Playing'

        return 'Won'
