import pygame
pygame.init()
import time

# Setup pygame screen
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Pygame heart')

# Setup some colors
screen_bg = (255, 255, 255)

# Set framerate
fps = 60
framerate = pygame.time.Clock()

# Load and define button images. Three states normal, hover, and pressed

heart_full = pygame.image.load('Assets\game_images\heart_full.png')
heart_empty = pygame.image.load('Assets\game_images\heart_empty.png')
current = heart_full

start_button_normal = pygame.image.load('Assets\main_menu_page_images\start_game_image.png')
start_button_pressed = pygame.image.load('Assets\main_menu_page_images\start_game_image_2.png')

# change cursor on hover
hand = pygame.SYSTEM_CURSOR_HAND

# Create heart class
class heart:
    def __init__(self, image, pos, callback):
        '''
            Create a animated button from images
            self.callback is for a funtion for the button to do - set to None
        '''
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.callback = callback

    def on(self):
        self.image = heart_full
    def off(self):
        self.image = heart_empty

# Set a variabe to True and enter loop
running = True
while running:

    # Fill screen with background color
    screen.fill(screen_bg)

    # Start event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create a button from the heart class with args for state, position, and callback
    hearts = heart(heart_full, (500, 500), None)

    # Get mouse button from pygame
    left, middle, right = pygame.mouse.get_pressed()

    # If cursor is over button change state to hover else state is normal
    if hearts.rect.collidepoint(pygame.mouse.get_pos()):
        

        # If left mouse button pressed change state to pressed else hover
        if left and hearts.rect.collidepoint(pygame.mouse.get_pos()):
            hearts.off()
            screen.blit(hearts.image, hearts.rect)
            pygame.display.update()
            pygame.time.delay(50)
            hearts.on()
            screen.blit(hearts.image, hearts.rect)
            pygame.display.update()
            pygame.time.delay(50)
            hearts.off()
            screen.blit(hearts.image, hearts.rect)
            pygame.display.update()
            pygame.time.delay(50)
            hearts.on()
            screen.blit(hearts.image, hearts.rect)
            pygame.display.update()
            pygame.time.delay(50)
            hearts.off()
            screen.blit(hearts.image, hearts.rect)
            pygame.display.update()
            pygame.time.delay(50)
            hearts.on()
            screen.blit(hearts.image, hearts.rect)
            pygame.display.update()
            pygame.time.delay(50)
            hearts.off()
            screen.blit(hearts.image, hearts.rect)
            pygame.display.update()
            pygame.time.delay(50)
            hearts.on()
            screen.blit(hearts.image, hearts.rect)
            pygame.display.update()
            pygame.time.delay(50)
            hearts.off()
            screen.blit(hearts.image, hearts.rect)
            pygame.display.update()
            pygame.time.delay(50)
            hearts.on()
            screen.blit(hearts.image, hearts.rect)
            pygame.display.update()
            pygame.time.delay(50)
            
            
    #     else:
    #         hearts.on()
    # else:
    #     hearts.on()

    # Blit button to screen
    screen.blit(hearts.image, hearts.rect)

    # Set framerate and update
    framerate.tick(fps)
    pygame.display.update()