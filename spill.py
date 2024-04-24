import pygame
from pygame.sprite import Group
import random as random


pygame.init()
clock = pygame.time.Clock()
running = True

display_info = pygame.display.Info()
height = display_info.current_h
width = display_info.current_h

screen = pygame.display.set_mode((width * 1.20, height))

SpeedDefault = display_info.current_w * 0.02
DiagonalSpeedDefault = SpeedDefault / 4

class rectangle1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('rectangle.png').convert_alpha()
        self.Rheight = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.center = (width *1.20, height // 2)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= SpeedDefault
        if keys[pygame.K_DOWN]:
            self.rect.y += SpeedDefault
        if self.rect.y < 0:  # Upper bound
            self.rect.y = 0
        elif self.rect.y > height - self.Rheight:  # Lower bound
            self.rect.y = height - self.Rheight
        pass

class rectangle2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('rectangle.png').convert_alpha()
        self.Rheight = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.center = (0, height // 2)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= SpeedDefault
        if keys[pygame.K_s]:
            self.rect.y += SpeedDefault
        if self.rect.y < 0:  # Upper bound
            self.rect.y = 0
        elif self.rect.y > height - self.Rheight:  # Lower bound
            self.rect.y = height - self.Rheight
        pass


#Ball object
class circle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('circle.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = ((width * 1.20), height // 2)
    def update(self):
        collisions = pygame.sprite.spritecollide(self, players, False)
        if collisions:
            print("colision")
        elif collisions == False:
            print("no colisison")
        else:
            print("shit don wok")
        pass


all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
P1 = rectangle1()
P2 = rectangle2()
Ball = circle()

all_sprites.add(Ball, P1, P2)
players.add(P1, P2)


running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Clear the screen
    screen.fill("white")


    # Update all sprites
    all_sprites.update()

    # Draw all sprites onto the screen
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()