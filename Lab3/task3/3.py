import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
hedgs_sizes = [(244, 170), (244, 170), (163, 113), (188, 131)]
hedgs_poses = [[150, 625], [400, 300], [60, 150], [300, 300]]
surs = []
surs_clouds = []
nut = pygame.Surface((900, 900))
nut = pygame.image.load('nut.bmp')
nut = pygame.transform.scale(nut, (167, 200))
the_sun = pygame.Surface((280, 270))
the_sun = pygame.image.load('the_sun.bmp')

flag = 0

for i in range(len(hedgs_sizes)):
    surs.append(pygame.Surface((97 * hedgs_sizes[i][0] // 80, 9 * hedgs_sizes[i][1] // 5)))
    surs[i] = pygame.image.load('hedgehog.bmp')
    surs[i].set_colorkey((0, 100, 10))
    surs[i] = pygame.transform.scale(surs[i], hedgs_sizes[i])
    surs[i] = pygame.transform.rotate(surs[i], i * 90)
    
for i in range(3):
    surs_clouds.append([pygame.Surface((210, 140)), randint(30, 70), randint(50, 250), randint(-100, -30), randint(0, 300), randint(2, 4)])
    surs_clouds[i][0].set_colorkey((0,0,0))
    surs_clouds[i][0].set_alpha(surs_clouds[i][2])

    
def draw_hedgehog(x, y, it, flag):  
    if it == 2 and not flag:
        surs[2] = pygame.transform.rotate(surs[2], 180)
    screen.blit(surs[it], (x,y))

    
def draw_clouds():
    for i in range(3):
        sur = surs_clouds[i][0]
        r = surs_clouds[i][1]
        surs_clouds[i][3] += surs_clouds[i][5]
        x = surs_clouds[i][3]
        y = surs_clouds[i][4]
        ellipse(sur, (255, 255, 255), (r // 4, 0, r, r))
        ellipse(sur, (255, 255, 255), (3 * r // 4, 0, r, r))
        ellipse(sur, (255, 255, 255), (5 * r // 4 , 0, r, r))
        ellipse(sur, (255, 255, 255), (r // 4, r // 2, r, r))
        ellipse(sur, (255, 255, 255), (3 * r // 4, r // 2, r, r))
        ellipse(sur, (255, 255, 255), (5 * r // 4, r // 2, r, r))
        ellipse(sur, (255, 255, 255), (0, r // 2, r // 2, r // 2))
        ellipse(sur, (255, 255, 255), (23 * r // 12, r // 2, r // 2, r // 2))
        if x > 800:
            r = surs_clouds[i][1] = randint(30, 70)
            surs_clouds[i][3] = -4 * r
            surs_clouds[i][4] = randint(0, 350)
            surs_clouds[i][2] = randint(50, 250)
            surs_clouds[i][0].set_alpha(randint(50, 250))
            surs_clouds[i][5] = randint(2, 4)
        screen.blit(sur, (x, y))


def draw_back():
    global flag
    rect(screen, (0, 102, 0), (0, 550, 800, 800))
    rect(screen, (0, 172, 230), (0, 0, 800, 550))
    screen.blit(the_sun, (-100, -100)) 
    draw_clouds()
    
    
    rect(screen, (169, 102, 41), (620, 0, 150, 600))
    rect(screen, (34, 34, 17), (220, 0, 90, 580))
    rect(screen, (30, 57, 19), (480, 0, 75, 650))
    rect(screen, (159, 109, 10), (350, 0, 80, 720))
    
    rect(screen, (139, 69, 19), (80, 0, 50, 750))
    screen.blit(nut, (567, 520))
    for i in range(len(hedgs_sizes)):
        draw_hedgehog(hedgs_poses[i][0],hedgs_poses[i][1], i, flag)
    


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    if hedgs_poses[2][1] <= 500:
        hedgs_poses[2][1] += 5
    else:
        flag = 1
    draw_back()
    screen.blit(surs[2], (hedgs_poses[2][0],hedgs_poses[2][1]))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


