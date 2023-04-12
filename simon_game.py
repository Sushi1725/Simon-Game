import pygame
import sys
import random
import time
from pygame.locals import *

# Game Setup
FPS = 60
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
pygame.mixer.init()

# rgb values of colours used
white = ('#FFFFFF')
grey = ('#131313')
black = ('#000000')

# load all the images
logo = pygame.image.load('./Assets/simon_logo.png')
mainPageImageScaled = pygame.transform.scale(logo, (450, 450))
startButtonNormal = pygame.image.load('./Assets/main_menu_page_images/start_game_image.png')
startButtonPressed = pygame.image.load('./Assets/main_menu_page_images/start_game_image_2.png')
settings = pygame.image.load('./Assets/main_menu_page_images/gear_cog.png') # 547, 600
settingsScaled = pygame.transform.scale(settings, (64,70))
settingsScaled2 = pygame.transform.scale(settings, (109.4, 120))
leaderboard = pygame.image.load('./Assets/main_menu_page_images/victory_cup.png') # 50 130
leaderboardScaled = pygame.transform.scale(leaderboard, (68, 68))
bgGreen = pygame.image.load('./Assets/main_menu_page_images/bg_green.png')
bgRed = pygame.image.load('./Assets/main_menu_page_images/bg_red.png')
bgYellow = pygame.image.load('./Assets/main_menu_page_images/bg_yellow.png')
bgBlue = pygame.image.load('./Assets/main_menu_page_images/bg_blue.png')

heartImageFull = pygame.image.load('./Assets/game_images/heart_full.png')
heartImageFullScaled = pygame.transform.scale(heartImageFull, (36, 36))
heartImageEmpty = pygame.image.load('./Assets/game_images/heart_empty.png')
heartImageEmptyScaled = pygame.transform.scale(heartImageEmpty, (36, 36))

blueLight = pygame.image.load('./Assets/game_images/blue_light.png')
blueLightScaled = pygame.transform.scale(blueLight, (225, 225))
blue = pygame.image.load('./Assets/game_images/blue.png')
blueScaled = pygame.transform.scale(blue, (225, 225))
greenLight = pygame.image.load('./Assets/game_images/green_light.png')
greenLightScaled = pygame.transform.scale(greenLight, (225, 225))
green = pygame.image.load('./Assets/game_images/green.png')
greenScaled = pygame.transform.scale(green, (225, 225))
redLight = pygame.image.load('./Assets/game_images/red_light.png')
redLightScaled = pygame.transform.scale(redLight, (225, 225))
red = pygame.image.load('./Assets/game_images/red.png')
redScaled = pygame.transform.scale(red, (225, 225))
yellowLight = pygame.image.load('./Assets/game_images/yellow_light.png')
yellowLightScaled = pygame.transform.scale(yellowLight, (225, 225))
yellow = pygame.image.load('./Assets/game_images/yellow.png')
yellowScaled = pygame.transform.scale(yellow, (225, 225))

blackGradientScreen = pygame.image.load('./Assets/main_menu_page_images/black_bg.png')
bg = pygame.Rect(50, 100, 700, 450)

soundOn = pygame.image.load('./Assets/setting_images/sound_on.png')
soundOnScaled = pygame.transform.scale(soundOn, (54, 54))
soundOff = pygame.image.load('./Assets/setting_images/sound_off.png')
soundOffScaled = pygame.transform.scale(soundOff, (87, 87))
soundSlider = pygame.image.load('./Assets/setting_images/slider.png')
soundSliderScaled = pygame.transform.scale(soundSlider, (26, 26))

homeButton = pygame.image.load('./Assets/end_game_images/home_button.png')
homeButtonScaled = pygame.transform.scale(homeButton, (100, 100))
restartButton = pygame.image.load('./Assets/end_game_images/restart_button.png')
restartButtonScaled = pygame.transform.scale(restartButton, (95, 95))

