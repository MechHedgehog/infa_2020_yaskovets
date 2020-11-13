import pygame
from pygame.draw import *
from random import randint
import math

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TEAL = (0, 128, 128)
OLIVE = (128, 128, 0)
COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN, TEAL, OLIVE]
NUM_OF_TARGETS = 3

class Ball:
    def __init__(self, x=60, y=450):
        """ Конструктор класса ball

        Args:
        x, y - coordinates of center
        x - horizontal
        y - vertical
        r - radius
        vx - horizontal speed
        vy - vertical speed
        live - lifetime of ball
        get_time - detector of hitting
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.ay = 10
        self.color = COLORS[randint(0, 6)]
        self.id = circle(screen, self.color, (self.x, self.y), self.r)
        self.live = 15

    def set_speed(self, speed, alpha):
        """
        set new values of speed by direction (alpha)
        :param speed: speed of ball
        :param alpha: angle of direction
        :return: values of horizontal and vertical speed
        """
        self.vx = speed * math.cos(alpha)
        self.vy = speed * math.sin(alpha)

    def draw(self):
        """
        drawing balls in a new location
        """
        circle(screen, self.color, (int(self.x), int(self.y)), self.r)

    def wall_coll(self):
        if self.x - self.r <= 50:
            self.vx *= -1
            self.x = 50 + self.r + 1
        if self.x + self.r >= 700:
            self.vx *= -1
            self.x = 700 - self.r - 1
        if self.y - self.r <= 50:
            self.vy *= -1
            self.y = 50 + self.r + 1
        if self.y + self.r >= 500:
            self.vy *= -1
            self.y = 500 - self.r - 1

    def move(self, dt):
        """moving of ball

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx * dt
        self.y -= self.vy * dt
        self.vy -= self.ay * dt
        self.wall_coll()
        self.live -= dt
        if self.live <= 0:
            self.x = 0
            self.y = 0
            self.r = 0

    def is_hit(self, x, y, r):
        """
        checks hitting with target
        :param x: x coordinate of target
        :param y: y coordinate of target
        :param r: z coordinate of target
        :return: True if hit
                False if missed
        """
        return (x - self.x) ** 2 + (y - self.y) ** 2 <= (self.r + r) ** 2

    def coord(self):#?
        """
        :return: coordinates of ball
        """
        return self.x, self.y, self.r


class Gun:
    def __init__(self, x0=50, y0=450, length=15, width=5, x=65, y=450):
        """

        :param x: horizontal coordinate of center
        :param y: vertical coordinate of center
        :param k: power coefficient

        Args:
        shotflag - flag of shot
        t, t0, t1 - time for timer
        """
        self.x = x
        self.y = y
        self.x0 = x0
        self.y0 = y0
        self.len_0 = length
        self.length = self.len_0
        self.width = width
        self.max_vel = 100
        self.charging = False
        self.ch_start_time = 0
        self.angle = 0

    def set_angle(self, pos):
        """
        define the flight direction of ball
        :param pos: position of mouse
        :return: alpha - angle of direction
        """
        self.angle = math.atan((self.y - pos[1]) / (pos[0] - self.x))
        return self.angle

    def set_lenght(self):
        if self.charging:
            self.length = self.len_0 * ((pygame.time.get_ticks() - self.ch_start_time) / 2000 + 1)
            if self.length > 2 * self.len_0:
                self.length = 2 * self.len_0
        else:
            self.length = self.len_0

    def set_coord(self):
        self.set_angle(pygame.mouse.get_pos())
        self.set_lenght()
        self.x = self.x0 + int(math.cos(self.angle) * self.length)
        self.y = self.y0 - int(math.sin(self.angle) * self.length)

    def start(self):
        """
        beginning of shot
        starts timer for calculating power of shot
        """

        self.charging = True
        self.ch_start_time = pygame.time.get_ticks()

    def power_up(self):
        """
        determines power of shot based on time held down button
        :return: new value of coefficient
        """

        vel = (pygame.time.get_ticks() - self.ch_start_time) // 20
        if vel > self.max_vel:
            vel = self.max_vel
        return vel

    def draw(self, surface):
        line(surface, RED, (self.x0, self.y0), (self.x, self.y), self.width)
        pygame.display.update()


class Target:

    def __init__(self):
        """
        Initializing a new target

        Args:
            x, y - coordinates of center
            r - radius (size)
            vy - vertical speed
        """
        self.color = RED
        self.r = randint(15, 30)
        self.y = randint(200, 350)
        self.x = randint(200, 550)
        self.vy = randint(-30, 30)
        self.vx = randint(-30, 30)
        self.points = 0
        self.live = 1
        circle(screen, self.color, (self.x, self.y), self.r)

    def draw(self):
        """
        drawing of target
        """
        circle(screen, self.color, (int(self.x), int(self.y)), self.r)

    def wall_coll(self):
        if self.x - self.r <= 50:
            self.vx *= -1
            self.x = 50 + self.r + 1
        if self.x + self.r >= 700:
            self.vx *= -1
            self.x = 700 - self.r - 1
        if self.y - self.r <= 50:
            self.vy *= -1
            self.y = 50 + self.r + 1
        if self.y + self.r >= 500:
            self.vy *= -1
            self.y = 500 - self.r - 1

    def move(self, dt):
        """
        moving of target
        :param dt: time (in order to make moving smooth)
        :return:
        """
        self.y += self.vy * dt
        self.x += self.vx * dt
        self.wall_coll()

    def coord(self):
        """
        :return: coordinates of center
        """
        return self.x, self.y, self.r


pygame.init()

comm_font = pygame.font.Font(None, 30)
alert = pygame.font.Font(None, 50)
FPS = 25
dt = 1 / FPS
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
finished = False
g1 = Gun()
bullet = 0
result = 0
balls_pool = []
targets_pool = [Target() for i in range(NUM_OF_TARGETS)]
while not finished:
    rect(screen, WHITE, (50, 100, 650, 400))
    clock.tick(FPS)
    for target in targets_pool:
        target.draw()
    g1.set_coord()
    g1.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            g1.start()
        elif event.type == pygame.MOUSEBUTTONUP:
            g1.charging = False
            v = g1.power_up()
            ball = Ball(x=g1.x, y=g1.y)
            ball.set_speed(v, g1.angle)
            balls_pool += [ball]
            bullet += 1
    for ball in balls_pool:
        for target in targets_pool:
            ball.move(dt)
            ball.draw()
            target.move(dt)
            target.draw()
            if ball.is_hit(*target.coord()):
                target.__init__()
                result += 2

    shots = comm_font.render("Выстрелы " + str(bullet), True, WHITE, BLACK)
    score = comm_font.render("Результат " + str(result - bullet), True, WHITE, BLACK)
    screen.blit(shots, (50, 70))
    screen.blit(score, (50, 500))
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
