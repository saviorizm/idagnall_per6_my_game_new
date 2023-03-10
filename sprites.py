
import pygame as pg

from pygame.sprite import Sprite

from settings import *

from random import randint

vec = pg.math.Vector2
wrap_around = False

# Player wrap class

# class Player_Wrap(Sprite):
    # def __init__(self):
    #     if (self.rect.x + PLAYER_WIDTH) > WIDTH:
    #         print(" I am off the right")
    #         self_remainder = int((self.rect.x + PLAYER_WIDTH) - WIDTH)
    #         Sprite.__init__(self)
    #         self.image = pg.Surface((self_remainder,50))
    #         self.image.fill(BLACK)
    #         self.rect = self.image.get_rect()
    #         self.rect.center = (WIDTH/2, HEIGHT/2)
    #         self.pos = vec(WIDTH/2, HEIGHT/2)

    #     if self.rect.x < 0:
    #         print("I am off the left")
    #         self_remainder = int((self.rect.x + PLAYER_WIDTH) - WIDTH)
    #         print(" I am off the right")
    #         self_remainder = int((self.rect.x + PLAYER_WIDTH) - WIDTH)
    #         Sprite.__init__(self)
    #         self.image = pg.Surface((self_remainder,50))
    #         self.image.fill(BLACK)
    #         self.rect = self.image.get_rect()
    #         self.rect.center = (WIDTH/2, HEIGHT/2)
    #         self.pos = vec(WIDTH/2, HEIGHT/2)

    #     if self.rect.y + PLAYER_HEIGHT > HEIGHT:
    #         print("I am off the bottom of the screen")
    #         self_remainder = int((self.rect.y + PLAYER_HEIGHT) - HEIGHT)

    #     if (self.rect.y) < 0:
    #         print("I am off the top of the screen")
    #         self_remainder = int((self.rect.y + PLAYER_HEIGHT) - HEIGHT)



# player class

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2,HEIGHT/2)
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
            self.pos = CENTER


# # if wraparound the border - 
#   # partial display of player on other side of screen
#   def wrap(self):
#       self.image_2.fill(BLACK)
#       self.rect = self.image.get_rect()
#       if self.rect.x > WIDTH:
#           print(" I am off the right side of the screen")
#           # self.rect.x = 0

              
#       if self.rect.x < -PLAYER_WIDTH:
#           print("I am off the left side of the screen")
#           # self.rect.x = WIDTH
#           self.image_2.pos

#       if self.rect.y > HEIGHT:
#           print("I am off the bottom of the screen")
#           # self.pos.y = 0

#       if self.rect.y < -PLAYER_HEIGHT:
#           print("I am off the top of the screen")
#           # self.pos.y = HEIGHT


    # def wrap_around_right(self_wrap):
    #         self_remainder = int((self_wrap.rect.x + PLAYER_WIDTH) - WIDTH)
    #         # self.rect.x = 0
    #         print(f"x posItions is {self_wrap.rect.x}")
    #         Sprite.__init__(self_wrap.wrap)
    #         self_wrap.image_wrap = pg.Surface((50, 50))
    #         self_wrap.pos.x = (self_wrap.rect.x + PLAYER_WIDTH) - WIDTH
    #         print(self_wrap.image_wrap)
    #         self_wrap.image_wrap.fill(BLACK)

    # checks to see if user is in the display area
    def inbounds(self):
        global wrap_around

        # if (self.rect.x + PLAYER_WIDTH) > WIDTH:
        #     print(" I am off the right")
        #     self_remainder = int((self.rect.x + PLAYER_WIDTH) % WIDTH)
        #     self.rect.x = -self_remainder
        #     print(f"self remainder is {self_remainder}")
        #     # Sprite.__init__(self)
        #     wrap_around = True

        if self.rect.x < 0:
            print("I am off the left")
            self_remainder = int(PLAYER_WIDTH % ((self.rect.x + PLAYER_WIDTH) % WIDTH))
            print(f"self remainder is {self_remainder}")
            self.rect.x = WIDTH - self_remainder
            print(f"x posItions is {self.rect.x}")

        if self.rect.y + PLAYER_HEIGHT > HEIGHT:
            print("I am off the bottom of the screen")
            self_remainder = int((self.rect.y + PLAYER_HEIGHT) % HEIGHT)
            print(f"self remainder is {self_remainder}")
            self.rect.y = -self_remainder
            print(f"y posItions is {self.rect.y}")

        # if (self.rect.y) < 0:
        #     print("I am off the top of the screen")
        #     self_remainder = int(PLAYER_HEIGHT % ((self.rect.y + PLAYER_HEIGHT) % HEIGHT))
        #     print(f"self remainder is {self_remainder}")
        #     self.rect.y = HEIGHT + self_remainder
        #     print(f"y posItions is {self.rect.y}")

        # ///////////////////////////////////////////////////////
        
        # if wrap_around:
        #     Sprite.__init__(self)
        #     self.image_wrap = pg.Surface() 
        #     print(self.image_wrap)
        #     self.image_wrap.fill(BLACK)


        # if wrap_around:
        #     Sprite.__init__(self)
        #     self.image_wrap = pg.Surface((50,50))
        #     self.image_wrap.fill(BLACK)
        #     self.pos.y = (HEIGHT - (self.pos.y + PLAYER_HEIGHT))
            

            # self.rect.x %= WIDTH
            # self.pos.y %= HEIGHT

            # self.image[0] %= WIDTH
            # self.image[1] %= HEIGHT

            # Sprite.__init__(self)
            # self.image = pg.Surface((50,50))
            # self.image.fill(BLACK)


    def update(self):
        self.inbounds()
        self.acc = self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

class Partial(Sprite):
    def __init__(self, Player):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(801,801)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        if Player.rect.x > 750 < 850:
            self.pos = vec(WIDTH/2, HEIGHT/2)
           
       

#  mob class
# //////////////////////////////////////////////////////////

class Mob(Sprite):
    def __init__(self,width,height,color):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pg.Surface((self.width,self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
    # ...
    def inbounds(self):
        if self.rect.x > WIDTH:
            print(" I am off the right side of the screen")
            self.rect.x = 0

        if self.rect.x < -75:
            print("I am off the left side of the screen")
            self.rect.x = WIDTH

        if self.rect.y > HEIGHT:
            print("I am off the bottom of the screen")
            self.pos.y = 0

        if self.rect.y < -75:
            print("I am off the top of the screen")
            self.pos.y = HEIGHT
        
    def behavior(self):
        self.x, self.y = 0, 0
        print(self.vel)
        self.rect.x = randint(-1,1)
        self.rect.y = randint(-1,1)

    def update(self):
        self.inbounds()
        self.acc = self.vel * -0.2
        self.vel += self.acc
        # self.behavior()
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos