import pygame
from pygame.draw import *

pygame.init()

FPS = 24
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
WHITE = (240, 240, 240)
RED = (255, 0, 0)
pi = 3.1415926


def draw_face(surface, x, y, height, width, color):
    '''
        function draws rabbit's face

        Parameters
        ----------
        6 components pygame.surface, int, int, int, int, tuple(int, int)
        surface -- surface on which rabbit's face will be drawn
        x, y -- coordinates of up-left corner
        height, width -- height and width of picture
        color -- rabbit face's color

        Returns
        -------
        Return type is void
        '''
    circle(surface, color, (x + width // 2 - width // 40, y + height // 3 + height // 12), width // 50)
    line(surface, color, (x + 102 * width // 200, y + 120 * height // 300),
         (x + 107 * width // 200, y + 129 * height // 300), 5)
    line(surface, color, (x + 107 * width // 200, y + 120 * height // 300),
         (x + 102 * width // 200, y + 129 * height // 300), 5)
    arc(surface, color, (x + width // 2 - width // 40, y + height // 3 + height // 15, width // 20, height // 12),
        pi * 1.1, -pi / 5, 3)


def draw_ear(surface, x, y, height, width, color):
    '''
        function draws rabbit's ears

        Parameters
        ----------
        6 components pygame.surface, int, int, int, int, tuple(int, int)
        surface -- surface on which rabbit's ears will be drawn
        x, y -- coordinates of up-left corner
        height, width -- height and width of picture
        color -- rabbit ear's color

        Returns
        -------
        Return type is void
        '''
    arc(surface, color, (x + width // 2 + width // 40, y, width // 40, 7 * height // 20), 3 * pi / 2, pi)
    arc(surface, color, (x + width // 2 - width // 20, y, width // 40, 7 * height // 20), 0, 3 * pi / 2)


def draw_head(surface, x, y, height, width, color):
    '''
        function draws rabbit's head

        Parameters
        ----------
        6 components pygame.surface, int, int, int, int, tuple(int, int)
        surface -- surface on which rabbit's head will be drawn
        x, y -- coordinates of up-left corner
        height, width -- height and width of picture
        color -- rabbit head's color

        Returns
        -------
        Return type is void
        '''
    ellipse(surface, color, (x + width // 2 - width // 20, y + height // 3, width // 10, height // 6))
    draw_face(surface, x, y, height, width, color)
    draw_ear(surface, x, y, height, width, color)


def draw_wings(surface, x, y, height, width, color):
    '''
        function draws rabbit's wings

        Parameters
        ----------
        6 components pygame.surface, int, int, int, int, tuple(int, int)
        surface -- surface on which rabbit's wings will be drawn
        x, y -- coordinates of up-left corner
        height, width -- height and width of picture
        color -- rabbit wing's color

        Returns
        -------
        Return type is void
        '''
    m = ((width // 2, 3 * height // 5), (5 * width // 7, height // 6), (95 * width // 100, 2 * height // 5),
         (4 * width // 5, 3 * height // 5), (95 * width // 100, 4 * height // 5), (9 * width // 14, 6 * height // 7),
         (width // 2, 5 * height // 6))

    for i in range(1, 7):
        line(surface, color, (x + m[i - 1][0], y + m[i - 1][1]), (x + m[i][0], y + m[i][1]), 3)
        line(surface, color, (x + width - m[i - 1][0], y + m[i - 1][1]), (x + width - m[i][0], y + m[i][1]), 3)


def draw_body(surface, x, y, height, width, color):
    '''
        function draws rabbit's body

        Parameters
        ----------
        6 components pygame.surface, int, int, int, int, tuple(int, int)
        surface -- surface on which rabbit's body will be drawn
        x, y -- coordinates of up-left corner
        height, width -- height and width of picture
        color -- rabbit's body's color

        Returns
        -------
        Return type is void
        '''
    ellipse(surface, color, (x + width // 2 - width // 20, y + height // 2, width // 10, height // 2))
    draw_wings(surface, x, y, height, width, color)


def draw_rabbit(surface, x, y, height, width, color):
    '''
    function draws rabbit, size width * height

    Parameters
    ----------
    6 components pygame.surface, int, int, int, int, tuple(int, int)
    surface -- surface on which rabbit will be drawn
    x, y -- coordinates of up-left corner
    height, width -- height and width of picture
    color -- rabbit's color

    Returns
    -------
    Return type is void
    '''
    draw_body(surface, x, y, height, width, color)
    draw_head(surface, x, y, height, width, color)
    draw_face(surface, x, y, height, width, (255, 0, 0))


draw_rabbit(screen, 0, 0, screen_width, screen_height, WHITE)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
