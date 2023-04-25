import pygame
from settings import screen_width, screen_height

bg_image = pygame.image.load('../images/bg.png')
screen = pygame.display.set_mode((screen_width, screen_height))
bg_scroll = 0

def draw_bg(bg_scroll):
    screen.blit(bg_image, (0, 0 + bg_scroll))
    screen.blit(bg_image, (0, -600 + bg_scroll))