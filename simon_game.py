import pygame
import sys
import random
import time
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
mainPageImageScaled = pygame.transform.scale(logo, (450, 450))
startButtonNormal = pygame.image.load('Assets/main_menu_page_images/start_game_image.png')
startButtonPressed = pygame.image.load('Assets/main_menu_page_images/start_game_image_2.png')
settings = pygame.image.load('Assets/main_menu_page_images/gear_cog.png') # 547, 600
settingsScaled = pygame.transform.scale(settings, (64,70))
information = pygame.image.load('Assets/main_menu_page_images/information.png') # 50 130
informationScaled = pygame.transform.scale(information, (30, 78))
bgGreen = pygame.image.load('Assets/main_menu_page_images/bg_green.png')
bgRed = pygame.image.load('Assets/main_menu_page_images/bg_red.png')
bgYellow = pygame.image.load('Assets/main_menu_page_images/bg_yellow.png')
bgBlue = pygame.image.load('Assets/main_menu_page_images/bg_blue.png')

# heartImageFull = pygame.image.load()
# heartImageTransitioning = pygame.image.load()

blueLight = pygame.image.load('Assets/game_images/blue_light.png')
blueLightScaled = pygame.transform.scale(blueLight, (225, 225))
blue = pygame.image.load('Assets/game_images/blue.png')
blueScaled = pygame.transform.scale(blue, (225, 225))
greenLight = pygame.image.load('Assets/game_images/green_light.png')
greenLightScaled = pygame.transform.scale(greenLight, (225, 225))
green = pygame.image.load('Assets/game_images/green.png')
greenScaled = pygame.transform.scale(green, (225, 225))
redLight = pygame.image.load('Assets/game_images/red_light.png')
redLightScaled = pygame.transform.scale(redLight, (225, 225))
red = pygame.image.load('Assets/game_images/red.png')
redScaled = pygame.transform.scale(red, (225, 225))
yellowLight = pygame.image.load('Assets/game_images/yellow_light.png')
yellowLightScaled = pygame.transform.scale(yellowLight, (225, 225))
yellow = pygame.image.load('Assets/game_images/yellow.png')
yellowScaled = pygame.transform.scale(yellow, (225, 225))

blackGradientScreen = pygame.image.load('Assets/main_menu_page_images/black_bg.png')

# load all the fonts
GAMEPLAY_FONT = 'Assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf'
gameFontStart = pygame.font.Font(GAMEPLAY_FONT, 50) # size 50 font
gameFont = pygame.font.Font(GAMEPLAY_FONT, 20) # size 20 font

# load all the sounds

# initialise the window of the game
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # creates the window
pygame.display.set_caption('Simon: The Game') # sets the name of the window
pygame.display.set_icon(logo) # sets the window's logo to the image

# variables
score = 0 # score number
running = True
pattern = [] # store array of previous colours
timeDelay = 500 # milliseconds
playerPattern = [] # store array of player guesses (used to compare)

##################
# Game Functions #
##################

class Start_Button: # the button class
    def __init__(button, buttonImage, pos, callback):  # intialise the class
        '''
            Create a animated button from images
            self.callback is for a funtion for the button to do - set to None
        '''
        button.image = buttonImage
        button.rect = button.image.get_rect(topright=(495, 480))
        button.callback = callback

    def normal(button): # the normal state of the button
        button.image = startButtonNormal
        pygame.mouse.set_cursor()
    
    def hover(button): # the hovered state of the button
        pygame.mouse.set_cursor(hand)
    
    def pressed(button): # the pressed state of the button
        button.image = startButtonPressed
        pygame.mouse.set_cursor()

class Heart_Animation: # the heart animation class
    def __init__(heartAnimation, heartImages, pos, callback):
        '''
        '''
        heartAnimation.image = heartImages
        heartAnimation.rect = heartAnimation.image.get_rect(topright=(0, 0))
        heartAnimation.callback = callback
        
    def paused(heartAnimation):
        heartAnimation.image = heartImageFull
    
    def playing(heartAnimation):
        heartAnimation.image = heartImageTransitioning

