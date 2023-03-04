import pygame, sys, random
from pygame.locals import *
pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# change cursor on hover
hand = pygame.SYSTEM_CURSOR_HAND

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# rgb values of colours used
white = (255, 255, 255)
black = (0, 0, 0)
grey = (47, 47, 47)

# load all the images
logo = pygame.image.load('Assets\simon_logo.png')
main_page_image_scaled = pygame.transform.scale(logo, (450, 450))
start_button_normal = pygame.image.load('Assets\main_menu_page_images\start_game_image.png')
start_button_pressed = pygame.image.load('Assets\main_menu_page_images\start_game_image_2.png')
settings = pygame.image.load('Assets\main_menu_page_images\gear_cog.png') # 547, 600
settings_scaled = pygame.transform.scale(settings, (64,70))
information = pygame.image.load('Assets\main_menu_page_images\information.png') # 50 130
information_scaled = pygame.transform.scale(information, (30, 78))

blue_light = pygame.image.load('Assets\game_images/blue_light.png')
blue_light_scaled = pygame.transform.scale(blue_light, (225, 225))
blue = pygame.image.load('Assets\game_images/blue.png')
blue_scaled = pygame.transform.scale(blue, (225, 225))
green_light = pygame.image.load('Assets\game_images\green_light.png')
green_light_scaled = pygame.transform.scale(green_light, (225, 225))
green = pygame.image.load('Assets\game_images\green.png')
green_scaled = pygame.transform.scale(green, (225, 225))
red_light = pygame.image.load('Assets\game_images/red_light.png')
red_light_scaled = pygame.transform.scale(red_light, (225, 225))
red = pygame.image.load('Assets\game_images/red.png')
red_scaled = pygame.transform.scale(red, (225, 225))
yellow_light = pygame.image.load('Assets\game_images\yellow_light.png')
yellow_light_scaled = pygame.transform.scale(yellow_light, (225, 225))
yellow = pygame.image.load('Assets\game_images\yellow.png')
yellow_scaled = pygame.transform.scale(yellow, (225, 225))


# load all the fonts
game_font = pygame.font.Font("Assets/fonts\Press_Start_2P\PressStart2P-Regular.ttf", 50)

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

class Start_Button: # the button class
    def __init__(button, button_image, pos, callback):  # intialise the class
        '''
            Create a animated button from images
            self.callback is for a funtion for the button to do - set to None
        '''
        button.image = button_image
        button.rect = button.image.get_rect(topright=(495, 480))
        button.callback = callback

    def normal(button): # the normal state of the button
        button.image = start_button_normal
        pygame.mouse.set_cursor()

    def hover(button): # the hovered state of the button
        pygame.mouse.set_cursor(hand)

    def pressed(button): # the pressed state of the button
        button.image = start_button_pressed
        pygame.mouse.set_cursor()

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

                # if 200 <= x <= 407 and 480 <= y <= 568: # for the start button
                #     # if the click is within a certain range
                #     print('go to start page')
                #     # menu_music.stop()
                #     # waiting = False
                
                if 510 <= x <= 574 and 30 <= y <= 100: # for the settings button
                    # if the click is within a certain range
                    print('go to settings page')

        # set background colour
        WINDOW.fill(grey)

        button = Start_Button(start_button_normal, (100, 100), None) # get the button from the Start_Button class
        left, middle, right = pygame.mouse.get_pressed()

        # if cursor is over button change state to 'hover'
        if button.rect.collidepoint(pygame.mouse.get_pos()):
            button.hover()
            # if button pressed, change the state to 'pressed' otherwise 'hover'
            if left and button.rect.collidepoint(pygame.mouse.get_pos()):
                button.pressed()
                waiting = False
                game_simon_play_page()
            else:
                button.hover()
        else:
            button.normal()

        # display text and images
        WINDOW.blit(title_text, (290, 50))
        WINDOW.blit(main_page_image_scaled, (175, logo_bob))
        WINDOW.blit(button.image, button.rect)
        WINDOW.blit(settings_scaled, (WINDOW_WIDTH-90, 30))
        WINDOW.blit(information_scaled, (WINDOW_WIDTH-70, 500))
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

        fpsClock.tick(FPS)

    # while running:
    #     new_pattern()
    #     show_pattern()
    #     click_listen()

def game_simon_play_page():
    looping = True

    # The main game loop
    while looping :
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

        # refresh display
        WINDOW.fill(grey)

        # draw elements
        # score_text = game_font.render('Score: ' + str(score), True, white)
        # WINDOW.blit(score_text, (50, 50))

        WINDOW.blit(blue_scaled, (400, 300))
        WINDOW.blit(green_scaled, (400, 75))
        WINDOW.blit(red_scaled, (175, 75))
        WINDOW.blit(yellow_scaled, (175, 300))
        pygame.display.update()

game_start_page()