nextPage = pygame.image.load('./Assets/info_images/page_left.png')
nextPageScaled = pygame.transform.scale(nextPage, (51, 51))
backPage = pygame.image.load('./Assets/info_images/page_right.png')
backPageScaled = pygame.transform.scale(backPage, (51, 51))

# load all the fonts
GAMEPLAY_FONT = './Assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf'
gameFontStart = pygame.font.Font(GAMEPLAY_FONT, 50) # size 50 font
gameFont = pygame.font.Font(GAMEPLAY_FONT, 20) # size 20 font
gameFontSubtitle = pygame.font.Font(GAMEPLAY_FONT, 24) # size 24 font
gameFontEnd = pygame.font.Font(GAMEPLAY_FONT, 40) # size 40 font
gameFontCred = pygame.font.Font(GAMEPLAY_FONT, 30) # size 30 font

# initialise the window of the game
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # creates the window
pygame.display.set_caption('Simon: The Game') # sets the name of the window
pygame.display.set_icon(logo) # sets the window's logo to the image

# variables
score = 0 # score number
volume = 1.0
life = 3
lifeStore = life
running = True
pattern = [] # store array of previous colours
timeDelay = 500 # milliseconds
playerPattern = [] # store array of player guesses (used to compare)
heart1 = heartImageFullScaled
heart2 = heartImageFullScaled
heart3 = heartImageFullScaled
sliderX = 692
sliderY = 215
pageRules = 0

################
# Game Classes #
################

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
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    
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
        heartAnimation.image = heartImageEmpty
        pygame.time.delay(80)
        heartAnimation.image = heartImageFull
        pygame.time.delay(80)
        heartAnimation.image = heartImageEmpty
        pygame.time.delay(80)
        heartAnimation.image = heartImageFull
        pygame.time.delay(80)
        heartAnimation.image = heartImageEmpty
        pygame.time.delay(80)
        heartAnimation.image = heartImageFull
        pygame.time.delay(80)
        heartAnimation.image = heartImageEmpty

##################
# Game Functions #
##################

def render_game_start_page(): # main screen page
    waiting = True
    global score
    score = 0
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
                
                if 710 <= x <= 774 and 30 <= y <= 100: # for the settings button
                    # if the click is within a certain range
                    render_settings_screen()
                elif 712 <= x <= 780 and 510 <= y <= 578:
                    render_leaderboard_screen()
                    # render_save_score_screen()
    
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
        WINDOW.blit(leaderboardScaled, (WINDOW_WIDTH-88, 510))
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
    
        pygame.time.Clock().tick(FPS)
    
    while running:
        random_pattern()
        show_pattern()
        store_player_guess()
    while not running:
        render_game_over_screen()

def render_game_simon_play_page(yellowColour = yellowScaled, blueColour = blueScaled, greenColour = greenScaled, redColour = redScaled):
    for event in pygame.event.get() :
        if event.type == QUIT :
            quit()
    
    # refresh display
    WINDOW.fill(grey)
    
    # draw elements
    global score
    score_text = gameFont.render('Score: ' + str(score), True, white)
    WINDOW.blit(score_text, (50, 50))
    # WINDOW.blit((gameFont.render('Score: 0', True, white)), (50, 50))
    
    WINDOW.blit(heart1, (WINDOW_WIDTH-36-36-36-5-5-50, 50))
    WINDOW.blit(heart2, (WINDOW_WIDTH-36-36-5-50, 50))
    WINDOW.blit(heart3, (WINDOW_WIDTH-36-50, 50))
    WINDOW.blit(yellowColour, (175, 300))
    WINDOW.blit(blueColour, (400, 300))
    WINDOW.blit(greenColour, (400, 75))
    WINDOW.blit(redColour, (175, 75))
    pygame.display.update()

def random_pattern():
    pattern.append(random.randint(1, 4))

