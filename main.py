import pygame
from sys import exit
import random
import math

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

    pygame.display.update()
    clock.tick(60)