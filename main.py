# file created by saviorizm - Ian Dagnall

# import libs
import pygame as pg
from random import randint
import os
# import settings 
from settings import *
from sprites import *

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprites file

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        #re/starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()

        self.player = Player(WIDTH/2,HEIGHT/2,self)
        platform1 = Platform(O1WIDTH,O1HEIGHT,randint(0,O1WIDTH),randint(0,WIDTH//3-O1HEIGHT),GREEN)

        platform2 = Platform(O2WIDTH,O2HEIGHT,randint(0,O2WIDTH),randint(WIDTH//3,WIDTH//3*2-O2HEIGHT),RED)

        platform3 = Platform(O3WIDTH,O3HEIGHT,randint(0,O3WIDTH),randint(WIDTH//3*2,WIDTH-O3HEIGHT),GREEN)

        platformbase = Platform(WIDTH,25,0,HEIGHT-25)

        self.all_sprites.add(self.player,platform1,platform2,platform3,platformbase)
        self.platforms.add(platform1,platform2,platform3,platformbase)
        # self.all_sprites.add(self.player)
        # for plat in PLATFORM_LIST:
        #     p = Platform(*plat)
        #     self.all_sprites.add(p)a
        #     platforms.add(p)

        for i in range(0,10):
            m = Mob(20,20,(0,255,0))
            self.all_sprites.add(m)
            self.enemies.add(m)

        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.self.jump()
    def collision(self):
        if self.player.vel.y > 0:
            collided_platforms = pg.sprite.spritecollide(self.player, self.platforms, False)

        for platform in collided_platforms:
            keystate = pg.key.get_pressed()
            # Calculate the penetration depth in x and y directions
            delta_x_left = self.player.rect.right - platform.rect.left
            delta_x_right = platform.rect.right - self.player.rect.left
            delta_y_top = self.player.rect.bottom - platform.rect.top
            delta_y_bottom = platform.rect.bottom - self.player.rect.top
            # Check for the smallest penetration depth
            min_delta_x = min(abs(delta_x_left), abs(delta_x_right))
            min_delta_y = min(abs(delta_y_top), abs(delta_y_bottom))
            if min_delta_x < min_delta_y:
                Player collides on the left side of the obstacle
                if abs(delta_x_left) == min_delta_x:
                    self.player.vel.x = 0
                    self.player.pos.x = platform.rect.left - PLAYER_WIDTH/2
                    if keystate[pg.K_d]:
                        self.player.vel.y += -PLAYER_GRAV*10
                    if keystate[pg.K_w]:
                        self.jump()
                # Player collides on tahe right side of the obstacle
                # else:
                    self.player.vel.x = 0
                    self.player.pos.x = platform.rect.right + PLAYER_WIDTH/2
                    print("top code")
                    if keystate[pg.K_a]:
                        self.player.vel.y += -PLAYER_GRAV*10
                        print("bottom")
                    # if keystate[pg.K_w]:
                    #     self.player.jump(-50)
            else:
                # Player collides on the top side of the obstacle
                if abs(delta_y_top) == min_delta_y:
                    self.player.vel.y = 0
                    self.player.pos.y = platform.rect.top - PLAYER_WIDTH/2
                # Player collides on the bottom side of the obstacle
                else:
                    self.player.vel.y = 0
                    self.player.pos.y = platform.rect.bottom + PLAYER_WIDTH/2

    def update(self):
        self.all_sprites.update()
        self.collision()
    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        # is this a method or a function?
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()
    

pg.quit()