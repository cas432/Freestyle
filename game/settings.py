import random
import pygame
from pygame import *
from os import path

img_dir = path.join(path.dirname(__file__), 'images')

#game options/settimgs
TITLE = 'Champions are Coming'
WIDTH = 960
HEIGHT = 720
FPS = 60

# Player Properties

PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = .7
PLAYER_JUMP = 18
PLAYER_HEALTH = 100
# Arrows
ARROW_SPEED = 13
ARROW_DAMAGE = 1
SHOT_TIME = 400

#Fireball
FIREBALL_SPEED = 5
FIREBALL_DAMAGE = 100

# starting platforms

PLATFORM_LIST = [(0, HEIGHT- 5, WIDTH, 10), 
                (WIDTH - 620, HEIGHT *3/4, 100, 5),
                (WIDTH - 120, HEIGHT - 360, 100, 5),
                (WIDTH - 155, HEIGHT - 540, 75, 5),
                (WIDTH - random.randint(475,500), HEIGHT - 300, 75, 5),
                (WIDTH/4, HEIGHT - random.randint(475,500), 200, 5)]

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LBROWN = (181, 101, 29)
DBROWN = (101, 67, 33)

# screens
img_dir = path.join(path.dirname(__file__), 'images')
