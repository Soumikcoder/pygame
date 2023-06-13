import pygame
from math import sin, cos, pi, atan2


WIDTH = 1200
HEIGHT = 600

class Player(pygame.sprite.Sprite):
    Img = pygame.image.load('resource/player_straight.png')
    Img_right = pygame.image.load('resource/player_right.png')
    Img_left = pygame.image.load('resource/player_left.png')
    Img_gun = pygame.image.load('resource/player_gun.png')
    speed = 2
    rtion = 1

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 128
        self.height = 128
        self.Img_loaded = self.Img
        self.Img_show = self.Img
        self.rect = self.Img_show.get_rect()
        self.gun_show = self.Img_gun
        self.rect_gun = self.gun_show.get_rect()
        self.angle = 0
        self.angle_r = 0
        self.gun_aim = 0
        self.gun_range = 200
        self.target = None
        self.power = 100
        self.die = 500

    def forward(self):
        self.x -= self.speed * sin(self.angle_r)
        self.y -= self.speed * cos(self.angle_r)

    def back(self):
        self.x += self.speed * sin(self.angle_r)
        self.y += self.speed * cos(self.angle_r)

    def rot_left(self):
        self.angle += self.rtion

    def rot_right(self):
        self.angle -= self.rtion

    def with_in_screen(self):

        if self.x < 30:
            self.x = 30
            if self.angle < 90:
                self.angle -= (70-self.angle)/25

            elif self.angle < 180:
                self.angle -= (110-self.angle)/25

            elif self.angle < 270:
                self.angle -= (250-self.angle)/25

            else:
                self.angle -= (290-self.angle)/25

        elif self.x > 1170:
            self.x = 1170
            if self.angle < 90:
                self.angle -= (70-self.angle)/25

            elif self.angle < 180:
                self.angle -= (110-self.angle)/25

            elif self.angle < 270:
                self.angle -= (250-self.angle)/25

            else:
                self.angle -= (290-self.angle)/25

        if self.y < 30:
            self.y = 30
            if self.angle < 90:
                self.angle -= (20-self.angle)/25

            elif self.angle < 180:
                self.angle -= (160-self.angle)/25

            elif self.angle < 270:
                self.angle -= (200-self.angle)/25

            else:
                self.angle -= (340-self.angle)/25

        elif self.y > 570:
            self.y = 570
            if self.angle < 90:
                self.angle -= (20-self.angle)/25

            elif self.angle < 180:
                self.angle -= (160-self.angle)/25

            elif self.angle < 270:
                self.angle -= (200-self.angle)/25

            else:
                self.angle -= (340-self.angle)/25

    def draw(self, zombies, fps,offset,screen):
        self.Img_show = pygame.transform.rotate(self.Img_loaded, self.angle)
        self.rect = self.Img_show.get_rect()
        self.rect.center = (self.x, self.y)
        offset.y=(HEIGHT/2)-self.y
        offset.x=(WIDTH/2)-self.x
        if self.target and (abs(self.target.x-self.x) + abs(self.target.y-self.y)) < self.gun_range*2:
            self.target.die -= self.power/fps
            if self.target.die <= 0:
                self.target = None
                dist = self.gun_range*2
                rough = 0
                for zombie in zombies:
                    if (zombie.x > self.x - self.gun_range and
                        zombie.x < self.x + self.gun_range and
                        zombie.y > self.y - self.gun_range and
                        zombie.y < self.y + self.gun_range and
                            zombie.die > 0):

                        rough = (abs(zombie.x-self.x) + abs(zombie.y-self.y))
                        if dist > rough:
                            dist = rough
                            self.target = zombie
        else:
            dist = self.gun_range*2
            rough = 0
            for zombie in zombies:
                if (zombie.x > self.x - self.gun_range and
                    zombie.x < self.x + self.gun_range and
                    zombie.y > self.y - self.gun_range and
                    zombie.y < self.y + self.gun_range and
                        zombie.die > 0):

                    rough = (abs(zombie.x-self.x) + abs(zombie.y-self.y))
                    if dist > rough:
                        dist = rough
                        self.target = zombie
        if self.target:
            xdist = self.target.x - self.x
            ydist = self.target.y - self.y

            self.gun_aim = atan2(xdist, ydist) * 180 / pi + 180
            self.gun_aim %= 360
            self.gun_show = pygame.transform.rotate(self.Img_gun, self.gun_aim)
        else:
            self.gun_show = pygame.transform.rotate(self.Img_gun, self.angle)

        self.rect_gun = self.gun_show.get_rect()
        self.rect_gun.center = self.rect.center

        rectoff=[self.rect.x+offset.x,self.rect.y+offset.y]
        rectoff_gun=[self.rect_gun.x+offset.x,self.rect_gun.y+offset.y]
        screen.blit(self.Img_show,rectoff)
        screen.blit(self.gun_show,rectoff_gun)

        if self.die <= 0:
            self.kill()