import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
screen_width = 1200
screen_height = 800
min_rad = 10
max_rad = 50
max_acc = 5
max_vel = 43
num_of_balls = 10
score = 0
targets_left = 1 + num_of_balls
finished = False
have_friend_param = False
name = ""
code = ""
leaders = []


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]

balls_pool = [
    [randint(screen_width // 10, 9 * screen_width // 10), randint(screen_height // 10, 9 * screen_height // 10),
     randint(min_rad, max_rad), COLORS[randint(0, 6)], randint(-15, 15), randint(-15, 15), randint(1, 3)] for i in
    range(num_of_balls + 1)]

balls_pool[0] = [randint(screen_width // 10, 9 * screen_width // 10),
                 randint(screen_height // 10, 9 * screen_height // 10),
                 randint(2 * min_rad, 3 * max_rad // 2), YELLOW, (1 - 2 * randint(0, 1)) * randint(15, 20),
                 (1 - 2 * randint(0, 1)) * randint(20, 25), randint(3, 4), (1 - 2 * randint(0, 1)) * randint(0, 5),
                 (1 - 2 * randint(0, 1)) * randint(0, 5)]

screen = pygame.display.set_mode((screen_width, screen_height))

star_surf = pygame.image.load("star.bmp")
star_surf.set_colorkey((255, 255, 255))
star_surf = pygame.transform.scale(star_surf, (balls_pool[0][2] * 2, balls_pool[0][2] * 2))

font_name = pygame.font.match_font("Arial")


def obj_collis(i):
    """
    function checks collisions of balls with walls
    1 component: int
    :param i: number of ball
    :return: void
    """
    global have_friend_param
    flag = 0
    if balls_pool[i][0] + balls_pool[i][2] > 9 * screen_width // 10:  # collision with right wall
        if i == 0 and have_friend_param:
            balls_pool[0][0] = screen_width // 10 + balls_pool[0][2]
        else:
            balls_pool[i][4] *= -1
            balls_pool[i][0] = 9 * screen_width // 10 - balls_pool[i][2]
        flag = 1

    if balls_pool[i][0] - balls_pool[i][2] < screen_width // 10:  # collision with left wall
        if i == 0 and have_friend_param:
            balls_pool[0][0] = 9 * screen_width // 10 - balls_pool[0][2]
        else:
            balls_pool[i][4] *= -1
            balls_pool[i][0] = screen_width // 10 + balls_pool[i][2]
        flag = 1

    if balls_pool[i][1] + balls_pool[i][2] > 9 * screen_height // 10:  # collision with top wall
        if i == 0 and have_friend_param:
            balls_pool[0][1] = screen_height // 10 + balls_pool[0][2]
        else:
            balls_pool[i][5] *= -1
            balls_pool[i][1] = 9 * screen_height // 10 - balls_pool[i][2]
        flag = 1

    if balls_pool[i][1] - balls_pool[i][2] < screen_height // 10:  # collision with bottom wall
        if i == 0 and have_friend_param:
            balls_pool[0][1] = 9 * screen_height // 10 - balls_pool[0][2]
        else:
            balls_pool[i][5] *= -1
            balls_pool[i][1] = screen_height // 10 + balls_pool[i][2]
        flag = 1
    # if ball is star and you haven't a friend, after collision it changes it's speed and acceleration
    if i == 0 and flag == 1 and not have_friend_param:
        balls_pool[0][7] = (1 - 2 * randint(0, 1)) * randint(0, 5)
        balls_pool[0][8] = (1 - 2 * randint(0, 1)) * randint(0, 5)
        if abs(balls_pool[0][4]) > 42:
            balls_pool[0][4] = (1 - 2 * randint(0, 1)) * randint(15, 20)
        if abs(balls_pool[0][5]) > 42:
            balls_pool[0][5] = (1 - 2 * randint(0, 1)) * randint(15, 20)


def draw_balls():
    """
    function draws balls
    0 component:
    :param: none
    :return: void
    """
    for i in range(1, num_of_balls + 1):
        if balls_pool[i][6] <= 0:
            continue
        balls_pool[i][0] += balls_pool[i][4]
        balls_pool[i][1] += balls_pool[i][5]
        obj_collis(i)
        circle(screen, balls_pool[i][3], (balls_pool[i][0], balls_pool[i][1]), balls_pool[i][2])


def draw_star():
    """
    function draws star
    0 component:
    :param: none
    :return: void
    """
    global star_surf, max_vel
    if balls_pool[0][6] <= 0:
        return
    balls_pool[0][4] += balls_pool[0][7]
    balls_pool[0][5] += balls_pool[0][8]
    balls_pool[0][0] += balls_pool[0][4]
    balls_pool[0][1] += balls_pool[0][5]
    obj_collis(0)

    star_surf = pygame.transform.rotate(star_surf, 90)
    star_rect = star_surf.get_rect(center=(balls_pool[0][0], balls_pool[0][1]))
    screen.blit(star_surf, star_rect)


def click(event):
    """
    function handles mouse clicks
    1 component: pygame.MOUSEBUTTONDOWN
    :param event: mouse click
    :return: void
    """
    global score, targets_left, have_friend_param
    flag = 0
    mult = event.button
    for i in range(num_of_balls + 1):
        if balls_pool[i][6] > 0 and (event.pos[0] - balls_pool[i][0]) ** 2 + (event.pos[1] - balls_pool[i][1]) ** 2 <= \
                balls_pool[i][2] ** 2:
            if i == 0:
                score += mult * max_rad * (1 + have_friend_param)
                screen.fill(YELLOW)
            else:
                score += mult * (max_rad + min_rad - balls_pool[i][2]) * (1 + have_friend_param)
            balls_pool[i][6] -= 1 * mult
            if balls_pool[i][6] <= 0:
                targets_left -= 1
            flag = 1

    if not flag:
        score -= mult * (max_rad + min_rad) // 10


def draw_text(screen, text, size, x, y):
    """
    function draws text bar with midtop coordinates x,y
    5 components: pygame.Surface, str, int, int, int
    :param screen: surface on which text bar is drawn
    :param text: what is written on text bar
    :param size: font size
    :param x: midtop x coordinate
    :param y: midtop y coordinate
    :return: void
    """
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)
    pygame.display.update()


def frame_quit(num_of_frame, event):
    """
    function processes quits from windows
    2 components: int, pygame.event
    :param num_of_frame: number of window
    :param event: event from pygame.event.get()
    :return: void
    """
    global targets_left
    return (event.type == pygame.QUIT) or \
           (num_of_frame == 1 and targets_left <= 0) or \
           (num_of_frame == 0 and event.type == pygame.KEYDOWN and
            (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN)) or \
           ((num_of_frame == 2 or num_of_frame == 3) and (event.type == pygame.MOUSEBUTTONDOWN or
            (event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN))))


def leaderboard_changing():
    """
    function opens Leaderboard.txt and adds new player
    0 component:
    :return: void
    """
    inp = open('Leaderboard.txt', 'r')
    global leaders, name, score
    leaderboard = inp.readlines()
    if leaderboard != ['\n']:
        for i in leaderboard:
            leaders.append((int(i.split(" ", 1)[0]), i.split(" ", 1)[1]))
    inp.close()
    for i in leaders:
        if score >= i[0]:
            leaders.insert(leaders.index(i), (score, name + "\n"))
            break

    if leaders == [] or score < leaders[-1][0]:
        leaders.append((score, name + "\n"))

    inp = open('Leaderboard.txt', 'w')
    for i in leaders:
        inp.write(str(i[0]) + " " + i[1])
    inp.close()


def before_events(num_of_frame, screen):
    """
    function makes stuff that should have done before events processing
    2 components: int, pygame.screen
    :param num_of_frame: number of window
    :param screen: screen on which all stuff are drawn
    :return: void
    """
    global name, score, leaders, screen_width, screen_height, have_friend_param, balls_pool
    if num_of_frame == 0:
        draw_text(screen, "Enter your name:", screen_height // 10, screen_width // 2, 3 * screen_height // 10)
        draw_text(screen, name, screen_height // 10, screen_width // 2, 4 * screen_height // 10)
    elif num_of_frame == 1:
        rect(screen, WHITE, (screen_width // 10, screen_height // 10, 8 * screen_width // 10, 8 * screen_height // 10), 3)
        draw_balls()
        draw_star()
        draw_text(screen, "Score: " + str(score), screen_height // 10, screen_width // 2, 0)
        keys = pygame.key.get_pressed()
        if have_friend_param:
            balls_pool[0][5] += keys[pygame.K_DOWN] and balls_pool[0][5] < max_vel
            balls_pool[0][5] -= keys[pygame.K_UP] and balls_pool[0][5] > -max_vel
            balls_pool[0][4] += keys[pygame.K_RIGHT] and balls_pool[0][4] < max_vel
            balls_pool[0][4] -= keys[pygame.K_LEFT] and balls_pool[0][4] > -max_vel
    elif num_of_frame == 2:
        draw_text(screen, "Congrats, " + name + "!", screen_height // 10, screen_width // 2, screen_height // 9)
        draw_text(screen, "Your score is " + str(score), screen_height // 10, screen_width // 2, 5 * screen_height // 9)
        if score == -9999998:
            draw_text(screen, "No, fuck you!", screen_height // 10, screen_width // 2, 4 * screen_height // 9)
        elif score == 9999998:
            draw_text(screen, "Cheater, booo", screen_height // 10, screen_width // 2, 4 * screen_height // 9)
    else:
        text_font = screen_height // max(10, len(leaders) + 1)
        draw_text(screen, "Leaders:", screen_height // 10, screen_width // 2, 0)
        for i in range(1, len(leaders) + 1):
            draw_text(screen, (str(leaders[i - 1][0]) + " " + leaders[i - 1][1]).rstrip(), text_font, screen_width // 2,
                      i * screen_height // (len(leaders) + 2) + screen_height // 10)


def events(num_of_frame, event):
    """
    function processes event from keyboard and mouse
    2 components: int, pygame.event
    :param num_of_frame: number of window
    :param event: event from pygame.event.get()
    :return: void
    """
    global name, score, code, balls_pool, targets_left, finished, have_friend_param, FPS
    if num_of_frame == 0:  # first window, enter your name
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            else:
                name += event.unicode
                name = name.rstrip()
    elif num_of_frame == 1:  # second window, the game itself
        if event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
            draw_text(screen, "Score: " + str(score), screen_height // 10, screen_width // 2, 0)
        elif event.type == pygame.KEYDOWN:
            code += event.unicode
            if "i want to win" in code:
                score = 9999998
                finished = True
                leaderboard_changing()
                FPS //= 10
            elif "fuck you" in code:
                score = -9999998
                finished = True
                leaderboard_changing()
                FPS //= 10
            elif "kill star" in code:
                if balls_pool[0][6]:
                    balls_pool[0][6] = 0
                    targets_left -= 1
            elif "i have a friend" in code:
                have_friend_param = True
                balls_pool[0][7] = 0
                balls_pool[0][8] = 0
            print(code)
    # third and last windows do nothing except waiting for closing


clock = pygame.time.Clock()


for i in range(4):  # main body
    finished = False
    while not finished:
        clock.tick(FPS)
        screen.fill(BLACK)
        before_events(i, screen)
        for event in pygame.event.get():
            if frame_quit(i, event):
                finished = True
                if i == 1:
                    leaderboard_changing()
                    FPS //= 10
            events(i, event)


pygame.quit()

