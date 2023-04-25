import pygame
from frog import *


screen = pygame.display.set_mode((screen_width, screen_height))
jumpy = Player(screen_width // 2, screen_height - 150)
game_over = False

fade_counter = 0

def check_game_over():
    if jumpy.rect.top > screen_height:
        game_over = True
def fade_counter_func():
    global fade_counter
    if fade_counter < screen_width:
        fade_counter += 5
        for y in range(0, 7, 2):
            pygame.draw.rect(screen, (55, 212, 223), (0, y * 100, fade_counter, 100))
            pygame.draw.rect(screen, (58, 194, 203),
                                (screen_width - fade_counter, (y + 1) * 100, screen_width, 100))