def quit():
    global running
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
            render_game_simon_play_page(redColour = redLightScaled) # change it into light mode
            pygame.mixer.music.load('./Assets/sounds/red_a.wav')
            pygame.mixer.music.play()
            pygame.time.delay(timeDelay) # current set time delay (faster as the game progresses)
            render_game_simon_play_page() # move it back into the "all dark" state
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        elif x == 2: # 2 = green
            render_game_simon_play_page(greenColour = greenLightScaled) # change it into light mode
            pygame.mixer.music.load('./Assets/sounds/green_e-lower.wav')
            pygame.mixer.music.play()
            pygame.time.delay(timeDelay) # current set time delay (faster as the game progresses)
            render_game_simon_play_page() # move it back into the "all dark" state
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        elif x == 3: # 3 = yellow
            render_game_simon_play_page(yellowColour = yellowLightScaled) # change it into light mode
            pygame.mixer.music.load('./Assets/sounds/yellow_c-sharp.wav')
            pygame.mixer.music.play()
            pygame.time.delay(timeDelay) # current set time delay (faster as the game progresses)
            render_game_simon_play_page() # move it back into the "all dark" state
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        elif x == 4: # 4 = blue
            render_game_simon_play_page(blueColour = blueLightScaled) # change it into light mode
            pygame.mixer.music.load('./Assets/sounds/blue_e-upper.wav')
            pygame.mixer.music.play()
            pygame.time.delay(timeDelay) # current set time delay (faster as the game progresses)
            render_game_simon_play_page() # move it back into the "all dark" state
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        print(pattern)
        pygame.time.delay(timeDelay)

def store_player_guess():
    print("now in store player guess")
    # 1 = red
    # 2 = green
    # 3 = yellow
    # 4 = blue

    global playerPattern
    playerPattern = []
    global pattern
    global lifeStore
    global life
    global score
    
    clickBlueScaled = pygame.transform.scale(blue, (225, 225)).convert_alpha() # optimises the checking the button
    clickGreenScaled = pygame.transform.scale(green, (225, 225)).convert_alpha()
    clickRedScaled = pygame.transform.scale(red, (225, 225)).convert_alpha()
    clickYellowScaled = pygame.transform.scale(yellow, (225, 225)).convert_alpha()
    blueScaledPos = (400, 300)
    greenScaledPos = (400, 75)
    redScaledPos = (175, 75)
    yellowScaledPos = (175, 300)
    
    while len(playerPattern) < len(pattern): # so that we check each item of the pattern
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                try: # only work if the click isnt in a transparent area
                    mask = pygame.mask.from_surface(clickRedScaled)
                    if mask.get_at((event.pos[0]-redScaledPos[0], event.pos[1]-redScaledPos[1])):
                        render_game_simon_play_page(redColour = redLightScaled) # change it into light mode
                        pygame.mixer.music.load('./Assets/sounds/red_a.wav') # load the sound
                        pygame.mixer.music.play() # play the sound
                        pygame.time.delay(timeDelay) # wait
                        render_game_simon_play_page() # turn off the light colour
                        pygame.mixer.music.stop() # stop the sound
                        pygame.mixer.music.unload() # unload the sound
                        playerPattern.append(1) # add the guess to the end of the array
                        check_pattern(playerPattern) # compare it
                        if life != lifeStore:
                            break
                except IndexError:  # if the click is in a transparent area, dont worry about it
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                try: # only work if the click isnt in a transparent area
                    mask = pygame.mask.from_surface(clickGreenScaled)
                    if mask.get_at((event.pos[0]-greenScaledPos[0], event.pos[1]-greenScaledPos[1])):
                        render_game_simon_play_page(greenColour = greenLightScaled) # change it into light mode
                        pygame.mixer.music.load('./Assets/sounds/green_e-lower.wav')
                        pygame.mixer.music.play()
                        pygame.time.delay(timeDelay) # wait
                        render_game_simon_play_page() # turn off the light colour
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        playerPattern.append(2) # add it to the end of the array
                        check_pattern(playerPattern)
                        if life != lifeStore:
                            break
                except IndexError:  # if the click is in a transparent area, dont worry about it
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                try: # only work if the click isnt in a transparent area
                    mask = pygame.mask.from_surface(clickYellowScaled)
                    if mask.get_at((event.pos[0]-yellowScaledPos[0], event.pos[1]-yellowScaledPos[1])):
                        render_game_simon_play_page(yellowColour = yellowLightScaled) # change it into light mode
                        pygame.mixer.music.load('./Assets/sounds/yellow_c-sharp.wav')
                        pygame.mixer.music.play()
                        pygame.time.delay(timeDelay) # wait
                        render_game_simon_play_page() # turn off the light colour
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        playerPattern.append(3) # add it to the end of the array
                        check_pattern(playerPattern)
                        if life != lifeStore:
                            break
                except IndexError:  # if the click is in a transparent area, dont worry about it
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                try: # only work if the click isnt in a transparent area
                    mask = pygame.mask.from_surface(clickBlueScaled) # mask makes it so that the translucent part of the image cannot be clicked
                    if mask.get_at((event.pos[0]-blueScaledPos[0], event.pos[1]-blueScaledPos[1])):
                        render_game_simon_play_page(blueColour = blueLightScaled) # change it into light mode
                        pygame.mixer.music.load('./Assets/sounds/blue_e-upper.wav')
                        pygame.mixer.music.play()
                        pygame.time.delay(timeDelay) # wait
                        render_game_simon_play_page() # turn off the light colour
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        playerPattern.append(4) # add it to the end of the array
                        check_pattern(playerPattern)
                        if life != lifeStore:
                            break
                except IndexError:  # if the click is in a transparent area, dont worry about it
                    pass
        if life != lifeStore:
            break
    if len(playerPattern) == len(pattern) and life == lifeStore:
        score = score + 1
    lifeStore = life

