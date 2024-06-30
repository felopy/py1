"""
A Pygame program where the objective is to catch falling balls with a cart. The game ends
either when the player loses all chances or when they score 100 point.
create by: Feliks Voskanyan
date: 29.06.2024
"""

import sys
from random import randint
import pygame
from ball import Ball

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 300)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 1600, 850

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60

cart_image = pygame.image.load('shield_man.jpg').convert_alpha()

cart_image_transparent = pygame.Surface(cart_image.get_size(), pygame.SRCALPHA)

cart_image = pygame.image.load('shield_man.jpg').convert_alpha()
cart_image = pygame.transform.scale(cart_image, (100, 100))
cart_image.set_colorkey((255, 255, 255))
cart_image_transparent = pygame.transform.scale(cart_image_transparent, (100, 100))

cart_rect = cart_image.get_rect(centerx=WIDTH // 2, bottom=HEIGHT - 5)

background = pygame.image.load('top.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

balls_data = [{'path': 'b1.jpeg'},
              {'path': 'b2.jpeg'},
              {'path': 'b3.jpeg'}]

balls_surf = []
"""makes the white part of the balls transparent"""
for data in balls_data:
    image = pygame.image.load(data['path']).convert_alpha()
    transparent_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            color = image.get_at((x, y))
            if color != (255, 255, 255, 255):
                transparent_image.set_at((x, y), color)
    balls_surf.append(transparent_image)

BALL_SIZE = (50, 50)

balls = pygame.sprite.Group()

def create_ball(group):
    """Create a new ball and add it to the group."""
    index = randint(0, len(balls_surf) - 1)
    x_position = randint(20, WIDTH - 20)
    speed = randint(1, 4)
    scaled_image = pygame.transform.scale(balls_surf[index], BALL_SIZE)
    Ball(x_position, speed, scaled_image, group)

create_ball(balls)

CART_SPEED = 10

SCORE = 0

CHANCES = 3

font = pygame.font.Font(None, 36)
"""starts the main game cycle"""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            create_ball(balls)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cart_rect.x = max(cart_rect.x - CART_SPEED, 0)
    elif keys[pygame.K_RIGHT]:
        cart_rect.x = min(cart_rect.x + CART_SPEED, WIDTH - cart_rect.width)

    screen.blit(background, (0, 0))
    """in this hole checks the collision of the ball with the human"""
    for ball in balls:
        if cart_rect.colliderect(ball.rect):
            CHANCES -= 1
            ball.kill()
            if CHANCES == 0:
                game_over_surf = font.render("Game Over!", True, (255, 0, 0))
                screen.blit(game_over_surf, (WIDTH // 2 - 100, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.delay(2000)
                pygame.quit()
                sys.exit()

    for ball in balls:
        if ball.rect.bottom >= HEIGHT - 5:
            SCORE += 1
            ball.kill()

    balls.update(HEIGHT)
    balls.draw(screen)

    screen.blit(cart_image, cart_rect)

    chances_surf = font.render(f'Chances: {CHANCES}', True, (255, 255, 255))
    screen.blit(chances_surf, (10, 10))

    score_surf = font.render(f'Score: {SCORE}', True, (255, 255, 255))
    screen.blit(score_surf, (10, 50))

    if SCORE >= 100:
        won_surf = font.render("You Won!", True, (0, 255, 0))
        screen.blit(won_surf, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(FPS)