def render_game_start_page(): # main screen page
    waiting = True
    # menu_music.play(-1)
    logoBob = 50 # where the logo starts at (y-axis)
    titleText = gameFontStart.render('SIMON', True, white) # write the words
    bobDirection = True # true = down, false = up
    
    while waiting:
        for event in pygame.event.get() : # if the user closes the window, close the game
            if event.type == QUIT :
                quit()
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
    
        button = Start_Button(startButtonNormal, (100, 100), None) # get the button from the Start_Button class
        left, middle, right = pygame.mouse.get_pressed()
    
        # if cursor is over button change state to 'hover'
        if button.rect.collidepoint(pygame.mouse.get_pos()):
            button.hover()
            # if button pressed, change the state to 'pressed' otherwise 'hover'
            if left and button.rect.collidepoint(pygame.mouse.get_pos()):
                button.pressed()
                waiting = False
                # render_game_simon_play_page()
            else:
                button.hover()
        else:
            button.normal()
    
        # display text and images
        WINDOW.blit(bgBlue, (0,302))
        WINDOW.blit(bgGreen, (402,302))
        WINDOW.blit(bgYellow, (0,0))
        WINDOW.blit(bgRed, (402, 0))
        WINDOW.blit(titleText, (279, 50))
        WINDOW.blit(mainPageImageScaled, (175, logoBob))
        WINDOW.blit(button.image, button.rect)
        WINDOW.blit(settingsScaled, (WINDOW_WIDTH-90, 30))
        WINDOW.blit(informationScaled, (WINDOW_WIDTH-70, 500))
        pygame.display.update()
    
        if logoBob == 25:  # limit for how high the logo goes
            pygame.time.delay(300)
            bobDirection = True
        elif logoBob == 75: # limit for how low the logo goes
            pygame.time.delay(300)
            bobDirection = False
    
        if bobDirection == True:
            logoBob += 0.5 # move it down
        else:
            logoBob -= 0.5 # move it up
    
        fpsClock.tick(FPS)
    
    while running:
        random_pattern()
        show_pattern()
        store_player_guess()

def render_game_simon_play_page(yellowColour = yellowScaled, blueColour = blueScaled, greenColour = greenScaled, redColour = redScaled):
    for event in pygame.event.get() :
        if event.type == QUIT :
            quit()
    
    # refresh display
    WINDOW.fill(grey)
    
    # draw elements
    global score
    # score_text_temp = gameFont.render('Score: 0', True, white)
    WINDOW.blit((gameFont.render('Score: 0', True, white)), (50, 50))
    
    WINDOW.blit(yellowColour, (175, 300))
    WINDOW.blit(blueColour, (400, 300))
    WINDOW.blit(greenColour, (400, 75))
    WINDOW.blit(redColour, (175, 75))
    pygame.display.update()

def random_pattern():
    global score
    score = len(pattern)
    pattern.append(random.randint(1, 4))

def quit():
    running = False
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def show_pattern():
    # 1 = red
    # 2 = green
    # 3 = yellow
    # 4 = blue
    
    timeDelay = 500 - 100 * int(len(pattern) / 5)
    print('back to show pattern')
    if timeDelay <= 100:
        print('now 100')
        timeDelay = 100
    
    render_game_simon_play_page()
    pygame.time.delay(300)
    
    for x in pattern:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
    
        if x == 1: # 1 = red
            print(pattern)
            render_game_simon_play_page(redColour = redLightScaled) # change it into light mode
            pygame.time.delay(timeDelay) # current set time delay (faster as the game progresses)
            render_game_simon_play_page() # move it back into the "all dark" state
        elif x == 2: # 2 = green
            print(pattern)
            render_game_simon_play_page(greenColour = greenLightScaled) # change it into light mode
            pygame.time.delay(timeDelay) # current set time delay (faster as the game progresses)
            render_game_simon_play_page() # move it back into the "all dark" state
        elif x == 3: # 3 = yellow
            print(pattern)
            render_game_simon_play_page(yellowColour = yellowLightScaled) # change it into light mode
            pygame.time.delay(timeDelay) # current set time delay (faster as the game progresses)
            render_game_simon_play_page() # move it back into the "all dark" state
        elif x == 4: # 4 = blue
            print(pattern)
            render_game_simon_play_page(blueColour = blueLightScaled) # change it into light mode
            pygame.time.delay(timeDelay) # current set time delay (faster as the game progresses)
            render_game_simon_play_page() # move it back into the "all dark" state
    
        pygame.time.delay(timeDelay)

