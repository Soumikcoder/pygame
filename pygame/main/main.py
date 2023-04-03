import pygame
import random
from math import sin, cos, pi, atan2
import os
from os import listdir
from os.path import isfile, join

#
pygame.init()

# screen
WIDTH = 1200
HEIGHT = 600
fps = 60
running = True
clock = pygame.time.Clock()

# Caption and Icon
pygame.display.set_caption("Invader")
icon = pygame.image.load('pygame/resource/logo.png')
pygame.display.set_icon(icon)


# player
class Player():
    Img = pygame.image.load('pygame/resource/player_straight.png')
    Img_right = pygame.image.load('pygame/resource/player_right.png')
    Img_left = pygame.image.load('pygame/resource/player_left.png')
    Img_gun = pygame.image.load('pygame/resource/player_gun.png')
    speed = 2
    rtion = 1

    def __init__(self, x, y):
        global Img
        self.x = x
        self.y = y
        self.Img_loaded = self.Img
        self.angle = 0
        self.angle_r = 0
        self.gun_aim = 0
        
    def image(self):
        self.Img_loaded = self.Img

    def image_l(self):
        self.Img_loaded = self.Img_left

    def image_r(self):
        self.Img_loaded = self.Img_right

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

    def draw(self):
        Img_show = pygame.transform.rotate(self.Img_loaded, self.angle)
        rect = Img_show.get_rect()
        rect.center = (self.x, self.y)

        
        xdist = enemy_cords[0] - rect.centerx
        ydist = enemy_cords[1] - rect.centery

        self.gun_aim = atan2(xdist, ydist) * 180 / pi + 180
        self.gun_aim %= 360

        gun_show = pygame.transform.rotate(self.Img_gun, self.gun_aim)
        rect_gun = gun_show.get_rect()
        rect_gun.center = rect.center

        screen.blit(Img_show, rect)
        screen.blit(gun_show, rect_gun)

enemy_cords = (0, 0)
class Zombie():

    def __init__(self):
        pass

cng_player_img = -1;
def handle_move(player):
    global cng_player_img
    keys = pygame.key.get_pressed()

    # player position
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.rot_right()
        else:
            player.rot_left()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.rot_left()
        else:
            player.rot_right()

    player.angle %= 360
    player.angle_r = (player.angle * pi) / 180

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.forward()

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.back()

    player.with_in_screen()

    # player image
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if cng_player_img != 0:
            cng_player_img = 0
            player.image_l()

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if cng_player_img != 1:
            cng_player_img = 1
            player.image_r()

    elif keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if cng_player_img != 2:
            cng_player_img = 2
            player.image()


grass = pygame.image.load('pygame/resource/grass.jpg')
def draw(player):
    # back ground
    for i in range(0, WIDTH, 128):
        for j in range(0, HEIGHT, 128):
            screen.blit(grass, (i, j))
    # player 
    player.draw()

    pygame.display.update()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = Player(WIDTH/2, HEIGHT/2)

while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handle_move(player)

    draw(player)