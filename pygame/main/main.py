import pygame
from random import randint
from math import sin, cos, pi, atan2


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

cng_player_img = 2
ground = pygame.image.load('pygame/resource/ground.jpg')

# groups
zombies = pygame.sprite.Group()
players = pygame.sprite.Group()

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
level = 0


class Player(pygame.sprite.Sprite):
    Img = pygame.image.load('pygame/resource/player_straight.png')
    Img_right = pygame.image.load('pygame/resource/player_right.png')
    Img_left = pygame.image.load('pygame/resource/player_left.png')
    Img_gun = pygame.image.load('pygame/resource/player_gun.png')
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

    def draw(self, zombies, fps):
        self.Img_show = pygame.transform.rotate(self.Img_loaded, self.angle)
        self.rect = self.Img_show.get_rect()
        self.rect.center = (self.x, self.y)

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

        screen.blit(self.Img_show, self.rect)
        screen.blit(self.gun_show, self.rect_gun)

        if self.die <= 0:
            self.kill()


class Zombie(pygame.sprite.Sprite):
    Img = pygame.image.load('pygame/resource/zombie.png')
    Img_flip = pygame.image.load('pygame/resource/zombie_flip.png')
    Img_die = pygame.image.load('pygame/resource/die.png')
    Img_die_flip = pygame.image.load('pygame/resource/die_flip.png')
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

    def draw(self):

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

        screen.blit(self.Img_loaded, self.rect)

        if self.die <= 0:
            self.corps -= 1
            if self.corps < 0:
                self.kill()


class Wall(pygame.sprite.Sprite):
    Img = pygame.image.load('pygame/resource/wall.jpg')

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

        screen.blit(self.Img_loaded, self.rect)


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

    player.with_in_screen()

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
for i in range(0):
    walls.append(Wall(22, 78))

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
    for i in range(0, WIDTH, 128):
        for j in range(0, HEIGHT, 128):
            screen.blit(ground, (i, j))
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
# k to kill all zombies