def store_player_guess():
    print("now in store player guess")
    # 1 = red
    # 2 = green
    # 3 = yellow
    # 4 = blue
    
    turn_time = time.time()
    global playerPattern
    playerPattern = []
    global pattern
    global score
    
    clickBlueScaled = pygame.transform.scale(blue, (225, 225)).convert_alpha() # optimises the checking the button
    clickGreenScaled = pygame.transform.scale(green, (225, 225)).convert_alpha()
    clickRedScaled = pygame.transform.scale(red, (225, 225)).convert_alpha()
    clickYellowScaled = pygame.transform.scale(yellow, (225, 225)).convert_alpha()
    blueScaledPos = (400, 300)
    greenScaledPos = (400, 75)
    redScaledPos = (175, 75)
    yellowScaledPos = (175, 300)
        
    # while time.time() <= turn_time + 3 and len(playerPattern) < len(pattern):
    moment_turn_time = time.time()
    while moment_turn_time <= turn_time + 3 and len(playerPattern) < len(pattern):
        # print(str(len(playerPattern)) + ", " + str(len(pattern)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                try: # only work if the click isnt in a transparent area
                    mask = pygame.mask.from_surface(clickRedScaled)
                    if mask.get_at((event.pos[0]-redScaledPos[0], event.pos[1]-redScaledPos[1])):
                        render_game_simon_play_page(redColour = redLightScaled) # change it into light mode
                        pygame.time.delay(timeDelay)
                        render_game_simon_play_page()
                        playerPattern.append(1) # add it to the end of the array
                        check_pattern(playerPattern)
                        turn_time = time.time() # get the current time
                except IndexError:  # if the click is in a transparent area, dont worry about it
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                try: # only work if the click isnt in a transparent area
                    mask = pygame.mask.from_surface(clickGreenScaled)
                    if mask.get_at((event.pos[0]-greenScaledPos[0], event.pos[1]-greenScaledPos[1])):
                        render_game_simon_play_page(greenColour = greenLightScaled) # change it into light mode
                        pygame.time.delay(timeDelay)
                        render_game_simon_play_page()
                        playerPattern.append(2) # add it to the end of the array
                        check_pattern(playerPattern)
                        turn_time = time.time() # get the current time
                except IndexError:  # if the click is in a transparent area, dont worry about it
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                try: # only work if the click isnt in a transparent area
                    mask = pygame.mask.from_surface(clickYellowScaled)
                    if mask.get_at((event.pos[0]-yellowScaledPos[0], event.pos[1]-yellowScaledPos[1])):
                        render_game_simon_play_page(yellowColour = yellowLightScaled) # change it into light mode
                        pygame.time.delay(timeDelay)
                        render_game_simon_play_page()
                        playerPattern.append(3) # add it to the end of the array
                        check_pattern(playerPattern)
                        turn_time = time.time() # get the current time
                except IndexError:  # if the click is in a transparent area, dont worry about it
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                try: # only work if the click isnt in a transparent area
                    mask = pygame.mask.from_surface(clickBlueScaled) # mask makes it so that the translucent part of the image cannot be clicked
                    if mask.get_at((event.pos[0]-blueScaledPos[0], event.pos[1]-blueScaledPos[1])):
                        # WINDOW.fill(grey)
                        # score = score + 1
                        # print(score)
                        # score_text = gameFont.render('Score: ' + str(score), True, white)
                        # WINDOW.blit(score_text, (50, 50))
                        render_game_simon_play_page(blueColour = blueLightScaled) # change it into light mode
                        pygame.time.delay(timeDelay)
                        render_game_simon_play_page()
                        playerPattern.append(4) # add it to the end of the array
                        check_pattern(playerPattern)
                        turn_time = time.time() # get the current time
                except IndexError:  # if the click is in a transparent area, dont worry about it
                    pass
    
    # if time.time() > turn_time + 3:
    #     print('game over?')
    #     render_game_over_screen()

def check_pattern(playerPattern):
    if playerPattern != pattern[:len(playerPattern)]: # if the last one of the player guess is not the same as the last one of the pattern
        # print(str(playerPattern) + ', ' + str(pattern[:len(playerPattern)]))
        render_game_over_screen()

def render_game_over_screen():
    print('meant to game over')
    global running
    running = False
    WINDOW.fill(grey)
    WINDOW.blit(blackGradientScreen, (0,0))
    pygame.display.update()

render_game_start_page()