def life_loss():
    pygame.mixer.music.load('./Assets/sounds/beep_beep_beep.wav')
    pygame.mixer.music.play()
    render_game_simon_play_page(blueColour = blueLightScaled, yellowColour = yellowLightScaled, greenColour = greenLightScaled, redColour = redLightScaled)
    pygame.time.delay(500)
    render_game_simon_play_page()
    pygame.time.delay(250)
    render_game_simon_play_page(blueColour = blueLightScaled, yellowColour = yellowLightScaled, greenColour = greenLightScaled, redColour = redLightScaled)
    pygame.time.delay(500)
    render_game_simon_play_page()
    pygame.time.delay(250)
    render_game_simon_play_page(blueColour = blueLightScaled, yellowColour = yellowLightScaled, greenColour = greenLightScaled, redColour = redLightScaled)
    pygame.time.delay(500)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    render_game_simon_play_page()

def check_pattern(playerPattern):  # only works after first guess/ if first guess is wrong, doesnt check
    if playerPattern != pattern[:len(playerPattern)]: # if the player's guess is not the same as the [corresponding index] of the pattern
        global life
        life = life - 1
        
        global heart1
        global heart2
        global heart3
        
        if life == 2:
            heart1 = heartImageEmptyScaled
            WINDOW.blit(heart1, (WINDOW_WIDTH-36-36-36-5-5-50, 50))
            pygame.display.update()
            life_loss()
        if life == 1:
            heart1 = heartImageEmptyScaled
            heart2 = heartImageEmptyScaled
            WINDOW.blit(heart1, (WINDOW_WIDTH-36-36-36-5-5-50, 50))
            WINDOW.blit(heart2, (WINDOW_WIDTH-36-36-5-50, 50))
            pygame.display.update()
            life_loss()
        if life == 0:
            heart1 = heartImageEmptyScaled
            heart2 = heartImageEmptyScaled
            heart3 = heartImageEmptyScaled
            WINDOW.blit(heart1, (WINDOW_WIDTH-36-36-36-5-5-50, 50))
            WINDOW.blit(heart2, (WINDOW_WIDTH-36-36-5-50, 50))
            WINDOW.blit(heart3, (WINDOW_WIDTH-36-50, 50))
            pygame.display.update()
            render_game_over_screen()

