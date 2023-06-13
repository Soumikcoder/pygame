import pygame
from random import randint
from math import sin, cos, pi, atan2
from Player import *
from zombie import *
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
icon = pygame.image.load('resource/logo.png')
pygame.display.set_icon(icon)

cng_player_img = 2
ground = pygame.image.load('resource/ground.jpg')

# groups
zombies = pygame.sprite.Group()
players = pygame.sprite.Group()

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
level = 0
offset=pygame.math.Vector2()



class Wall(pygame.sprite.Sprite):
    Img = pygame.image.load('resource/wall.jpg')


    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.Img_loaded = self.Img
        self.rect = self.Img_loaded.get_rect()

    def draw(self):
        self.rect = self.Img_loaded.get_rect()
        self.rect.center = (self.x, self.y)
        rectoff=[self.rect.x+offset.x,self.rect.y+offset.y]
        screen.blit(self.Img_loaded,rectoff)


def handle_input(player):
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

    # player.with_in_screen()

    # player image
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if cng_player_img != 0:
            cng_player_img = 0
            player.Img_loaded = player.Img_left

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if cng_player_img != 1:
            cng_player_img = 1
            player.Img_loaded = player.Img_right

    elif keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if cng_player_img != 2:
            cng_player_img = 2
            player.Img_loaded = player.Img


def start():
    players.add(Player(WIDTH/2, HEIGHT/2))


def spawn():
    global level
    level += 1
    for i in range(25):
        zombies.add(Zombie(level))


def kill():
    for zombie in zombies:
        zombie.die = 0


walls = []
for i in range(3000):
    walls.append(Wall(randint(-WIDTH*10,WIDTH*10),randint(-HEIGHT*10, HEIGHT*10)))

while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            spawn()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
            kill()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            if not players:
                start()

    for player in players:
        handle_input(player)

        for zombie in zombies:
            if zombie.die > 0:
                zombie.move(player, fps)

    # background
    for i in range(-128+int(offset.x)%128, int(WIDTH+int(offset.x)%128), 128):
        for j in range(-128+int(offset.y)%128,int( HEIGHT+int(offset.y)%128), 128):
            rectoff=[i,j]
            screen.blit(ground, rectoff)
    # walls
    for wall in walls:
        wall.draw()

    # player
    for player in players:
        player.draw(zombies, fps)

    # zombies
    for zombie in zombies:
        zombie.draw()

    pygame.display.update()

# p to create player
# z to creat zombies
# k to kill all zombie