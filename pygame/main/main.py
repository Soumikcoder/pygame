import pygame
import random
#
pygame.init()

# Caption and Icon
pygame.display.set_caption("Invader")
icon = pygame.image.load('pygame/resource/logo.png')
pygame.display.set_icon(icon)

# player
playerImg_straight = pygame.image.load('pygame/resource/player_straight.png')
playerImg_right = pygame.image.load('pygame/resource/player_right.png')
playerImg_left = pygame.image.load('pygame/resource/player_left.png')
playerImg0 = playerImg_straight
rect0 = playerImg0.get_rect()
playerX = 400
playerY = 300
rect0.center = (playerX, playerY)


clock = pygame.time.Clock()


def player():

    global playerX
    global playerY

    if playerX <= 70:
        playerX = 70
    elif playerX >= 730:
        playerX = 730
    if playerY <= 70:
        playerY = 70
    elif playerY >= 530:
        playerY = 530

    rect0.center = (playerX, playerY)
    screen.blit(playerImg0, rect0)


# seed generation
seed = random.randint(0, 9)
chunk_coords = [0, 0]

# create screen
screen = pygame.display.set_mode((800, 600))

running = True
# update_chunk(coords)
while running:

    # RGB = Red, Green, Blue
    screen.fill((40, 40, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
        playerX -= 1.8
        playerImg0 = playerImg_left

    if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
        playerX += 1.8
        playerImg0 = playerImg_right

    if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:
        playerY -= 1.8
        playerImg0 = playerImg_straight

    if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:
        playerY += 1.8
        playerImg0 = playerImg_straight

    player()

    clock.tick(120)
    pygame.display.update()
