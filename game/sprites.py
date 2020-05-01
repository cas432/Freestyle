import pygame as pg
from settings import *
from os import path

vec = pg.math.Vector2
img_dir = path.join(path.dirname(__file__), 'images') #variable for image filepath


class Player(pg.sprite.Sprite):
"""
Creates the Player class to provide a template for players in the game.
"""
    def __init__(self, game, img):
    """
    Initializes (sets up) the player class.

    Parameters: 
    
        self (self):  keyword we can access the attributes and methods of the class in python 
    
        game #HOW TO EXPLAIN THIS???????

        img (.png file): png file that has an image for the player
    
    Source: YouTube Videos KidsCanCode provided information needed for initial setup of code, though code was altered to tailor to project

    Source Link: https://www.youtube.com/watch?v=uWvb3QzA48c
    """
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32,32))
        self.image = pg.image.load(path.join(img_dir, img)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = PLAYER_HEALTH
        self.radius = 15 
    
    def jump(self):
    """
    Defines rules for the player action of jumping.

    Parameters: 
    
        self (self):  keyword we can access the attributes and methods of the class in python 
    
    Source: YouTube Videos KidsCanCode provided information needed for initial setup of code, though code was altered to tailor to project

    Source Link: https://www.youtube.com/watch?v=uWvb3QzA48c
    """ 
        self.rect.y += 1

        hits = pg.sprite.spritecollide(self,self.game.platforms, False)
        self.rect.y -= 1
        
        if hits:
            self.vel.y = -PLAYER_JUMP
    
        
    
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC

        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC


        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # Nothing passed the sides
        self.rect.midbottom = self.pos

        if self.pos.x > WIDTH:
            self.pos.x  = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0

class Platform(pg.sprite.Sprite):
"""
Creates the Platform class to provide a template for platforms in the game.
"""
    def __init__(self, x, y, w, h):
    """
    Initializes (sets up) the platform class.

    Parameters: 
    
        self (self):  keyword we can access the attributes and methods of the class in python 
    
        x (int): x coordinate of the platform on the screen (changing the coordinate moves the pltform horizontally)

        y (int): y coordinate of the platform on the screen (changing the coordinate moves the pltform vertically)

        w (int): length of the platform (changing the coordinate makes the platform longer)

        h (int): height of the platform (changing the coordinate makes the platform taller)

    Source: YouTube Videos KidsCanCode provided information needed for initial setup of code, though code was altered to tailor to project

    Source Link: https://www.youtube.com/watch?v=uWvb3QzA48c
    """     
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(pg.sprite.Sprite):
"""
Creates the Enemy class to provide a template for enemies in the game.
"""
    def __init__(self,x,y, img):
    """
    Initializes (sets up) the enemy class.

    Parameters: 
    
        self (self):  keyword we can access the attributes and methods of the class in python 
    
        x (int): x coordinate of the platform on the screen (changing the coordinate moves the pltform horizontally)

        y (int): y coordinate of the platform on the screen (changing the coordinate moves the pltform vertically)

        img (.png file): png file that has an image for the enemy        
    """ 
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(img_dir, img)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 10
        
        
    def update(self):
        if self.health < 0:
            self.kill()
    

class Arrow(pg.sprite.Sprite):
"""
Creates the Arrow class to provide a template for arrows (player weapons) in the game.
"""
    def __init__(self, x, y, img):
    """
    Initializes (sets up) the arrow class.

    Parameters: 
    
        self (self):  keyword we can access the attributes and methods of the class in python 
    
        x (int): 

        y (int): 

        img (.png file): png file that has an image for the enemy        

    Source: YouTube Videos KidsCanCode provided information needed for initial setup of code, though code was altered to tailor to project

    Source Link: https://www.youtube.com/watch?v=uWvb3QzA48c
    """  
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(img_dir, img)).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.pos = vec(x, y)
        self.vel = vec(ARROW_SPEED,-3)
        self.acc = vec(0,0)
    
    def update(self):
        
        # equations of motion
        self.acc = vec(0, PLAYER_GRAV)
        self.acc.x += self.vel.x
        self.vel.y += self.acc.y
        self.pos += self.vel + 0.5 * self.acc
        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y - 32

        if self.rect.x > WIDTH + 100:
            self.kill()
        if self.rect.y > HEIGHT + 100:
            self.kill()


       
class Fireball(pg.sprite.Sprite):
"""
Creates the Fireball class to provide a template for fireballs (enemy weapons) in the game.
"""
    def __init__(self, x, y, img):
    """
    Initializes (sets up) the fireball class.

    Parameters: 
    
        self (self):  keyword we can access the attributes and methods of the class in python 
    
        x (int): 

        y (int): 

        img (.png file): png file that has an image for the enemy        

    Source: YouTube Videos KidsCanCode provided information needed for initial setup of code, though code was altered to tailor to project

    Source Link: https://www.youtube.com/watch?v=uWvb3QzA48c
    """ 
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(path.join(img_dir, img)).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.pos = vec(x, y)
        self.vel = vec(-FIREBALL_SPEED,0)
        self.acc = vec(0,0)
    
    def update(self):
        
        # equations of motion
        self.acc = vec(0, 0.008)
        self.acc.x += self.vel.x
        self.vel.y += self.acc.y
        self.pos += self.vel + 0.5 * self.acc
        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y - 64
        
               
        
    


        
        

             