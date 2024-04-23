import pygame
from pygame.sprite import Group


pygame.init()
clock = pygame.time.Clock()
running = True

display_info = pygame.display.Info()
height = display_info.current_h
width = display_info.current_h

screen = pygame.display.set_mode((width * 1.20, height))

SpeedDefault = display_info.current_w * 0.02
DiagonalSpeedDefault = SpeedDefault / 4

#circle object
class circle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('circle.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
    def update(self):
        #catches key presses
        keys = pygame.key.get_pressed()

        #diagonals
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            self.rect.y -= DiagonalSpeedDefault
            self.rect.x -= DiagonalSpeedDefault
        if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            self.rect.y -= DiagonalSpeedDefault
            self.rect.x += DiagonalSpeedDefault

        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.rect.y += DiagonalSpeedDefault
            self.rect.x -= DiagonalSpeedDefault
        if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self.rect.y += DiagonalSpeedDefault
            self.rect.x += DiagonalSpeedDefault

        #directionals
        if keys[pygame.K_UP]:
            self.rect.y -= SpeedDefault
        if keys[pygame.K_DOWN]:
            self.rect.y += SpeedDefault
        if keys[pygame.K_LEFT]:
            self.rect.x -= SpeedDefault
        if keys[pygame.K_RIGHT]:
            self.rect.x += SpeedDefault
        if keys[pygame.K_e]:
            self.rect.center = (width // 2, height // 2)   
        pass

all_sprites = pygame.sprite.Group()

my_sprite = circle()

all_sprites.add(my_sprite)

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