import os
import pygame.constants
from constants import *

os.environ['SDL_VIDEO_CENTERED'] = '1'


pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Forknife')
clock = pygame.time.Clock()
gameover = False


# main loop
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # This would be a quit event.
            gameover = True
    # Drawing
    #screen.blit(background, (0, 0))
    screen.fill(cyan)
    pygame.draw.circle(screen, white, (100, 100), 50)
    pygame.display.update()
    clock.tick(90)

pygame.quit()
