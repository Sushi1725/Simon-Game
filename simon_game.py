import pygame
import sys
import random
from pygame.locals import *

# Game Setup
FPS = 60
pygame.init()
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
# change cursor on hover
hand = pygame.SYSTEM_CURSOR_HAND

# rgb values of colours used
white = (255, 255, 255)
black = (0, 0, 0)
darker_grey = (47, 47, 47)
grey = (19, 19, 19)

# load all the images
logo = pygame.image.load('Assets/simon_logo.png')
main_page_image_scaled = pygame.transform.scale(logo, (450, 450))
start_button_normal = pygame.image.load('Assets/main_menu_page_images/start_game_image.png')
start_button_pressed = pygame.image.load('Assets/main_menu_page_images/start_game_image_2.png')
settings = pygame.image.load('Assets/main_menu_page_images/gear_cog.png') # 547, 600
settings_scaled = pygame.transform.scale(settings, (64,70))
information = pygame.image.load('Assets/main_menu_page_images/information.png') # 50 130
information_scaled = pygame.transform.scale(information, (30, 78))
bg_green = pygame.image.load('Assets/main_menu_page_images/bg_green.png')
bg_red = pygame.image.load('Assets/main_menu_page_images/bg_red.png')
bg_yellow = pygame.image.load('Assets/main_menu_page_images/bg_yellow.png')
bg_blue = pygame.image.load('Assets/main_menu_page_images/bg_blue.png')

blue_light = pygame.image.load('Assets/game_images/blue_light.png')
blue_light_scaled = pygame.transform.scale(blue_light, (225, 225))
blue = pygame.image.load('Assets/game_images/blue.png')
green_light = pygame.image.load('Assets/game_images/green_light.png')
green_light_scaled = pygame.transform.scale(green_light, (225, 225))
green = pygame.image.load('Assets/game_images/green.png')
red_light = pygame.image.load('Assets/game_images/red_light.png')
red_light_scaled = pygame.transform.scale(red_light, (225, 225))
red = pygame.image.load('Assets/game_images/red.png')
yellow_light = pygame.image.load('Assets/game_images/yellow_light.png')
yellow_light_scaled = pygame.transform.scale(yellow_light, (225, 225))
yellow = pygame.image.load('Assets/game_images/yellow.png')

blue_scaled = pygame.transform.scale(blue, (225, 225))
green_scaled = pygame.transform.scale(green, (225, 225))
red_scaled = pygame.transform.scale(red, (225, 225))
yellow_scaled = pygame.transform.scale(yellow, (225, 225))


# load all the fonts
gameplay_font = 'Assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf'
game_font_start = pygame.font.Font(gameplay_font, 50)
game_font = pygame.font.Font(gameplay_font, 20)

# load all the sounds

# initialise the window of the game
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # creates the window
pygame.display.set_caption('Simon: The Game') # sets the name of the window
pygame.display.set_icon(logo) # sets the window's logo to the image

# variables
score = 0 # score number
running = True # is the game running?
pattern = [] # random pattern, so different each time
time_delay = 750 # milliseconds

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
    title_text = game_font_start.render('SIMON', True, white) # write the words
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
                # game_simon_play_page()
            else:
                button.hover()
        else:
            button.normal()

        # display text and images
        WINDOW.blit(bg_blue, (0,302))
        WINDOW.blit(bg_green, (402,302))
        WINDOW.blit(bg_yellow, (0,0))
        WINDOW.blit(bg_red, (402, 0))
        WINDOW.blit(title_text, (279, 50))
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

    while running:
        new_pattern()
        show_pattern()
    #     click_listen()

