import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((50,255,10))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(1,width-55),random.randint(1,height-55))
        self.x_speed = 1
    def update(self):


        if self.rect.x <= 0:
            self.x_speed *= -1
        if self.rect.x >= width-50:
            print("passed")
            self.x_speed *= -1

        self.rect.x += self.x_speed

pygame.init()
pygame.mixer.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("My game")

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()

all_sprites.add(player)


running = True

while running:
    clock.tick(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.add(player)

    all_sprites.update()
    # Draw
    screen.fill((100,100,100))
    all_sprites.draw(screen)
    pygame.display.flip()
