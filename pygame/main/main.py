import pygame
import random
from math import sin, cos, pi, atan2

#
pygame.init()

# screen
width = 1200
height = 600

# Caption and Icon
pygame.display.set_caption("Invader")
icon = pygame.image.load('pygame/resource/logo.png')
pygame.display.set_icon(icon)

# player
playerImg_straight = pygame.image.load('pygame/resource/player_straight.png')
playerImg_right = pygame.image.load('pygame/resource/player_right.png')
playerImg_left = pygame.image.load('pygame/resource/player_left.png')
playerImg0 = playerImg_straight
rect0_player = playerImg0.get_rect()
playerX = width/2
playerY = height/2
rect0_player.center = (playerX, playerY)
angle_player = 0
angle_player_r = 0

playerImg_gun0 = pygame.image.load('pygame/resource/player_gun.png')
angle_gun = 0

clock = pygame.time.Clock()

enemy_cords = (0, 0)


def player():

    global playerX
    global playerY
    global angle_player
    global angle_gun
    angle_gun += 1

    rect0_player.center = (playerX, playerY)
    playerImg1 = pygame.transform.rotate(playerImg0, angle_player)
    rect1_player = playerImg1.get_rect()
    rect1_player.center = rect0_player.center

    xdist = enemy_cords[0] - rect0_player.centerx
    ydist = enemy_cords[1] - rect0_player.centery

    angle_gun = atan2(xdist, ydist) * 180 / pi + 180
    angle_gun %= 360

    playerImg_gun1 = pygame.transform.rotate(playerImg_gun0, angle_gun)
    rect1_gun = playerImg_gun1.get_rect()
    rect1_gun.center = rect0_player.center

    screen.blit(playerImg1, rect1_player)
    screen.blit(playerImg_gun1, rect1_gun)


# seed generation
seed = random.randint(0, 9)
chunk_coords = [0, 0]

# create screen
screen = pygame.display.set_mode((width, height))

running = True
# update_chunk(coords)
while running:
    clock.tick(120)

    # RGB = Red, Green, Blue
    screen.fill((40, 40, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # player position
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            angle_player -= .5
        else:
            angle_player += .5

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            angle_player += .5
        else:
            angle_player -= .5

    angle_player %= 360
    angle_player_r = (angle_player * pi) / 180

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        playerY -= 1.8 * cos(angle_player_r)
        playerX -= 1.8 * sin(angle_player_r)

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        playerY += 1.8 * cos(angle_player_r)
        playerX += 1.8 * sin(angle_player_r)

    # player image
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        playerImg0 = playerImg_left

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        playerImg0 = playerImg_right

    elif keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]:
        playerImg0 = playerImg_straight

    if playerX < 70:
        playerX = 70
        if angle_player < 70:
            angle_player -= (70-angle_player)/50
        elif angle_player < 90:
            angle_player -= (70-angle_player)/50

        elif angle_player < 110:
            angle_player -= (110-angle_player)/50
        elif angle_player < 180:
            angle_player -= (110-angle_player)/50

        elif angle_player < 250:
            angle_player -= (250-angle_player)/50
        elif angle_player < 270:
            angle_player -= (250-angle_player)/50

        elif angle_player < 290:
            angle_player -= (290-angle_player)/50
        else:
            angle_player -= (290-angle_player)/50

    elif playerX > 1130:
        playerX = 1130
        if angle_player < 70:
            angle_player -= (70-angle_player)/50
        elif angle_player < 90:
            angle_player -= (70-angle_player)/50

        elif angle_player < 110:
            angle_player -= (110-angle_player)/50
        elif angle_player < 180:
            angle_player -= (110-angle_player)/50

        elif angle_player < 250:
            angle_player -= (250-angle_player)/50
        elif angle_player < 270:
            angle_player -= (250-angle_player)/50

        elif angle_player < 290:
            angle_player -= (290-angle_player)/50
        else:
            angle_player -= (290-angle_player)/50


    if playerY < 70:
        playerY = 70
        if angle_player < 20:
            angle_player -= (20-angle_player)/50
        elif angle_player < 90:
            angle_player -= (20-angle_player)/50

        elif angle_player < 160:
            angle_player -= (160-angle_player)/50
        elif angle_player < 180:
            angle_player -= (160-angle_player)/50

        elif angle_player < 200:
            angle_player -= (200-angle_player)/50
        elif angle_player < 270:
            angle_player -= (200-angle_player)/50

        elif angle_player < 340:
            angle_player -= (340-angle_player)/50
        else:
            angle_player -= (340-angle_player)/50


    elif playerY > 530:
        playerY = 530
        if angle_player < 20:
            angle_player -= (20-angle_player)/50
        elif angle_player < 90:
            angle_player -= (20-angle_player)/50

        elif angle_player < 160:
            angle_player -= (160-angle_player)/50
        elif angle_player < 180:
            angle_player -= (160-angle_player)/50

        elif angle_player < 200:
            angle_player -= (200-angle_player)/50
        elif angle_player < 270:
            angle_player -= (200-angle_player)/50

        elif angle_player < 340:
            angle_player -= (340-angle_player)/50
        else:
            angle_player -= (340-angle_player)/50


    player()

    pygame.display.update()
