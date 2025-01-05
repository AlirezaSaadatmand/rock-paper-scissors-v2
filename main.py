import pygame
from sys import exit

WIDTH , HEIGHT = 1200 , 700

count = 20

BLUE = count
RED = count
GREEN = count

blue_win = 0
red_win = 0
green_win = 0

SPEED = 2

particles = []



pygame.init()
screen = pygame.display.set_mode( (WIDTH , HEIGHT)) 
clock = pygame.time.Clock()


while True:

    pygame.display.set_caption(f" FPS : {round(clock.get_fps())} Ray Casting")
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)