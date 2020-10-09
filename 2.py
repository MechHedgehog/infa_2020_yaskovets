import pygame
from pygame.draw import *


pygame.init()

FPS = 24
screen = pygame.display.set_mode((800, 800))

def draw_face(x, y, r, flag):
    circle(screen, (255, 255, 0), (x, y), r)
    circle(screen, (255, 255, 255), (x, y), r, 3)

    line(screen, (0,0,0), (x - r//2, y + r//2), (x + r//2, y + r//2), 3 * r // 15)

    circle(screen, (255, 0, 0), (x - r//2, y - r//6), r//5)
    circle(screen, (0, 0, 0), (x - r//2, y - r//6), r//10)

    circle(screen, (255, 0, 0), (x + r//2, y - r//6), r//5)
    circle(screen, (0, 0, 0), (x + r//2, y - r//6), r//10)
    if flag:
        line(screen, (0,0,0), (x - 16 * r //15 , y - 31 * r // 30), (x - 4 * r // 15, y - 4 * r // 15), 2 * r // 15)
        line(screen, (0,0,0), (x + 13 * r // 15, y - 19 * r // 30), (x + r // 5 , y - 3 * r // 10), 2 * r // 15)
    else:
        line(screen, (0,0,0), (x - 16 * r // 15, y - r // 3), (x - 4 * r // 15, y - 9 * r // 20), 2 * r // 15)
        line(screen, (0,0,0), (x + 16 * r // 15, y - r // 3), (x + 4 * r // 15, y - 9 * r // 20), 2 * r // 15)

    polygon(screen, (0,0,0), [(x, y + r // 30), (x - r // 6, y + r // 6), (x + r // 6, y + r // 6), (x, y + r // 30)])

n = int(input("input number of faces (better even number): "))
r = int(1600 / (3 * n))
for i in range(n):
    draw_face((i % 2) * r // 2 + r // 2 + r + (i // 2) * 3 * r ,r + 2 * r * (i % 2) , r, i % 2)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
