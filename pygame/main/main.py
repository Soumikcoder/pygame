import pygame
import random
#
pygame.init()

# Caption and Icon
pygame.display.set_caption("Invader")
icon = pygame.image.load('pygame/resource/logo.png')
pygame.display.set_icon(icon)

# player
playerImg_face = pygame.image.load('pygame/resource/pov.png')
playerImg_back = pygame.image.load('pygame/resource/povback.png')
playerImg_right = pygame.image.load('pygame/resource/povright.png')
playerImg_left = pygame.image.load('pygame/resource/povleft.png')
playerImg = playerImg_face
playerX = 330
playerY = 420

clock=pygame.time.Clock()
def player(x, y):
    screen.blit(playerImg, (x, y))

#seed generation
seed=random.randint(0,9);
chunk_coords=[0,0]

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

    if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a] :
            playerX -= 1.8
            playerImg = playerImg_left

    if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
            playerX += 1.8
            playerImg = playerImg_right

    if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:
            playerY -= 1.8
            playerImg = playerImg_back

    if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:
            playerY += 1.8
            playerImg = playerImg_face

    if playerX <= -20:
        playerX = -20
    elif playerX >= 690:
        playerX = 690
    if playerY <= 0:
        playerY = 0
    elif playerY >= 470:
        playerY = 470
    player(playerX, playerY)
    clock.tick(120)
    pygame.display.update()
