
import pygame as pg

from pygame.sprite import Sprite

from settings import *

from random import randint
from time import sleep

vec = pg.math.Vector2
wrap_around = False
color_state = False


# player class

class Player(Sprite):
    def __init__(self,X,Y):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(X,Y)
        # self.color = color
        self.start = (X,Y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
        self.fragment = vec((self.rect.x + PLAYER_WIDTH - WIDTH), (self.pos.y + HEIGHT) - HEIGHT)
    
    def input(self):
        keystate = pg.key.get_pressed()

        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
            
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
            
        if keystate[pg.K_w]:
            self.acc.y = -PLAYER_ACC
            
        if keystate[pg.K_s]:
            self.acc.y = PLAYER_ACC
            
        if keystate[pg.K_c]:
            self.pos = self.start

        if keystate[pg.K_r]:
            global color_state
            color_state = not color_state

    def inbounds(self):
        global wrap_around

        if self.rect.x > self.start[0] + WIDTH:
            print("resetting from right")
            self.pos.x = self.start[0]

        if self.rect.x < self.start[0] - WIDTH:
            print("resetting from left")
            self.pos.x = self.start[0]

        if self.rect.y > self.start[1] + HEIGHT:
            print("resetting from bottom")
            self.pos.y = self.start[1]

        if self.rect.y < self.start[1] - HEIGHT:
            print('resetting from top')
            self.pos.y = self.start[1]
        
    def wait(self,time):
        ms_time = time *1000
        CURRENT_TIME = pg.time.get_ticks()
        # if CURRENT_TIME 

    def color_change(self):
        while color_state:
            CURRENT_TIME = pg.time.get_ticks()
            print(CURRENT_TIME)
            index = 0
            self.image.fill(GREEN)
            if CURRENT_TIME > 3000:
                self.image.fill(COLOR_LIST[index])

                # index +=1
            # self.current_color = COLOR_LIST % len(COLOR_LIST)
        else:
            self.image.fill(BLACK)

    def update(self):
        self.inbounds()
        self.color_change()
        self.acc = self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos
           

#  mob class
class Mob(Sprite):
    def __init__(self,width,height, color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(1,1)
        self.cofric = 0.01
    ...
    def inbounds(self):
        if self.rect.x > WIDTH - PLAYER_WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.x < 0 + PLAYER_WIDTH:
            self.vel.x *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y < 0 - PLAYER_HEIGHT:
            self.vel.y *= -1
            # self.acc = self.vel * -self.cofric
        if self.rect.y > HEIGHT - PLAYER_HEIGHT:
            self.vel.y *= -1
    #         # self.acc = self.vel * -self.cofric

    # def inbounds(self):
    #     if self.rect.x > WIDTH:
    #         self.pos.x = 0

    #     if self.rect.x < 0:
    #         self.pos.x = WIDTH

    #     if self.rect.y < 0:
    #         self.pos.y = HEIGHT

    #     if self.rect.y > HEIGHT:
    #         self.pos.y = 0


    def update(self):
        self.inbounds()
        # self.pos.x += self.vel.x
        # self.pos.y += self.vel.y
        self.pos += self.vel
        self.rect.center = self.pos
