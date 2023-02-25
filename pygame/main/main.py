import pygame

#
pygame.init()

# Caption and Icon
pygame.display.set_caption("Invader")
icon = pygame.image.load('./resource/logo.png')
pygame.display.set_icon(icon)

# player
playerImg_face = pygame.image.load('./resource/pov.png')
playerImg_back = pygame.image.load('./resource/povback.png')
playerImg = playerImg_face
playerX = 330
playerY = 420

clock=pygame.time.Clock()
def player(x, y):
    screen.blit(playerImg, (x, y))


# create screen
screen = pygame.display.set_mode((800, 600))

running = True

while running:

    # RGB = Red, Green, Blue
    screen.fill((40, 40, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= 1.8

        if event.key == pygame.K_RIGHT:
            playerX += 1.8

        if event.key == pygame.K_UP:
            playerY -= 1.8
            playerImg = playerImg_back

        if event.key == pygame.K_DOWN:
            playerY += 1.8
            playerImg = playerImg_face

    if playerX <= -20:
        playerX = -20
    elif playerX >= 690:
        playerX = 690

    player(playerX, playerY)
    clock.tick(60)
    pygame.display.update()

