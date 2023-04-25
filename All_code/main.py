import pygame, sys, os
from settings import *
from All_code.frog import Player
from platform import *
from bg import *
from Game_Over import *



import random

pygame.init()
clock = pygame.time.Clock()

first_font = pygame.font.SysFont('../font/Roboto-Black.ttf', 40)
second_font = pygame.font.SysFont('../font/Roboto-Black.ttf', 30)

if os.path.exists('score.txt'):
    with open('score.txt', 'r') as file:
        high_score = int(file.read())
else:
    high_score = 0
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jumpy")

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_panel():
    pygame.draw.rect(screen, (55, 212, 223), (0, 0, screen_width, 30))
    pygame.draw.line(screen, 'white', (0, 30), (screen_width, 30), 2)
    draw_text("SCORE:  %s" %score, first_font, 'white', 0, 0)

#player instances
jumpy = Player(screen_width // 2, screen_height - 150)


platform = Platform(screen_width // 2 - 50, screen_height - 50, 100, False)
platform_group.add(platform)


while run:
    clock.tick(fps)

    if game_over == False:
       "STARTING DISPLAYING"
       scroll = jumpy.move()
       #bg
       bg_scroll += scroll
       if bg_scroll >= 600:
            bg_scroll = 0
       draw_bg(bg_scroll)
       #generate platforms
       if len(platform_group) < max_platforms:
            p_w = random.randint(40, 60)
            p_x = random.randint(0, screen_width - p_w)
            p_y = platform.rect.y - random.randint(80, 120)
            p_type = random.randint(1, 2)
            if p_type == 1 and score > 500:
                p_moving = True
            else:
                p_moving = False
            platform = Platform(p_x, p_y, p_w, p_moving)
            platform_group.add(platform)
       # update platforms
       platform_group.update(scroll)

       #update score
       if scroll > 0:
           score += scroll
       #draw line at previos high score
       pygame.draw.line(screen, 'white', (0, score - high_score + scroll_thrash),
                        (screen_width, score - high_score + scroll_thrash), 3)
       draw_text('HIGH SCORE', second_font, 'white', screen_width - 130, score - high_score + scroll_thrash)

       #draw panel
       draw_panel()

       #check game over
       if jumpy.rect.top > screen_height:
           game_over = True

       #draw sprites
       platform_group.draw(screen)
       jumpy.draw()
       "ENDING DISPLAYING"
    else:
        screen.fill(((55, 212, 223)))
        draw_text('GAME OVER!', second_font, 'black', 200, 250)
        draw_text('FINAL SCORE IS  %s' %score, second_font, 'black', 180, 300)
        draw_text('HIGH SCORE IS %s' %high_score, second_font, 'black', 170, 350)
        draw_text('PRESS SPACE TO PLAY AGAIN', second_font, 'black', 130, 400)

        #update high score
        if score > high_score:
            high_score = score
            with open('score.txt', 'w') as file:
                file.write(str(high_score))
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            game_over = False
            score = 0
            scroll = 0
            jumpy.rect.center = (screen_width // 2, screen_height - 150)
            #reset platforms
            platform_group.empty()
            platform = Platform(screen_width // 2 - 50, screen_height - 50, 100, False)
            platform_group.add(platform)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if score > high_score:
                high_score = score
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))
            pygame.quit()
            sys.exit()

    pygame.display.update()


