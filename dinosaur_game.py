import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dinosaur Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
dinosaur_img = pygame.image.load('dinosaur.png')
cactus_img = pygame.image.load('cactus.png')

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = "static/assets/dinosaur.PNG"
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - 50
        self.velocity = 0

    def update(self):
        self.velocity += 1
        self.rect.y += self.velocity
        if self.rect.y >= SCREEN_HEIGHT - 50:
            self.rect.y = SCREEN_HEIGHT - 50
            self.velocity = 0

    def jump(self):
        if self.rect.y == SCREEN_HEIGHT - 50:
            self.velocity = -15

# Define the cactus class
class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = "static/assets/cactus.PNG"
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT - 50

    def update(self):
        self.rect.x -= 5
        if self.rect.x < -self.rect.width:
            self.rect.x = SCREEN_WIDTH
            self.rect.y = SCREEN_HEIGHT - 50

# Create groups for sprites
all_sprites = pygame.sprite.Group()
cacti = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Update
    all_sprites.update()

    # Spawn new cactus
    if pygame.time.get_ticks() % 100 == 0:
        cactus = Cactus()
        all_sprites.add(cactus)
        cacti.add(cactus)

    # Collision detection
    if pygame.sprite.spritecollide(player, cacti, False):
        running = False

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
