import pygame
from random import randint
from math import sin, cos, pi, atan2

WIDTH = 1200
HEIGHT = 600


class Zombie(pygame.sprite.Sprite):
    Img = pygame.image.load('resource/zombie.png')
    Img_flip = pygame.image.load('resource/zombie_flip.png')
    Img_die = pygame.image.load('resource/die.png')
    Img_die_flip = pygame.image.load('resource/die_flip.png')
    speed = 1
    rtion = 1

    def __init__(self, level):
        super().__init__()
        if randint(0, 1):
            self.x = randint(WIDTH-100, WIDTH+100) % WIDTH
            self.y = randint(0, HEIGHT)
        else:
            self.x = randint(0, WIDTH)
            self.y = randint(HEIGHT-100, HEIGHT+100) % HEIGHT
        self.width = 30
        self.height = 42
        self.Img_loaded = self.Img
        self.rect = self.Img_loaded.get_rect()
        self.range = 100
        self.aim = randint(0, 7)
        self.change_aim = randint(1, 10)
        self.die = 25*level
        self.power = 2*level
        self.corps = 60
        self.attack = 1

    def move(self, player, fps):
        xdist = player.x - self.x
        ydist = player.y - self.y

        if abs(xdist) + abs(ydist) < self.range*2:
            self.aim = atan2(xdist, ydist) + pi
            if abs(xdist) + abs(ydist) < 40:
                self.attack = 0
            else:
                self.attack = 1
        else:
            self.attack = 1
            self.change_aim -= 1/fps
            if self.change_aim < 0:
                self.change_aim = randint(1, 10)
                self.aim = randint(0, 7)

            if self.x < 0:
                self.x = 0
                self.aim = randint(4, 6)
            elif self.x > WIDTH:
                self.x = WIDTH
                self.aim = randint(1, 3)
            if self.y < 0:
                self.y = 0
                self.aim = randint(2, 5)
            elif self.y > HEIGHT:
                self.y = HEIGHT
                self.aim = randint(-2, 5)
        if self.attack:
            self.x -= self.speed * sin(self.aim)
            self.y -= self.speed * cos(self.aim)
        else:
            player.die -= self.power/fps

    def draw(self,offset,screen):

        if self.aim > 0 and self.aim < pi:
            if self.die <= 0:
                self.Img_loaded = self.Img_die_flip
            else:
                self.Img_loaded = self.Img_flip
        else:
            if self.die <= 0:
                self.Img_loaded = self.Img_die
            else:
                self.Img_loaded = self.Img

        self.rect = self.Img_loaded.get_rect()
        self.rect.center = (self.x, self.y)

        rectoff=[self.rect.x+offset.x,self.rect.y+offset.y]
        screen.blit(self.Img_loaded,rectoff)

        if self.die <= 0:
            self.corps -= 1
            if self.corps < 0:
                self.kill()

