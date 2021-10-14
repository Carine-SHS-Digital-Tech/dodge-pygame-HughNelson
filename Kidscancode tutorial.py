import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((50,255,10))
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,height/2)
        self.x_speed = 1
    def update(self):


        if self.rect.colliderect(Player()):
            self.x_speed *= -1
        if self.rect.x >= width-50:
            print("passed")
            self.x_speed *= -1

        self.rect.x += self.x_speed
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 100))
        self.image.fill((50,255,10))
        self.rect = self.image.get_rect()
        self.rect.center = (30,height/2)
        self.x_speed = 1

    def move(self, direction):
        if direction == "down":
            self.rect.y += 1



pygame.init()
pygame.mixer.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("My game")

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
ball = Ball()
player = Player()
all_sprites.add(ball)


running = True

while running:


    clock.tick(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.move("down")
            if event.key == pygame.K_UP:
                player.move("up")

    # Update
    all_sprites.add(ball)
    all_sprites.add(player)

    all_sprites.update()
    # Draw
    screen.fill((100,100,100))
    all_sprites.draw(screen)
    pygame.display.flip()