def render_settings_screen():
    waiting = True
    global volume
    global sliderX
    global sliderY
    sound = soundOnScaled
    soundLocation = (100, 200)
    switching = 1
    yMin = 215
    yMax = 241
    while waiting:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # mute button
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                
                yMin = 215
                yMax = 241

                if 100 <= x <= 154 and 200 <= y <= 254:
                    if switching == 1:
                        sound = soundOffScaled
                        soundLocation = (85, 185)
                        pygame.mixer.music.set_volume(0)
                        print("volume now 0?")
                        switching = 2
                        break
                    if switching == 2:
                        sound = soundOnScaled
                        soundLocation = (100, 200)
                        pygame.mixer.music.set_volume(volume)
                        switching = 1
                        break
                elif 180 <= x <= 420 and 450 <= y <= 540:
                    waiting = False
                elif 580 <= x <= 620 and 450 <= y <= 540:
                    render_credits_screen()
                elif 720 <= x <= 800 and 450 <= y <= 540:
                    render_game_rules_screen()
            if event.type == pygame.MOUSEMOTION and event.buttons == (1, 0, 0): # slider
                pos = pygame.mouse.get_pos() # if the cursor is moving and left click is being pressed
                x = pos[0]
                y = pos[1]
                
                if x < 180 or x > 705 or y < yMin and 180 <= x <= 705 or y > yMax and 180 <= x <= 705:
                    print('ok')
                else:
                    if event.rel[0] != 0:
                        yMin = 0
                        yMax = 600
                        sliderX = x - 13
                        if sliderX > (705): # constrict the location of the slider to the most right of the slider line
                            sliderX = (705-13)
                        if sliderX < (178): # constrict the location of the slider to the most left of the slider line
                            sliderX = (178)
            if volume <= 0:
                sound = soundOffScaled
                soundLocation = (85, 185)
            else:
                sound = soundOnScaled
                soundLocation = (100, 200)
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if 180 <= x <= 705 and 215 <= y <= 241:
                    sliderX = x - 13

        WINDOW.fill(grey)
        WINDOW.blit(blackGradientScreen, (0,0))
        thig = pygame.Rect(180, 450, 100, 100)
        temp = pygame.Rect(580, 450, 40, 90)
        temp1 = pygame.Rect(720, 450, 80, 90)
        pygame.draw.rect(WINDOW, black, bg)
        pygame.draw.rect(WINDOW, white, bg, 2)
        pygame.draw.rect(WINDOW, white, thig)
        pygame.draw.rect(WINDOW, white, temp)
        pygame.draw.rect(WINDOW, white, temp1)
        WINDOW.blit(settingsScaled2, (345.3, 50))
        WINDOW.blit(sound, soundLocation)
        pygame.draw.line(WINDOW, white, (180, 227), (705, 227), 2) # volume goes up to 525
        WINDOW.blit(soundSliderScaled, (sliderX, 215)) # make it so that the x location is proportional to the volume
        volume = 2*((sliderX-180) / (10**len(str(sliderX)))) # the location of the slider - 180 divede by 10 to the power of the length (to get between 0.0-1.0)
        pygame.mixer.music.set_volume(volume) # sliderScaled = (26, 26)
        print(volume)
        pygame.display.update() #^^^ 177 cause 1 empty *2 + 1

def render_game_info_screen():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 180 <= x <= 234 and 300 <= y <= 354:
                    render_game_start_page()
                elif 180 <= x <= 420 and 450 <= y <= 540:
                    quit()
        WINDOW.fill(grey)
        WINDOW.blit(blackGradientScreen, (0,0))
        pygame.draw.rect(WINDOW, black, bg)
        pygame.draw.rect(WINDOW, white, bg, 2)
        pygame.display.update()

