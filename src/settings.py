"""Game settings"""


import pygame


# Window settings
window_size = (1200, 800)
window_caption = 'Tanks'
window_icon = pygame.image.load('images/icon.png')
window_background_color = (0, 0, 0)

text_color = (255, 255, 255)  # Text color
fps = 120  # FPS

# Tanks rotation
top_rotation = 0
left_rotation = 90
down_rotation = 180
right_rotation = 270
