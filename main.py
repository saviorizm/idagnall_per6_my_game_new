# This file was created by Saviorizm 
# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

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
        self.paused = False
        print(self.screen)
    def new(self):
        #re/starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(WIDTH/2,HEIGHT/2,self)
        # draw sprites
        platform1 = Platform(O1WIDTH,O1HEIGHT,randint(0,O1WIDTH),randint(0,WIDTH//3-O1HEIGHT),GREEN)
        platform2 = Platform(O3WIDTH,O3HEIGHT,randint(0,O2WIDTH),randint(WIDTH//3*2,WIDTH-O3HEIGHT),RED)
        platform3 = Platform(200,20, WIDTH/2,randint(WIDTH//3,WIDTH//3*2-O2HEIGHT),WHITE)
        platformbase = Platform(WIDTH,25,0,HEIGHT-25)
        self.all_sprites.add(self.player,platform1,platform2,platform3,platformbase)
        self.platforms.add(platform1,platform2,platform3,platformbase)
        self.run()
        # run method that sets playing to true and enters the game loop
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            # game only updates if it is not paused
            if not self.paused:
                self.update()
    # defines pause function
    def pause(self):
        self.paused = True
        # defines unpause function
    def unpause(self):
        self.paused = False
    # events in the game
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                if event.key == pg.K_p: # pause the game if the 'p' key is pressed
                    self.pause()
                if event.key == pg.K_u: # unpause the game if the 'u' key is pressed
                    self.unpause()
    # method that generates new platforms of a random color, size and x position.
    # the platform is generated at the top of the screen and is scrolled downwards into frame
    def generate_new_platform(self):
        width = randint(50, WIDTH//3 - (PLAYER_WIDTH+ 20))
        height = randint(50, HEIGHT//3 - (PLAYER_HEIGHT+20))
        x = randint(0, WIDTH - width)
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        platform = Platform(width, height, x, 0, color)
        self.all_sprites.add(platform)
        self.platforms.add(platform)
    # method that is made to be put into the update loop
    # checks whether or not hte player has touched the bottom ro the top.
    # it promps them to restart(r) or quit(x)
    def game_over(self):
        if self.player.pos.y >= HEIGHT or self.player.rect.y <= 0:
            self.pause()
            print("game is paused")
            self.draw_text("GAME OVER", 20, WHITE, WIDTH/2, HEIGHT/2)
            self.draw_text("Press 'r' to restart", 20, WHITE, WIDTH/2, HEIGHT/2 + 50)
            self.draw_text("Press 'x' to QUIT", 20, WHITE, WIDTH/2, HEIGHT/2 + 100)
            print("the text is drawn")
            while self.paused:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_r:
                            self.unpause()
                            self.new()
                        if event.key == pg.K_x:
                           pg.quit()
    # update loop
    def update(self):
        self.all_sprites.update() 
        self.game_over()

        # if the player is falling
        if self.player.vel.y > 0:
            # if the player collides with a platofmr
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                # player is standing onthe patform
                self.player.standing = True
                # attmepted variant that disappears after 3 seconds
                # sole purpose of the start platform
                if hits[0].variant == "start_platform":
                    global last_call_time
                    # make starting platofmr disappear after 3 seconds
                    if pg.time.get_ticks() -last_call_time > 3000:
                        print("killing start platform")
                        hits[0].kill()
                    # bouncey platform that bounces the player if they collide with it. 
                    # same bounce height as a regular jump
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    # regular platform collision. If the player collides with the platform, they get tp'd to the top
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
            else:
                self.player.standing = False

        # generate new platform if number of platforms drops to 2
        if len(self.platforms) == 2:
            self.generate_new_platform()
            # draws the sprites and background then refreshes screen
    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    # method that can draw text
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
        pg.display.flip()
    
# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()