def render_credits_screen():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 600 <= x <= 700 and 400 <= y <= 500:
                    render_game_start_page()
        WINDOW.fill(grey)
        WINDOW.blit(blackGradientScreen, (0,0))
        pygame.draw.rect(WINDOW, black, bg)
        pygame.draw.rect(WINDOW, white, bg, 2)
        credBg = pygame.Rect(200, 50, 400, 100)
        pygame.draw.rect(WINDOW, black, credBg)
        pygame.draw.rect(WINDOW, white, credBg, 2)
        WINDOW.blit(homeButtonScaled, (600, 400))
        credText = gameFontStart.render('Credits', True, white)
        WINDOW.blit(credText, (225, 75))
        ben = gameFontCred.render('Benjamin See', True, white)
        WINDOW.blit(ben, (150, 200))
        shou = gameFontCred.render('Shou-Yi Lai', True, white)
        WINDOW.blit(shou, (150, 300))
        tanya = gameFontCred.render('Tanya W.', True, white)
        WINDOW.blit(tanya, (150, 400))
        pygame.display.update()

def render_game_rules_screen():
    global pageRules
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 75 <= x <= 126 and 299.5 <= y <= 350.5:
                    pageRules = pageRules + 1
                if 675 <= x <= 726 and 299.5 <= y <= 350.5:
                    pageRules = pageRules - 1
                if 225 <= x <= 581 and 475 <= y <= 501:
                    render_game_start_page()
        WINDOW.fill(grey)
        WINDOW.blit(blackGradientScreen, (0,0))
        pygame.draw.rect(WINDOW, black, bg)
        pygame.draw.rect(WINDOW, white, bg, 2)
        titleText = gameFontEnd.render('Game Rules', True, white)
        WINDOW.blit(titleText, (205, 35))
        goHomeText = gameFontCred.render('Back to Game', True, white)
        WINDOW.blit(goHomeText, (225, 475))
        WINDOW.blit(nextPageScaled, (75, 299.5))
        WINDOW.blit(backPageScaled, (675, 299.5))
        pygame.display.update()

def render_game_over_screen():
    # reset the game variables
    global score
    storeScore = score
    score = 0
    global life
    life = 3
    global heart1
    global heart2
    global heart3
    heart1 = heartImageFullScaled
    heart2 = heartImageFullScaled
    heart3 = heartImageFullScaled
    global lifeStore
    lifeStore = life
    global running
    running = True
    global pattern
    pattern = [] # store array of previous colours
    global timeDelay
    timeDelay = 500 # milliseconds
    global playerPattern
    playerPattern = [] # store array of player guesses (used to compare)
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 279 <= x <= 379 and 300 <= y <= 400:
                    render_game_start_page()
                elif 421 <= x <= 616 and 300 <= y <= 395:
                    waiting = False
                    lifeStore = 1
        WINDOW.fill(grey)
        WINDOW.blit(blackGradientScreen, (0,0))
        gameOverText = gameFontEnd.render('Game Over', True, white) # write the words
        WINDOW.blit(gameOverText, (223, 200))
        gameOverText = gameFont.render('Score: ' + str(storeScore), True, white) # write the words
        WINDOW.blit(gameOverText, (50, 50))
        WINDOW.blit(homeButtonScaled, (279, 300))
        WINDOW.blit(restartButtonScaled, (421, 300))
        pygame.display.update()


    # # The 'a' means append (as opposed to 'w' for write which will clear the file before writing.)
    # highScores = open('high_scores.txt', 'a')
    
    # # This is called a priming read
    # name = input('Player name : ')
    # score = int(input('Player score : '))
    
    # while name != 'end' :
    #     highScores.write(f'{name},{score}\n')
    #     name = input('Player name : ')
    #     score = int(input('Player score : '))

    # print('High Scores saved to file.')
    # highScores.close()
    # #Reading from a file
    # #Next we will access that file and print the results.
    # scores = open('high_scores.txt')
	# # line = scores.readline().strip()

	# # while line != '':
    #     # fields = line.split(',')
    #     # print (f'Player {fields[0]} got a score of : {fields[1]}')
    #     # line = scores.readline().strip()

