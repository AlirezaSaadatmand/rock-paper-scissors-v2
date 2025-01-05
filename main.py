import pygame
from sys import exit
import random
import math
import time

WIDTH , HEIGHT = 1200 , 700

count = 20

BLUE = count
RED = count
GREEN = count
YELLOW = count
PURPLE = count

blue_win = 0
red_win = 0
green_win = 0
yellow_win = 0
purple_win = 0

SPEED = 2

particles = []

class Particle:
    def __init__(self , type , ray):
        self.type = type
        self.ray = ray
        self.x = random.randint(WIDTH // 2 - 150 , WIDTH // 2 + 150)
        self.y = random.randint(HEIGHT // 2 - 150 , HEIGHT // 2 + 150)
        self.color = type

    def move(self):
        if self.x > WIDTH // 2 + int(WIDTH * 0.15) or self.x < WIDTH // 2 - int(WIDTH * 0.15):
            self.ray.colide("side")
        if self.y > HEIGHT // 2 + int(WIDTH * 0.15) or self.y < HEIGHT // 2 - int(WIDTH * 0.15):
            self.ray.colide("not side")

        self.x += self.ray.x * SPEED
        self.y += self.ray.y * SPEED

    
    def draw(self):
        pygame.draw.circle(screen, self.color , (self.x , self.y), 7)


class Ray:
    def __init__(self):
        self.angle = random.random() * 2 * math.pi
        self.x = math.sin(self.angle)
        self.y = math.cos(2 * math.pi - self.angle)
    
    def colide(self , side):
        if side == "side":
            self.x *= -1
        else:
            self.y *= -1

def move_particles():
    pygame.draw.rect(screen, "white", pygame.Rect(WIDTH // 2 - int(WIDTH * 0.15) - 7 , HEIGHT // 2 - int(WIDTH * 0.15) - 7 , int(WIDTH * 0.15) * 2 + 13, int(WIDTH * 0.15) * 2 + 13))
    for particle in particles:
        particle.move()
        particle.draw()

def change():
    global GREEN , BLUE , RED
    for i in particles:
        for j in particles:
            if math.dist([i.x , i.y] , [j.x , j.y]) < 15:

                if i.color == "red" and j.color == "green":
                    i.color = "green"
                    RED -= 1
                    GREEN += 1 
                elif i.color == "green" and j.color == "blue":
                    i.color = "blue"
                    GREEN -= 1
                    BLUE += 1
                elif i.color == "blue" and j.color == "red":
                    i.color = "red"
                    BLUE -= 1
                    RED += 1
                # break

def restart():
    global particles , BLUE , RED , GREEN , count
    particles = []
    BLUE = count
    RED = count
    GREEN = count
    for _ in range(BLUE):
        particles.append(Particle("blue", Ray()))

    for _ in range(RED):
        particles.append(Particle("red", Ray()))

    for _ in range(GREEN):
        particles.append(Particle("green", Ray()))

    for _ in range(YELLOW):
        particles.append(Particle("yellow", Ray()))

    for _ in range(PURPLE):
        particles.append(Particle("purple", Ray()))

restart()

pygame.init()
screen = pygame.display.set_mode( (WIDTH , HEIGHT)) 
clock = pygame.time.Clock()


while True:
    screen.fill("black")
    screen.blit(screen,(0,0))
    pygame.display.set_caption(f" FPS : {round(clock.get_fps())} Ray Casting")
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    color_count = pygame.font.Font(None, 30)
    color_count = color_count.render(f"blue : {BLUE}    red : {RED}    green : {GREEN}", True, "white")
    color_count_rect = color_count.get_rect(center=(WIDTH / 2, 100))
    screen.blit(color_count , color_count_rect)

    blue_win_count = pygame.font.Font(None, 30)
    blue_win_count = blue_win_count.render(f"blue : {blue_win}", True, "white")
    blue_win_count_rect = blue_win_count.get_rect(center=(200, HEIGHT / 2))
    screen.blit(blue_win_count , blue_win_count_rect)

    red_win_count = pygame.font.Font(None, 30)
    red_win_count = red_win_count.render(f"red : {red_win}", True, "white")
    red_win_count_rect = red_win_count.get_rect(center=(200, HEIGHT / 2 - 30))
    screen.blit(red_win_count , red_win_count_rect)

    green_win_count = pygame.font.Font(None, 30)
    green_win_count = green_win_count.render(f"green : {green_win}", True, "white")
    green_win_count_rect = green_win_count.get_rect(center=(200, HEIGHT / 2 + 30))
    screen.blit(green_win_count , green_win_count_rect)


    if not (RED == count * 5 or BLUE == count * 5 or GREEN == count * 5):
        change()
        move_particles()
    else:
        if RED == count * 5:
            red_win += 1
        elif BLUE == count * 5:
            blue_win += 1
        elif GREEN == count * 5:
            green_win += 1
        elif YELLOW == count * 5:
            yellow_win += 1
        elif PURPLE == count * 5:
            purple_win += 1

        time.sleep(1)
        restart()

    pygame.display.update()
    clock.tick(60)