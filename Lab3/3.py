import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
hedgs_sizes = [(160, 80), (160, 80), (120, 55), (140, 65)]
hedgs_poses = [[150, 600], [400, 300], [60, 150], [300, 300]]
surs = []
for i in range(len(hedgs_sizes)):
   surs.append(pygame.Surface((97 * hedgs_sizes[i][0] // 80, 9 * hedgs_sizes[i][1] // 5), pygame.SRCALPHA))


def draw_body(hed_len, hed_whd, it):
    '''
    Рисует тело ёжика.
    
    -----------
    Parametrs:
    
    hed_len : int 
        длинна ёжика.
        
    hed_whd : int
        высота ёжика.
        
    it : Surface
        Холст pygame, где будет нарисовано тело ёжика
        
    ----------
    Возвращаемые значения: 
        None 
    '''
    ellipse(surs[it], (75, 85, 35), (0, 3 * hed_whd // 5, hed_len, hed_whd))
    ellipse(surs[it], (255, 255, 255), (0, 3 * hed_whd // 5, hed_len, hed_whd), 1) 
    

def draw_paws(hed_len, hed_whd, it):
    '''
    Рисует лапы ёжика.
    
    -----------
    Parametrs:
    
    hed_len : int 
        длинна ёжика.
        
    hed_whd : int
        высота ёжика.
        
    it : Surface
        Холст pygame, где будет нарисовано тело ёжика
        
    ----------
    Возвращаемые значения: 
        None 
    '''
    ellipse(surs[it], (75, 85, 35), (hed_len // 10, 3 * hed_whd // 5 + 39 * hed_whd // 50, 3 * hed_len // 16, hed_whd // 4))
    ellipse(surs[it], (255, 255, 255), (hed_len // 10, 3 * hed_whd // 5 + 39 * hed_whd // 50, 3 * hed_len // 16, hed_whd // 4), 1)
    
    ellipse(surs[it], (75, 85, 35), (0, 3 * hed_whd // 5 + 17 * hed_whd // 25, hed_len // 4, 3 * hed_whd // 16))
    ellipse(surs[it], (255, 255, 255), (0, 3 * hed_whd // 5 + 17 * hed_whd // 25, hed_len // 4, 3 * hed_whd // 16), 1)
    
    ellipse(surs[it], (75, 85, 35), (7 * hed_len // 10, 3 * hed_whd // 5 + 22 * hed_whd // 25, 5 * hed_len // 32, 9 * hed_whd // 40))
    ellipse(surs[it], (255, 255, 255), (7 * hed_len // 10, 3 * hed_whd // 5 + 22 * hed_whd // 25, 5 * hed_len // 32, 9 * hed_whd // 40), 1)
    
    ellipse(surs[it], (75, 85, 35), (43 * hed_len // 50, 3 * hed_whd // 5 + 13 * hed_whd // 20, 5 * hed_len // 32, 9 * hed_whd // 40))
    ellipse(surs[it], (255, 255, 255), (43 * hed_len // 50, 3 * hed_whd // 5 + 13 * hed_whd // 20, 5 * hed_len // 32, 9 * hed_whd // 40), 1)


def draw_head(hed_len, hed_whd, it):
    '''
    Рисует голову ёжика.
    
    -----------
    Parametrs:
    
    hed_len : int 
        длинна ёжика.
        
    hed_whd : int
        высота ёжика.
        
    it : Surface
        Холст pygame, где будет нарисовано тело ёжика
        
    ----------
    Возвращаемые значения: 
        None 
    '''
    ellipse(surs[it], (75, 85, 35), (9 * hed_len // 10, 3 * hed_whd // 5 + 3 * hed_whd // 10 , 5 * hed_len // 16, 7 * hed_whd // 16))
    ellipse(surs[it], (255, 255, 255), (9 * hed_len // 10, 3 * hed_whd // 5 + 3 * hed_whd // 10 , 5 * hed_len // 16, 7 * hed_whd // 16), 1)

    ellipse(surs[it], (0,0,0), (97 * hed_len // 100, 3 * hed_whd // 5 + 2 * hed_whd // 5, hed_whd // 8, hed_whd // 8))
    ellipse(surs[it], (0,0,0), (106 * hed_len // 100, 3 * hed_whd // 5 + 2 * hed_whd // 5, hed_whd // 8, hed_whd // 8))

    arc(surs[it], (0,0,0), (100 * hed_len // 97, 3 * hed_whd // 5 + hed_whd // 2, 9 * hed_len // 100, hed_whd // 5), 3.1415, 2 * 3.1415)


def mushrum(hed_len, hed_whd, it):
    '''
    Рисует гриб.
    
    -----------
    Parametrs:
    
    hed_len : int 
        длинна ёжика.
        
    hed_whd : int
        высота ёжика.
        
    it : Surface
        Холст pygame, где будет нарисовано тело ёжика
        
    ----------
    Возвращаемые значения: 
        None 
    '''
    ellipse(surs[it], (255,255,255), (0 + hed_len // 4, 3 * hed_whd // 5, hed_len // 8, hed_whd // 3))
    ellipse(surs[it], (255,0,0), (0 + hed_len // 8, 3 * hed_whd // 5 - hed_whd // 10, 3 * hed_len // 8, hed_whd // 5))
                    
    ellipse(surs[it], (255,255,255), (2 * hed_len // 5, 3 * hed_whd // 5 - hed_whd // 30, hed_whd // 15, hed_whd // 15))
    ellipse(surs[it], (255,255,255), (hed_len // 3, 3 * hed_whd // 5, hed_whd // 10, hed_whd // 25))
    ellipse(surs[it], (255,255,255), (hed_len // 4, 3 * hed_whd // 5 - hed_whd // 10, hed_whd // 10, hed_whd // 10))
    ellipse(surs[it], (255,255,255), (hed_len // 5, 3 * hed_whd // 5 - hed_whd // 20, hed_whd // 20, hed_whd // 10))
    ellipse(surs[it], (255,255,255), (hed_len // 6, 3 * hed_whd // 5 + hed_whd // 40, hed_whd // 30, hed_whd // 30))
      
      
def draw_spikes(hed_len, hed_whd, it):
    '''
    Рисует иголки ёжика.
    
    -----------
    Parametrs:
    
    hed_len : int 
        длинна ёжика.
        
    hed_whd : int
        высота ёжика.
        
    it : Surface
        Холст pygame, где будет нарисовано тело ёжика
        
    ----------
    Возвращаемые значения: 
        None 
    '''
    for i in range(4):
        start_pos_x = int((0.05 + (i == 0) * 0.1) * hed_len)
        if(i == 3):
            start_pos_x = int(0.28 * hed_len)
        start_pos_y = int(3 * hed_whd // 5 + hed_whd * (i + 1) / 5)
        
        for j in range(8 + (i != 0) - (i == 3) * 3):
            spikes = [
                [(start_pos_x + 3 * hed_len // 100, start_pos_y - 4 * hed_whd // 5), (start_pos_x + 6 * hed_len // 100, start_pos_y)],
                [(start_pos_x - hed_len // 25, start_pos_y - 84 * hed_whd // 125), (start_pos_x + 3 * hed_len // 50, start_pos_y - 6 * hed_whd // 125)],
                [(start_pos_x - hed_len // 5, start_pos_y - 68 * hed_whd // 125), (start_pos_x + hed_len // 25, start_pos_y - 2 * hed_whd // 25)],
                [(start_pos_x + 3 * hed_len // 25, start_pos_y - 84 * hed_whd // 125), (start_pos_x + 3 * hed_len // 50, start_pos_y + 6 * hed_whd // 125)],
                [(start_pos_x + hed_len // 5, start_pos_y - 68 * hed_whd // 125), (start_pos_x + hed_len // 25, start_pos_y + 2 * hed_whd // 25)]
             ]
            for k in range(5):
                polygon(surs[it], (0,0,0),[ (start_pos_x,start_pos_y), *spikes[k], (start_pos_x, start_pos_y)])
                if i == 2:
                    mushrum(hed_len, hed_whd, it)
                    ellipse(surs[it], (255, 69,0), (5 * hed_len // 7, 3 * hed_whd // 5 , hed_whd // 3, hed_whd // 3))
                    ellipse(surs[it], (255, 69,0), (3 * hed_len // 7, 3 * hed_whd // 5 + hed_whd // 6, hed_whd // 3, hed_whd // 3)) 
            start_pos_x += hed_len // 10

    
def draw_hedgehog(x, y, hed_len, hed_whd, it):
    '''
    Рисует ёжика.
    
    -----------
    Parametrs:
        
    x : int
        координата левой границы холста с ёжиком
        
    y : int
        координата верхней границы холста с ёжиком
    
    hed_len : int 
        длинна ёжика.
        
    hed_whd : int
        высота ёжика.
        
    it : Surface
        Холст pygame, где будет нарисовано тело ёжика
        
    ----------
    Возвращаемые значения: 
        None 
    '''
    draw_body(hed_len, hed_whd, it)
    draw_paws(hed_len, hed_whd, it)
    draw_head(hed_len, hed_whd, it)
    draw_spikes(hed_len, hed_whd, it)
    surs[it] = pygame.transform.rotate(surs[it], it * 90)
    screen.blit(surs[it], (x,y))
    

def draw_back():
    '''
    Рисует задний фон (деревья, солнце, небо, земля), на котором нет анимированных объектов.
    
    -----------
    Parametrs:
        
    ----------
    Возвращаемые значения: 
        None 
    '''
    rect(screen, (0, 100, 10), (0, 550, 800, 800))
    rect(screen, (40, 45, 245), (0, 0, 800, 550))

    ellipse(screen, (255,255,0), (-100,-100,200, 200)) 
    
    rect(screen, (139, 69, 19), (80, 0, 50, 750))
    rect(screen, (139, 69, 19), (620, 0, 150, 600))
    rect(screen, (139, 69, 19), (220, 0, 90, 580))
    rect(screen, (139, 69, 19), (480, 0, 75, 650))
    rect(screen, (139, 69, 19), (350, 0, 80, 720))

    
def kost():
    '''
    Рисует задний фон, на котором есть анимированный объект.
    
    -----------
    Parametrs:
  
    ----------
    Возвращаемые значения: 
        None 
    '''
    rect(screen, (0,100,10), (0,550,220, 40))
    rect(screen, (40, 45, 245), (0, 0, 220, 550))
    ellipse(screen, (255,255,0), (-100,-100,200, 200)) 
    rect(screen, (139, 69, 19), (80, 0, 50, 750))

    
draw_back()
for i in range(len(hedgs_sizes)):
    draw_hedgehog(hedgs_poses[i][0],hedgs_poses[i][1], hedgs_sizes[i][0],hedgs_sizes[i][1], i)
    surs[i] = pygame.transform.rotate(surs[i], 90 * i)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)


    if hedgs_poses[2][1] <= 500:
        hedgs_poses[2][1] += 5
        kost()
        screen.blit(surs[2], (hedgs_poses[2][0],hedgs_poses[2][1]))
        pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