def render_save_score_screen():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 650 <= x <= 750 and 450 <= y <= 550:
                    render_game_over_screen()
        WINDOW.fill(grey)
        WINDOW.blit(blackGradientScreen, (0,0))
        pygame.draw.rect(WINDOW, black, bg)
        pygame.draw.rect(WINDOW, white, bg, 2)
        saveBg = pygame.Rect(300, 25, 200, 100)
        pygame.draw.rect(WINDOW, black, saveBg)
        pygame.draw.rect(WINDOW, white, saveBg, 2)
        titleText = gameFontEnd.render('Save', True, white)
        WINDOW.blit(titleText, ((WINDOW_WIDTH-titleText.get_width())/2, 55))
        subtitleText = gameFontSubtitle.render('Rank   Name   Score', True, white)
        WINDOW.blit(subtitleText, ((WINDOW_WIDTH-subtitleText.get_width())/2, 150))
        WINDOW.blit(homeButtonScaled, (650, 450))
        
        test1 = gameFont.render('1ST', True, white)
        WINDOW.blit(test1, (96+((WINDOW_WIDTH-subtitleText.get_width())/2)-test1.get_width(), 190))
        test2 = gameFont.render('SYL', True, white)
        WINDOW.blit(test2, (264+((WINDOW_WIDTH-subtitleText.get_width())/2)-test2.get_width(), 190))
        test3 = gameFont.render('17', True, white)
        WINDOW.blit(test3, (456+((WINDOW_WIDTH-subtitleText.get_width())/2)-test3.get_width(), 190))
        
        pygame.display.update()


def render_leaderboard_screen():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 75 <= x <= 126 and 299.5 <= y <= 350.5:
                    pageRules = pageRules + 1
                if 675 <= x <= 726 and 299.5 <= y <= 350.5:
                    pageRules = pageRules - 1
                if 650 <= x <= 750 and 450 <= y <= 550:
                    render_game_start_page()
        WINDOW.fill(grey)
        WINDOW.blit(blackGradientScreen, (0,0))
        pygame.draw.rect(WINDOW, black, bg)
        pygame.draw.rect(WINDOW, white, bg, 2)
        leaderboardBg = pygame.Rect(100, 25, 600, 100)
        pygame.draw.rect(WINDOW, black, leaderboardBg)
        pygame.draw.rect(WINDOW, white, leaderboardBg, 2)
        titleText = gameFontEnd.render('High Scores', True, white)
        WINDOW.blit(titleText, (185, 55))
        subtitleText = gameFontSubtitle.render('Rank   Name   Score', True, white)
        WINDOW.blit(subtitleText, ((WINDOW_WIDTH-subtitleText.get_width())/2, 150))
        WINDOW.blit(homeButtonScaled, (650, 450))
        WINDOW.blit(nextPageScaled, (75, 299.5))
        WINDOW.blit(backPageScaled, (675, 299.5))
        
        test1 = gameFont.render('1ST', True, white)
        WINDOW.blit(test1, (96+((WINDOW_WIDTH-subtitleText.get_width())/2)-test1.get_width(), 190))
        test2 = gameFont.render('SYL', True, white)
        WINDOW.blit(test2, (264+((WINDOW_WIDTH-subtitleText.get_width())/2)-test2.get_width(), 190))
        test3 = gameFont.render('17', True, white)
        WINDOW.blit(test3, (456+((WINDOW_WIDTH-subtitleText.get_width())/2)-test3.get_width(), 190))
        
        pygame.display.update()

render_game_start_page()