
import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import randint
from time import sleep
import os

# variables that need to be predfined
vec = pg.math.Vector2
game_over = False
last_call_time = 0
# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
print(img_folder)


# player class
class Player(Sprite):
    def __init__(self,X,Y,game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(X,Y)
        self.start = (X,Y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.fragment = vec((self.rect.x + PLAYER_WIDTH - WIDTH), (self.pos.y + HEIGHT) - HEIGHT)
    # method that tracks the inputs from the player
    def input(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.acc.x = -PLAYER_ACC
            # print("key a is pressed")
        if keystate[pg.K_d]:
            self.acc.x = PLAYER_ACC
            # print("key d is pressed")
        if keystate[pg.K_w]:
            self.jump()
        if keystate[pg.K_c]:
            self.pos = self.start
            # keeps he player character in the screen
    def inbounds(self):
        if self.rect.x >= WIDTH - PLAYER_WIDTH:
            # self.vel.x = -1
            # print("i am off the right side")
            self.vel.x = 0
            self.pos.x = WIDTH - PLAYER_WIDTH/2
        if self.rect.x <= 0:
            # self.vel.x = 1
            # print("i am off the left")
            self.vel.x = 0
            self.pos.x = PLAYER_WIDTH/2
        if self.rect.y <= 0:
             print("I am off the top")
             self.vel.y = 0
             self.pos.y = PLAYER_HEIGHT/2
        if self.rect.y > HEIGHT - PLAYER_HEIGHT:
            # print("I am off the bottom")
            self.vel.y = 0
            self.pos.y = HEIGHT
        
    def wait(self,time):
        ms_time = time *1000
        CURRENT_TIME = pg.time.get_ticks()
        # if CURRENT_TIME 
    # jump method for the player
    def jump(self):
        keystate = pg.key.get_pressed()
        global last_call_time

        if keystate[pg.K_w]:
            # checks whether or not the player has jumped inthe last 3 seconds, if not, they can jump
            if pg.time.get_ticks() - last_call_time > PLAYER_JUMP_COOLDOWN:
                last_call_time = pg.time.get_ticks()
                self.vel.y = -PLAYER_JUMP
                self.rect.x += 1
                hits = pg.sprite.spritecollide(self, self.game.platforms, False)
                self.rect.x -= 1
                if not hits:
                    print(f"last jump call time is {last_call_time}")

    # player sticks to wall when a key is pressed
    def wall_stick(self):
        keystate = pg.key.get_pressed()
        self.wall_stick_time = None
        # left side
        if self.rect.x <= 0:
            if keystate[pg.K_a]:
                self.vel.y = -PLAYER_GRAV
                print("sticking to wall")
                # checks if player has been on the wall for more than 1.7 secs
                if self.wall_stick_time is None:
                    self.wall_stick_time = pg.time.get_ticks()
                elif pg.time.get_ticks() - self.wall_stick_time > 1700:
                    print("falling off the wall")
                    # kicks them off the wall
                    keystate[pg.K_a] = 0
                    self.wall_stick_time = None
                # right side
        if self.rect.x >= WIDTH - PLAYER_WIDTH:
            if keystate[pg.K_d]:
                self.vel.y = -PLAYER_GRAV
                print("sticking to wall")
                if self.wall_stick_time is None:
                    self.wall_stick_time = pg.time.get_ticks()
                elif pg.time.get_ticks() - self.wall_stick_time > 1700:
                    print("falling off the wall")
                    keystate[pg.K_a] = 0
                    self.wall_stick_time = None
    # update loop
    # handles gravity, other physics and character handling
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x = self.vel.x * PLAYER_FRICTION
        self.input()
        self.inbounds()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        self.wall_stick()


#  Bomb class
class Bomb(Sprite):
    def __init__(self,xpos,ypos):
        Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(game_folder,img_folder, 'game_bomb.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.pos = vec(600,600)
        self.vel = vec(randint(1,5),randint(1,5))
        self.acc = vec(1,1)
        self.cofric = 0.01
    # scroll the platforms downwards
    def scrolling(self):
        self.rect.y = self.rect.y + 6
        if self.rect.y > HEIGHT:
            self.kill()
    # update loop handles scrolling
    def update(self):
        self.scrolling()

# platform class
class Platform(Sprite):
    def __init__(self, width, height, xpos, ypos, color="WHITE", variant="normal",scroll = True):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width, self.height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.variant = variant
        self.scroll = scroll
    # method that moves the platforms downwards everytime the update loop is looped through
    def scrolling(self):
        # scroll the platforms downwards
        if self.scroll:
            self.rect.y = self.rect.y + 1
            if self.rect.y > HEIGHT:
                # kills the platforms after they float off the screen
                self.kill()  
    # update loop method
    def update(self):
        self.scrolling()