def game_simon_play_page(yellow_colour = yellow_scaled, blue_colour = blue_scaled, green_colour = green_scaled, red_colour = red_scaled):
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

    # refresh display
    WINDOW.fill(grey)

    # draw elements
    # score = 0
    score_text_temp = game_font.render('Score: 0', True, white)
    WINDOW.blit(score_text_temp, (50, 50))

    WINDOW.blit(yellow_colour, (175, 300))
    WINDOW.blit(blue_colour, (400, 300))
    WINDOW.blit(green_colour, (400, 75))
    WINDOW.blit(red_colour, (175, 75))
    pygame.display.update()
        
        # blue_scaled = pygame.transform.scale(blue, (225, 225)).convert_alpha() # optimises the checking the button
        # green_scaled = pygame.transform.scale(green, (225, 225)).convert_alpha()
        # red_scaled = pygame.transform.scale(red, (225, 225)).convert_alpha()
        # yellow_scaled = pygame.transform.scale(yellow, (225, 225)).convert_alpha()
        # blue_scaled_pos = (400, 300)
        # green_scaled_pos = (400, 75)
        # red_scaled_pos = (175, 75)
        # yellow_scaled_pos = (175, 300)

        # while True:
        #     for event in pygame.event.get():
        #         if event.type == QUIT :
        #             pygame.quit()
        #             sys.exit()
        #         if event.type == pygame.MOUSEBUTTONDOWN: # one for each colour
        #             try:
        #                 mask = pygame.mask.from_surface(blue_scaled) # mask makes it so that the translucent part of the image cannot be clicked
        #                 if mask.get_at((event.pos[0]-blue_scaled_pos[0], event.pos[1]-blue_scaled_pos[1])):
        #                     WINDOW.fill(grey)
        #                     score = score + 1
        #                     print(score)
        #                     score_text = game_font.render('Score: ' + str(score), True, white)
        #                     WINDOW.blit(score_text, (50, 50))
        #             except IndexError:
        #                 pass
        #             try:
        #                 mask = pygame.mask.from_surface(red_scaled)
        #                 if mask.get_at((event.pos[0]-red_scaled_pos[0], event.pos[1]-red_scaled_pos[1])):
        #                     WINDOW.fill(grey)
        #                     score = score + 1
        #                     print(score)
        #                     score_text = game_font.render('Score: ' + str(score), True, white)
        #                     WINDOW.blit(score_text, (50, 50))
        #             except IndexError:
        #                 pass
        #             try:
        #                 mask = pygame.mask.from_surface(green_scaled)
        #                 if mask.get_at((event.pos[0]-green_scaled_pos[0], event.pos[1]-green_scaled_pos[1])):
        #                     WINDOW.fill(grey)
        #                     score = score + 1
        #                     print(score)
        #                     score_text = game_font.render('Score: ' + str(score), True, white)
        #                     WINDOW.blit(score_text, (50, 50))
        #             except IndexError:
        #                 pass
        #             try:
        #                 mask = pygame.mask.from_surface(yellow_scaled)
        #                 if mask.get_at((event.pos[0]-yellow_scaled_pos[0], event.pos[1]-yellow_scaled_pos[1])):
        #                     WINDOW.fill(grey)
        #                     score = score + 1
        #                     print(score)
        #                     score_text = game_font.render('Score: ' + str(score), True, white)
        #                     WINDOW.blit(score_text, (50, 50))
        #             except IndexError:
        #                 pass

        #     WINDOW.blit(blue_scaled, blue_scaled_pos)
        #     WINDOW.blit(green_scaled, green_scaled_pos)
        #     WINDOW.blit(red_scaled, red_scaled_pos)
        #     WINDOW.blit(yellow_scaled, yellow_scaled_pos)
        #     pygame.display.update()

def new_pattern():
    global score
    score = len(pattern)
    pattern.append(random.randint(1, 4))

def show_pattern():
    # 1 = green
    # 2 = red
    # 3 = yellow
    # 4 = blue
    # print('should be in showing pattern now')

    time_delay = 750 - 100 * int(len(pattern) / 5)
    print('more than 100')
    if time_delay <= 100:
        print('now 100')
        time_delay = 100

    game_simon_play_page()
    # print('here')
    pygame.time.delay(1000)

    for x in pattern:
        # print('now doing x in pattern')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        # blue_scaled_pos = (400, 300)
        # green_scaled_pos = (400, 75)
        # red_scaled_pos = (175, 75)
        # yellow_scaled_pos = (175, 300)

        if x == 1:
            # RED
            # print('red')
            print(pattern)
            # WINDOW.blit(red_light_scaled, red_scaled_pos)
            game_simon_play_page(red_colour = red_light_scaled)
            # red_sound.play()
            pygame.time.delay(time_delay)
            game_simon_play_page()
            # red_sound.stop()
        elif x == 2:
            # GREEN
            # print('green')
            print(pattern)
            # WINDOW.blit(green_light_scaled, green_scaled_pos)
            game_simon_play_page(green_colour = green_light_scaled)
            # green_sound.play()
            pygame.time.delay(time_delay)
            game_simon_play_page()
            # green_sound.stop()
        elif x == 3:
            # YELLOW
            # print('yellow')
            print(pattern)
            # WINDOW.blit(yellow_light_scaled, yellow_scaled_pos)
            game_simon_play_page(yellow_colour = yellow_light_scaled)
            # yellow_sound.play()
            pygame.time.delay(time_delay)
            game_simon_play_page()
            # yellow_sound.stop()
        elif x == 4:
            # BLUE
            # print('blue')
            print(pattern)
            # WINDOW.blit(blue_light_scaled, blue_scaled_pos)
            game_simon_play_page(blue_colour = blue_light_scaled)
            # blue_sound.play()
            pygame.time.delay(time_delay)
            game_simon_play_page()
            # blue_sound.stop()

        pygame.time.delay(time_delay)

game_start_page()