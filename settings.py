WIDTH = 1000
HEIGHT = 900    

CENTER = (WIDTH/2, HEIGHT/2)

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

PLAYER_ACC = 1
PLAYER_FRICTION = -0.1
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

MOB_ACC = 0
MOB_FRICTION = -0.2

BLACK = (0,0,0)

RED = (255, 50, 50)
ORANGE = (255, 165, 0)
YELLOW = (255,255,0)
GREEN = (0, 255, 50)
BLUE = (50,50,255)
PURPLE = (230,0,250)
WHITE = (255,255,255)

COLOR_LIST = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

COLOR_STATE = False
SCORE = 0

PAUSED = False


FPS = 61
RUNNING = True
# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (200,200,200), "bouncey"),
                 (125, HEIGHT - 350, 100, 5, (200,200,200), "disappearing "),
                 (350, 200, 100, 20, (200,200,200), "normal"),
                 (175, 100, 50, 20, (200,200,200), "normal")]