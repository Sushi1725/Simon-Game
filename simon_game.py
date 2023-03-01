import pygame, sys, random
from pygame.locals import *
pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# rgb values of colours used
red = (100, 0, 0)
light_red = (255, 0, 0)
green = (0, 100, 0)
light_green = (0, 255, 0)
yellow = (100, 100, 0)
light_yellow = (255, 255, 0)
blue = (0, 0, 100)
light_blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (47, 47, 47)

# load all the images
logo = pygame.image.load('simon_logo.png')
main_page_image = pygame.image.load('simon_logo.png')
main_page_image_scaled = pygame.transform.scale(main_page_image, (450, 450))
start_button = pygame.image.load('start_game_image.png')

# load all the fonts
game_font = pygame.font.Font("Press_Start_2P\PressStart2P-Regular.ttf", 50)

# load all the sounds

# initialise the window of the game
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # creates the window
pygame.display.set_caption('Simon: The Game') # sets the name of the window
pygame.display.set_icon(logo) # sets the window's logo to the image

# variables
score = 0 # score number
running = True # is the game running?
pattern = [] # random pattern, so different each time
time_delay = 500 # milliseconds

##################
# Game Functions #
##################

def game_start_page(): # main screen page
    waiting = True
    # menu_music.play(-1)
    logo_bob = 50 # where the logo starts at (y-axis)
    title_text = game_font.render('Simon', True, white) # write the words

    bob_direction = True # true = down, false = up
    while waiting:
        for event in pygame.event.get() : # if the user closes the window, close the game
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]  # gets the location of where the mouse clicks
                y = pos[1]

                if 200 <= x <= 407 and 480 <= y <= 568:
                    # if the click is within a certain range
                    print('works')
                #     menu_music.stop()
                #     waiting = False

        # set background colour
        WINDOW.fill(grey)

        # display text and images
        WINDOW.blit(title_text, (190, 50))
        WINDOW.blit(main_page_image_scaled, (75, logo_bob))
        WINDOW.blit(start_button, (200, 480)) # is 207 x 88 pixel
        pygame.display.update()

        if logo_bob == 25:  # limit for how high the logo goes
            pygame.time.delay(300)
            bob_direction = True
        elif logo_bob == 75: # limit for how low the logo goes
            pygame.time.delay(300)
            bob_direction = False

        if bob_direction == True:
            logo_bob += 0.5 # move it down
        else:
            logo_bob -= 0.5 # move it up

    #     clock.tick(60)

    # while running:
    #     new_pattern()
    #     show_pattern()
    #     click_listen()

# The main function that controls the game
def main () :
    looping = True

    # The main game loop
    while looping :
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()


        game_start_page()

        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        pygame.display.update()
        fpsClock.tick(FPS)

main()