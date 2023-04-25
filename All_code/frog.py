import pygame, sys
from platform import *
from settings import *

jumpy_image = pygame.image.load('../images/frog.png')
screen = pygame.display.set_mode((screen_width, screen_height))

class Player:
    def __init__(self, x, y,):
        self.image = pygame.transform.scale(jumpy_image, (45, 45))
        self.width = 30
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.player_gravity = 1
        self.vel_y = 0


    def move(self):
        #needed veriables
        dy = 0
        scroll = 0
        # player gravity
        self.vel_y += self.player_gravity
        dy += self.vel_y

        # keys pressed
        # moves right and left
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += 10
        if key[pygame.K_LEFT]:
            self.rect.x -= 10

        #collisions with right and left walls
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.left <= 0:
            self.rect.left = 0

        # collisions with platforms
        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = -20


        # check if the player bounced to the top of the screen
        if self.rect.top <= scroll_thrash:
            if self.vel_y < 0:
                scroll = -dy

        # update rect position
        self.rect.y += dy + scroll

        return scroll

    def draw(self):
        screen.blit(self.image, (self.rect.x - 8, self.rect.y - 5))
