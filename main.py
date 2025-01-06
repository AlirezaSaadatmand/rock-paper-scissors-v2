import pygame
from sys import exit
import random
import math
import time

WIDTH , HEIGHT = 1200 , 700

count = 10

RADIUS = 10

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
    def __init__(self , type , ray , point1 , point2):
        self.type = type
        self.ray = ray
        self.x = random.randint(point1[0] , point2[0])
        self.y = random.randint(point1[1] , point2[1])
        self.color = type

    def move(self):
        if self.x > WIDTH // 2 + int(WIDTH * 0.2) or self.x < WIDTH // 2 - int(WIDTH * 0.2):
            self.ray.colide("side")
        if self.y > HEIGHT // 2 + int(WIDTH * 0.2) or self.y < HEIGHT // 2 - int(WIDTH * 0.2):
            self.ray.colide("not side")

        self.x += self.ray.x * SPEED
        self.y += self.ray.y * SPEED

    
    def draw(self):
        pygame.draw.circle(screen, self.color , (self.x , self.y), RADIUS)


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
    pygame.draw.rect(screen, "white", pygame.Rect(WIDTH // 2 - int(WIDTH * 0.2) - RADIUS , HEIGHT // 2 - int(WIDTH * 0.2) - RADIUS , int(WIDTH * 0.2) * 2 + RADIUS * 2, int(WIDTH * 0.2) * 2 + RADIUS * 2))
    for particle in particles:
        particle.move()
        particle.draw()

def change():
    global GREEN , BLUE , RED , YELLOW , PURPLE
    for i in particles:
        for j in particles:
            if math.dist([i.x , i.y] , [j.x , j.y]) < RADIUS * 2 and i.color != j.color:
                sound_effect.stop()
                sound_effect.play()
                if i.color == "red" and j.color == "green":
                    j.color = "red"
                    RED += 1
                    GREEN -= 1 
                elif i.color == "red" and j.color == "blue":
                    j.color = "red"
                    RED += 1
                    BLUE -= 1

                elif i.color == "blue" and j.color == "green":
                    j.color = "blue"
                    BLUE += 1
                    GREEN -= 1
                elif i.color == "blue" and j.color == "purple":
                    j.color = "blue"
                    BLUE += 1
                    PURPLE -= 1

                elif i.color == "green" and j.color == "purple":
                    j.color = "green"
                    GREEN += 1
                    PURPLE -= 1
                elif i.color == "green" and j.color == "yellow":
                    j.color = "green"
                    GREEN += 1
                    YELLOW -= 1
                
                elif i.color == "purple" and j.color == "yellow":
                    j.color = "purple"
                    PURPLE += 1
                    YELLOW -= 1
                elif i.color == "purple" and j.color == "red":
                    j.color = "purple"
                    PURPLE += 1
                    RED -= 1
                
                elif i.color == "yellow" and j.color == "red":
                    j.color = "yellow"
                    YELLOW += 1
                    RED -= 1    
                elif i.color == "yellow" and j.color == "blue":
                    j.color = "yellow"
                    YELLOW += 1
                    BLUE -= 1
  
                # break

def restart():
    global particles , BLUE , RED , GREEN , YELLOW , PURPLE , count
    particles = []
    BLUE = count
    RED = count
    GREEN = count
    YELLOW = count
    PURPLE = count
    for _ in range(BLUE):
        particles.append(Particle("blue", Ray() , (WIDTH // 2 - 200 , HEIGHT // 2 - 200) , (WIDTH // 2 - 100 , HEIGHT // 2 - 100)))

    for _ in range(RED):
        particles.append(Particle("red", Ray() , (WIDTH // 2 - 200 , HEIGHT // 2 + 100) , (WIDTH // 2 - 100 , HEIGHT // 2 + 200)))

    for _ in range(GREEN):
        particles.append(Particle("green", Ray() , (WIDTH // 2 - 50 , HEIGHT // 2 - 50) , (WIDTH // 2 + 50 , HEIGHT // 2 + 50)))

    for _ in range(YELLOW):
        particles.append(Particle("yellow", Ray() , (WIDTH // 2 + 100 , HEIGHT // 2 - 200) , (WIDTH // 2 + 200 , HEIGHT // 2 - 100)))

    for _ in range(PURPLE):
        particles.append(Particle("purple", Ray() , (WIDTH // 2 + 100 , HEIGHT // 2 + 100) , (WIDTH // 2 + 200 , HEIGHT // 2 + 200)))

restart()

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode( (WIDTH , HEIGHT)) 
clock = pygame.time.Clock()

sound_effect = pygame.mixer.Sound("sound_effects/sound_effect3.wav")
sound_effect.set_volume(0.2) 

pygame.mixer.music.load("sound_effects/background_sound_effect.mp3")
pygame.mixer.music.play(loops=-1)
while True:
    screen.fill("black")
    screen.blit(screen,(0,0))
    pygame.display.set_caption(f" FPS : {round(clock.get_fps())} Color Fight")
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    color_count = pygame.font.Font(None, 30)
    color_count = color_count.render(f"blue : {BLUE}    red : {RED}    green : {GREEN}    yellow : {YELLOW}    purple : {PURPLE}", True, "white")
    color_count_rect = color_count.get_rect(center=(WIDTH / 2, 70))
    screen.blit(color_count , color_count_rect)

    blue_win_count = pygame.font.Font(None, 30)
    blue_win_count = blue_win_count.render(f"blue : {blue_win}", True, "blue")
    blue_win_count_rect = blue_win_count.get_rect(center=(200, HEIGHT / 2))
    screen.blit(blue_win_count , blue_win_count_rect)

    red_win_count = pygame.font.Font(None, 30)
    red_win_count = red_win_count.render(f"red : {red_win}", True, "red")
    red_win_count_rect = red_win_count.get_rect(center=(200, HEIGHT / 2 - 30))
    screen.blit(red_win_count , red_win_count_rect)

    green_win_count = pygame.font.Font(None, 30)
    green_win_count = green_win_count.render(f"green : {green_win}", True, "green")
    green_win_count_rect = green_win_count.get_rect(center=(200, HEIGHT / 2 + 30))
    screen.blit(green_win_count , green_win_count_rect)

    yellow_win_count = pygame.font.Font(None, 30)
    yellow_win_count = yellow_win_count.render(f"yellow : {yellow_win}", True, "yellow")
    yellow_win_count_rect = yellow_win_count.get_rect(center=(200, HEIGHT / 2 + 60))
    screen.blit(yellow_win_count , yellow_win_count_rect)

    purple_win_count = pygame.font.Font(None, 30)
    purple_win_count = purple_win_count.render(f"purple : {purple_win}", True, "purple")
    purple_win_count_rect = purple_win_count.get_rect(center=(200, HEIGHT / 2 - 60))
    screen.blit(purple_win_count , purple_win_count_rect)


    if not (RED == count * 5 or BLUE == count * 5 or GREEN == count * 5 or YELLOW == count * 5 or PURPLE == count * 5):
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