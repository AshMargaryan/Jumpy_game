import pygame
from settings import *
import random

platform_image = pygame.image.load('../images/platform.png')
max_platforms = 10
platform_group = pygame.sprite.Group()


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, moving):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, 10))
        self.rect = self.image.get_rect()
        self.moving = moving
        self.move_counter = random.randint(0, 50)
        self.direction = random.choice([-1, 1])
        self.speed = random.randint(1, 2)
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):
        if self.moving == True:
            self.move_counter += 1
            self.rect.x += self.direction  * self.speed
        if self.move_counter >= 100 or self.rect.left < 0 or self.rect.right > screen_width:
            self.direction *= -1
            self.move_counter = 0
        #update platforms vertical position
        self.rect.y += scroll
        if self.rect.top > screen_height:
            self.kill()
    def first_platforms(self):
         platform = Platform(screen_width // 2 - 50, screen_height - 50, 100)
         platform_group.add(platform)
    def generating_platforms(self):
        platform = Platform(screen_width // 2 - 50, screen_height - 50, 100)
        p_w = random.randint(40, 60)
        p_x = random.randint(0, screen_width - p_w)
        p_y = platform.rect.y - random.randint(80, 120)
        platform = Platform(p_x, p_y, p_w)
        platform_group.add(platform)
