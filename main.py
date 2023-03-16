# file created by saviorizm - Ian Dagnall
# Agenda:
# gIT GITHUB

# import libs
import pygame as pg
from random import randint
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

def get_mouse_now():
    x,y = pg.mouse.get_pos()
    return (x,y)


# init pg and create window
pg.init()

# init sound mixers99
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My first game...")
clock = pg.time.Clock() 

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

player = Player(WIDTH/2,HEIGHT/2)
player_left = Player(player.pos.x - WIDTH, player.pos.y,)
player_right = Player(player.pos.x + WIDTH, player.pos.y,)
player_top = Player(player.pos.x, player.pos.y + HEIGHT)
player_bottom = Player(player.pos.x, player.pos.y - HEIGHT)
all_sprites.add(player, player_left, player_right, player_top, player_bottom)
print(f"enemies is {enemies}")

# creates a for loop that creates 20 mobs
# 
for i in range(0,20):
    # instantiate mobs
    m = Mob(randint(30,90), randint(30, 90), (255,0,0))
    # add enemies to enemies and all_sprites...
    # enemies.add(m)
    all_sprites.add(m)

print(f"enemies is {enemies}")

mob1 = Mob(10,10,RED)
all_sprites.add(mob1)
# enemies.add(mob1)
print(f"enemies is {enemies}")

# game loop

while RUNNING:
    #  keep loop running at the right speed
    clock.tick(FPS)
    ### process input events section of game loop
    for event in pg.event.get():
        # check for window closing
        if event.type == pg.QUIT:
            RUNNING = False
            # dbreak
    # print(get_mouse_now())
    ### update section of game loop (if updates take longer the 1/30th of a second, you will get laaaaag...)
    enemies.update()
    all_sprites.update()



    blocks_hit_list = pg.sprite.spritecollide(player, enemies, True)
    for block in blocks_hit_list:
        # print(enemies)
        pass
    ### draw and render section of game loop
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # double buffering draws frames for entire screen
    pg.display.flip()
    # pg.display.update() -> only updates a portion of the screen
# ends program when loops evaluates to false
pg.quit()