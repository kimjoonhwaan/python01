import pygame
import pandas
import time
import sys
import random

from pygame.locals import *

WINDOW_WIDTH = 800  #윈도우 넓이
WINDOW_HEIGTH  = 600  #윈도우 높이

WHITE = (255 ,255 ,255)
GREEN = (0, 50, 0)
ORANGE = (255, 150 ,0)
GRAY = (100,100,100)

GRID_SIZE  =20
GRID_WIDTH = WINDOW_WIDTH /GRID_SIZE
GRID_HEIGTH = WINDOW_HEIGTH  / GRID_SIZE

FPS = 10

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
# main 함수 구문

class Python(object):
    def __init__(self):
        self.create()
        self.color = GREEN

    def create(self):
        self.length = 2
        self.positions = [((WINDOW_WIDTH/ 2), (WINDOW_HEIGTH /2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def control (self, xy):
        if (xy[0] * -1 , xy[1] * -1 ) == self.direction:
            return
        else:
            self.direction = xy

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WINDOW_WIDTH) , (cur[1] + (y * GRID_SIZE)) % WINDOW_HEIGTH )
        if new in self.positions[2:]:
            self.create()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def eat(self):
        self.length += 1

    def draw(self, surface):
        for p in self.positions:
            draw_object(surface, self.color, p)




class Feed(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = ORANGE
        self.create()

    def create(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGTH - 1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position )




def draw_object(surface , color , pos):
    r = pygame.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(surface, color, r)

def check_eat(python, feed):
    if python.positions[0] == feed.position:
        python.eat()
        feed.create()

def show_info(length, speed, surface):
    font = pygame.font.Font(None, 34)
    text = font.render("lengh: "+ str(length) + " Speed: "+str(round(speed, 2)), 1, GRAY )
    pos = text.get_rect()
    pos.centerx= 150
    surface.blit(text, pos)




print("start1")
# if '__name__' == '__main__':
print("start2")
python = Python()
feed = Feed()

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH),0,32)
pygame.display.set_caption("python game")
surface = pygame.Surface(window.get_size())
surface = surface.convert()  #실제 컨버트
surface.fill(WHITE)   #화이트로 지정
clock = pygame.time.Clock()
# pygame.key_set_repeat(1,40)
window.blit(surface, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                python.control(UP)
            elif event.key == K_DOWN:
                python.control(DOWN)
            elif event.key == K_LEFT:
                python.control(LEFT)
            elif event.key == K_RIGHT:
                python.control(RIGHT)
    surface.fill(WHITE)
    python.move()
    check_eat(python, feed)
    speed = (FPS + python.length)/2
    show_info(python.length, speed, surface ) #정보 표시
    python.draw(surface)   # 화면에 표시
    feed.draw(surface)

    window.blit(surface, (0, 0))
    pygame.display.update()
    clock.tick(speed)

