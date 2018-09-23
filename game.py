import os
import pygame.constants
from constants import *
from player import Player

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Forknife')
clock = pygame.time.Clock()
gameover = False

# create player
p = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(p)
# main loop
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # This would be a quit event.
            gameover = True
    # Drawing
    # screen.blit(background, (0, 0))
    screen.fill(cyan)
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(90)

pygame.quit()
