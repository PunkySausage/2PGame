# ship game part 1 (?)
# player sprite and controlling
from os import path
import pygame
import random

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 600
HEIGHT = 700
FPS = 60

speed1 = 5
speed2 = 5
speedofbullet = 8
# adding colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (100, 100, 255)
YELLOW = (255, 255, 0)

# creating the game and window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("игра на 2")
clock = pygame.time.Clock()

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player1_img, (80, 68))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 20

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= speed1
        if keystate[pygame.K_RIGHT]:
            self.rect.x += speed1
        if keystate[pygame.K_DOWN]:
            self.rect.y += speed1
        if keystate[pygame.K_UP]:
            self.rect.y -= speed1
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        
    def shoot1(self):
        bullet1 = Bullet1(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet1)
        bullets1.add(bullet1)


class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player2_img_rotate, (80, 68))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.top = HEIGHT - 660

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.rect.x -= speed2
        if keystate[pygame.K_d]:
            self.rect.x += speed2
        if keystate[pygame.K_s]:
            self.rect.y += speed2
        if keystate[pygame.K_w]:
            self.rect.y -= speed2
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        
    def shoot2(self):
        bullet2 = Bullet2(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet2)
        bullets2.add(bullet2)


class Bullet1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet1_img, (15, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y

    def update(self):
        self.rect.y -= speedofbullet
        if self.rect.bottom < 0:
            self.kill()

class Bullet2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet2_img, (15, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y

    def update(self):
        self.rect.y += speedofbullet
        if self.rect.top < 0:
            self.kill()

background = pygame.image.load(path.join(img_dir, "blue.png")).convert()
background_rect = background.get_rect()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player1_img = pygame.image.load(path.join(img_dir, "playerLife2_blue.png")).convert()
player2_img = pygame.image.load(path.join(img_dir, "playerLife2_red.png")).convert()
player2_img_rotate = pygame.transform.rotate(player2_img, 180)
bullet2_img = pygame.image.load(path.join(img_dir, "laserRed02.png")).convert()
bullet1_img = pygame.image.load(path.join(img_dir, "laserBlue02.png")).convert()

bullets1 = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player1 = Player1()
player2 = Player2()
all_sprites.add(player1)
all_sprites.add(player2)


# game cycle
running = True
while running:
    # keeping the cycle on the correct speed
    clock.tick(FPS)
    # proccess ( event )
    for event in pygame.event.get():
        # checking for window closing
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                player2.shoot2()
            elif event.key == pygame.K_l:
                player1.shoot1()

        
    # updating
    all_sprites.update()

    hits = pygame.sprite.spritecollide(player1, bullets2, False)
    if hits:
        running = False
    
    hits = pygame.sprite.spritecollide(player2, bullets1, False)
    if hits:
        running = False


    # rendering
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    
    # After rendering everything, flip the screen
    pygame.display.flip()

pygame.quit()