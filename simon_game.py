import pygame
import sys
import random
from pygame.locals import *
import csv

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
life = 3
lifeStore = life
running = True
pattern = [] # store array of previous colours
timeDelay = 500 # milliseconds
playerPattern = [] # store array of player guesses (used to compare)
heart1 = heartImageFullScaled
heart2 = heartImageFullScaled
heart3 = heartImageFullScaled
initial = []
volume = 1.0

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
    
    sortedFile = []
    scoreFile = open("high_scores.csv")
    fileReader = csv.reader(scoreFile, delimiter=",")
    for Score, Name in fileReader:
        sortedFile = sorted(fileReader, key=lambda row: int(row[0]), reverse=True)
        print(sortedFile)
    scoreFile.close()

    scoreFile2 = open("high_scores.csv", "w", newline='')
    fileWriter = csv.writer(scoreFile2, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
    txtFile = open("high_scores.txt", "w", newline='')
    txtFileWriter = csv.writer(txtFile, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
    fileWriter.writerow(['Score', 'Name'])
    for i, j in enumerate(sortedFile):
        fileWriter.writerow(sortedFile[i])
        txtFileWriter.writerow(sortedFile[i])
    scoreFile2.close()
    txtFile.close()
    
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
            logoBob = logoBob + 0.5 # move it down
        else:
            logoBob = logoBob - 0.5 # move it up
    
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
    
    timeDelay = 500 - 100 * int(len(pattern) / 5) # changing it to an integer makes it round down if is float
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
        pygame.mixer.music.load('./Assets/sounds/ding.wav')
        pygame.mixer.music.play()
        pygame.time.delay(1500) # wait
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
            render_save_score_screen()

def render_settings_screen():
    waiting = True
    global volume
    volume = 1.0
    sliderX = 692
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
                elif 360 <= x <= 440 and 475 <= y <= 515:
                    waiting = False
                elif 299 <= x <= 499 and 365 <= y <= 425:
                    render_credits_screen()
                elif 349 <= x <= 449 and 275 <= y <= 335:
                    render_game_rules_screen()
            if event.type == pygame.MOUSEMOTION and event.buttons == (1, 0, 0): # slider
                pos = pygame.mouse.get_pos() # if the cursor is moving and left click is being pressed
                x = pos[0]
                y = pos[1]
                
                if x < 180 or x > 705 or y < yMin and 180 <= x <= 705 or y > yMax and 180 <= x <= 705:
                    print('ok')
                    break #### TESTING ###### NOT SURE IF WORKING
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
        credBox = pygame.Rect(299, 365, 200, 60)
        infoBox = pygame.Rect(349, 275, 100, 60)
        pygame.draw.rect(WINDOW, black, bg)
        pygame.draw.rect(WINDOW, white, bg, 2)
        pygame.draw.rect(WINDOW, black, credBox)
        pygame.draw.rect(WINDOW, white, credBox, 2)
        pygame.draw.rect(WINDOW, black, infoBox)
        pygame.draw.rect(WINDOW, white, infoBox, 2)
        okText = gameFontEnd.render("OK", True, white)
        WINDOW.blit(okText, ((WINDOW_WIDTH-okText.get_width())/2, 475))
        infoText = gameFontSubtitle.render("i", True, white)
        WINDOW.blit(infoText, ((WINDOW_WIDTH-infoText.get_width())/2, 295))
        credText = gameFontSubtitle.render("Credits", True, white)
        WINDOW.blit(credText, ((WINDOW_WIDTH-credText.get_width())/2, 385))
        WINDOW.blit(settingsScaled2, (345.3, 50))
        WINDOW.blit(sound, soundLocation)
        pygame.draw.line(WINDOW, white, (180, 227), (705, 227), 2) # volume goes up to 525
        WINDOW.blit(soundSliderScaled, (sliderX, 215)) # make it so that the x location is proportional to the volume
        volume = 2*((sliderX-180) / (10**len(str(sliderX)))) # the location of the slider - 180 divede by 10 to the power of the length (to get between 0.0-1.0)
        pygame.mixer.music.set_volume(volume) # sliderScaled = (26, 26)
        print(volume)
        pygame.display.update() #^^^ 177 cause 1 empty *2 + 1

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
    waiting = True
    textToShowNum = 1
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 75 <= x <= 126 and 299.5 <= y <= 350.5:
                    textToShowNum = textToShowNum - 1
                    if textToShowNum < 1:
                        textToShowNum = 1
                if 675 <= x <= 726 and 299.5 <= y <= 350.5:
                    textToShowNum = textToShowNum + 1
                    if textToShowNum > 3:
                        textToShowNum = 3
                if 225 <= x <= 581 and 475 <= y <= 501 and textToShowNum == 3:
                    render_game_start_page()
        
        WINDOW.fill(grey)
        WINDOW.blit(blackGradientScreen, (0,0))
        pygame.draw.rect(WINDOW, black, bg)
        pygame.draw.rect(WINDOW, white, bg, 2)
        titleText = gameFontEnd.render('Game Rules', True, white)
        WINDOW.blit(titleText, (205, 35))
        WINDOW.blit(nextPageScaled, (75, 299.5))
        WINDOW.blit(backPageScaled, (675, 299.5))
        pageNum = gameFont.render(str(textToShowNum) + "/3", True, white)
        WINDOW.blit(pageNum, (WINDOW_WIDTH-pageNum.get_width()-70, 515))
        if textToShowNum == 1:
            cover = pygame.Rect(75, 299.5, 51, 51)
            pygame.draw.rect(WINDOW, black, cover)
            page1line1 = gameFont.render("The following game is a", True, white)
            WINDOW.blit(page1line1, (int(((WINDOW_WIDTH-page1line1.get_width())/2)), 250))
            page1line2 = gameFont.render("python recreation of the", True, white)
            WINDOW.blit(page1line2, (int(((WINDOW_WIDTH-page1line2.get_width())/2)), 275))
            page1line3 = gameFont.render("1978 children's toy 'Simon'", True, white)
            WINDOW.blit(page1line3, (int(((WINDOW_WIDTH-page1line3.get_width())/2)), 300))
            page1line4 = gameFont.render("by Ralph H. Baer and", True, white)
            WINDOW.blit(page1line4, (int(((WINDOW_WIDTH-page1line4.get_width())/2)), 325))
            page1line5 = gameFont.render("Howard J. Morrison", True, white)
            WINDOW.blit(page1line5, (int(((WINDOW_WIDTH-page1line5.get_width())/2)), 350))
            
        elif textToShowNum == 2:
            page2line1 = gameFont.render("The game has four coloured", True, white)
            WINDOW.blit(page2line1, (140, 175))
            page2line2 = gameFont.render("buttons where each button", True, white)
            WINDOW.blit(page2line2, (140, 200))
            page2line3 = gameFont.render("produces a unique tone when", True, white)
            WINDOW.blit(page2line3, (140, 225))
            page2line4 = gameFont.render("it is pressed or activated.", True, white)
            WINDOW.blit(page2line4, (140, 250))
            page2line5 = gameFont.render("One round in the game", True, white)
            WINDOW.blit(page2line5, (140, 275))
            page2line6 = gameFont.render("consists of one or more", True, white)
            WINDOW.blit(page2line6, (140, 300))
            page2line7 = gameFont.render("colours lighting up and", True, white)
            WINDOW.blit(page2line7, (140, 325))
            page2line8 = gameFont.render("sounding in a random order.", True, white)
            WINDOW.blit(page2line8, (140, 350))
            page2line9 = gameFont.render("After, the player must", True, white)
            WINDOW.blit(page2line9, (140, 375))
            page2line10 = gameFont.render("reproduce that pattern by", True, white)
            WINDOW.blit(page2line10, (140, 400))
            page2line11 = gameFont.render("pressing the buttons.", True, white)
            WINDOW.blit(page2line11, (140, 425))
            page2line12 = gameFont.render("As the game progresses,", True, white)
            WINDOW.blit(page2line12, (140, 450))
        elif textToShowNum == 3:
            cover = pygame.Rect(675, 299.5, 51, 51)
            pygame.draw.rect(WINDOW, black, cover)
            page3line1 = gameFont.render("the number of buttons", True, white)
            WINDOW.blit(page3line1, (140, 150))
            page3line2 = gameFont.render("that needs to be pressed", True, white)
            WINDOW.blit(page3line2, (140, 175))
            page3line3 = gameFont.render("increases. The speed which", True, white)
            WINDOW.blit(page3line3, (140, 200))
            page3line4 = gameFont.render("the colour pattern is", True, white)
            WINDOW.blit(page3line4, (140, 225))
            page3line5 = gameFont.render("played at also gets faster", True, white)
            WINDOW.blit(page3line5, (140, 250))
            page3line6 = gameFont.render("every 5 turns. You are", True, white)
            WINDOW.blit(page3line6, (140, 275))
            page3line7 = gameFont.render("given 3 lives. Your goal", True, white)
            WINDOW.blit(page3line7, (140, 300))
            page3line8 = gameFont.render("is to get the highest", True, white)
            WINDOW.blit(page3line8, (140, 325))
            page3line9 = gameFont.render("score in those 3 lives to", True, white)
            WINDOW.blit(page3line9, (140, 350))
            page3line10 = gameFont.render("get onto the leaderboard.", True, white)
            WINDOW.blit(page3line10, (140, 375))
            page3line11 = gameFont.render("", True, white)
            WINDOW.blit(page3line11, (140, 400))
            page3line12 = gameFont.render("Good Luck :)", True, white)
            WINDOW.blit(page3line12, (int((WINDOW_WIDTH-page3line12.get_width())/2), 425))
            goHomeText = gameFontCred.render('Back to Game', True, white)
            WINDOW.blit(goHomeText, (225, 475))
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

def render_save_score_screen():
    red = ('#FF0000')
    row1 = ['A' ,'B' ,'C' ,'D' ,'E' ,'F' ,'G' ,'H' ,'I' ,'J']
    row1X = [172, 220, 268, 316, 364, 412, 460, 508, 556, 604]
    row1Y = 160
    row2 = ['K' ,'L' ,'M' ,'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T']
    row2X = [172, 220, 268, 316, 364, 412, 460, 508, 556, 604]
    row2Y = 200
    row3 = ['U' ,'V' ,'W' ,'X' ,'Y' ,'Z']
    row3X = [172, 220, 268, 316, 364, 412, 460, 508]
    row3Y = 240
    global initial
    initial = []
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = [0, 1, 2, 3, 4, 5]
    colour = black
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 625 <= x <= 705 and 475 <= y <= 515:
                    if len(initial) == 3:
                        update_file()
                        render_game_over_screen()
                    else:
                        print('Please Choose 3 Letters')
                        colour = white
                for e in nums:
                    if row1X[e] <= x <= row1X[e]+24 and row1Y <= y <= row1Y+24:
                        if len(initial) < 3:
                            initial.append(row1[e])
                            print(initial)
                            colour = black
                for f in nums:
                    if row2X[f] <= x <= row2X[f]+24 and row2Y <= y <= row2Y+24:
                        if len(initial) < 3:
                            initial.append(row2[f])
                            print(initial)
                            colour = black
                for g in num:
                    if row3X[g] <= x <= row3X[g]+24 and row3Y <= y <= row3Y+24:
                        if len(initial) < 3:
                            initial.append(row3[g])
                            print(initial)
                            colour = black
                if 556 <= x <= 556+24*3 and row3Y <= y <= row3Y+24:
                    try:
                        initial.pop(-1)
                        colour = black
                    except IndexError:
                        colour = black
                        pass
                if 484 <= x <= 484+24 and row3Y <= y <= row3Y+24:
                    if len(initial) < 3:
                        initial.append('-')
                        print(initial)
                        colour = black
        WINDOW.fill(grey)
        WINDOW.blit(blackGradientScreen, (0,0))
        pygame.draw.rect(WINDOW, black, bg)
        pygame.draw.rect(WINDOW, white, bg, 2)
        saveBg = pygame.Rect(300, 25, 200, 100)
        pygame.draw.rect(WINDOW, black, saveBg)
        pygame.draw.rect(WINDOW, white, saveBg, 2)
        titleText = gameFontEnd.render('Save', True, white)
        WINDOW.blit(titleText, ((WINDOW_WIDTH-titleText.get_width())/2, 55))
        okText = gameFontEnd.render('OK', True, white)
        WINDOW.blit(okText, (625, 475))
        for i, j in zip(row1, row1X):
            WINDOW.blit(gameFontSubtitle.render(i, True, white), (j, row1Y))
            if gameFontSubtitle.render(i, True, white).get_rect(topleft=(j, row1Y)).collidepoint(pygame.mouse.get_pos()):
                pygame.draw.line(WINDOW, red, (j-2, row1Y+24), (j+24, row1Y+24), 4)
                # pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            # else:
                # pygame.mouse.set_cursor()
        for a, b in zip(row2, row2X):
            WINDOW.blit(gameFontSubtitle.render(a, True, white), (b, row2Y))
            if gameFontSubtitle.render(a, True, white).get_rect(topleft=(b, row2Y)).collidepoint(pygame.mouse.get_pos()):
                pygame.draw.line(WINDOW, red, (b-2, row2Y+24), (b+24, row2Y+24), 4)
                # pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        for c, d in zip(row3, row3X):
            WINDOW.blit(gameFontSubtitle.render(c, True, white), (d, row3Y))
            if gameFontSubtitle.render(c, True, white).get_rect(topleft=(d, row3Y)).collidepoint(pygame.mouse.get_pos()):
                pygame.draw.line(WINDOW, red, (d-2, row3Y+24), (d+24, row3Y+24), 4)
                # pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        hyphen = gameFontSubtitle.render('-', True, white)
        WINDOW.blit(hyphen, (484, row3Y))
        delete = gameFontSubtitle.render('DEL', True, white)
        WINDOW.blit(delete, (556, row3Y))
        if hyphen.get_rect(topleft=(484, row3Y)).collidepoint(pygame.mouse.get_pos()):
            pygame.draw.line(WINDOW, red, (486, row3Y+24), (484+24, row3Y+24), 4)
        if delete.get_rect(topleft=(556, row3Y)).collidepoint(pygame.mouse.get_pos()):
            pygame.draw.line(WINDOW, red, (554, row3Y+24), (556+delete.get_width(), row3Y+24), 4)
        pygame.draw.line(WINDOW, white, (285, 450), (355, 450), 4)
        pygame.draw.line(WINDOW, white, (365, 450), (435, 450), 4)
        pygame.draw.line(WINDOW, white, (445, 450), (515, 450), 4)
        try:
            letter1 = gameFontStart.render(initial[0], True, white)
            WINDOW.blit(letter1, ((((70-letter1.get_width())/2)+288), 400))
        except IndexError:
            pass
        try:
            letter2 = gameFontStart.render(initial[1], True, white)
            WINDOW.blit(letter2, ((((70-letter2.get_width())/2)+368), 400))
        except IndexError:
            pass
        try:
            letter3 = gameFontStart.render(initial[2], True, white)
            WINDOW.blit(letter3, ((((70-letter3.get_width())/2)+448), 400))
        except IndexError:
            pass
        errorText = gameFont.render('Please Choose 3 Letters', True, colour)
        WINDOW.blit(errorText, ((WINDOW_WIDTH-errorText.get_width())/2, 525))

        pygame.display.update()

def update_file():
    # # The 'a' means append (as opposed to 'w' for write which will clear the file before writing.)
    highScores = open('high_scores.csv', 'a', newline='')
    fileWriter = csv.writer(highScores, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
    fileWriter.writerow([score, initial[0] + initial[1] + initial[2]])
    print('High Scores saved to file.')
    highScores.close()

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
        
        #Reading from a file
        #Next we will access that file and print the results.
        rank = 1
        suffix = ''
        rankX = 190
        scores = open('high_scores.txt', 'r')
        for j, i in enumerate(scores):
            if j < 10: # limit to the top ten
                fields = i.strip().split(',')
                # print(fields)
                if rank == 1:
                    suffix = 'st'
                elif rank == 2:
                    suffix = 'nd'
                elif rank == 3:
                    suffix = 'rd'
                elif rank >= 4:
                    suffix = 'th'
                # print(fields[0] + ' got a score of: ' + fields[1] + ' and is ' + str(rank) + suffix)
                showRank = gameFont.render(str(rank) + suffix, True, white)
                WINDOW.blit(showRank, (96+((WINDOW_WIDTH-subtitleText.get_width())/2)-showRank.get_width(), rankX))
                showName = gameFont.render(fields[1], True, white)
                WINDOW.blit(showName, (264+((WINDOW_WIDTH-subtitleText.get_width())/2)-showName.get_width(), rankX))
                showScore = gameFont.render(fields[0], True, white)
                WINDOW.blit(showScore, (456+((WINDOW_WIDTH-subtitleText.get_width())/2)-showScore.get_width(), rankX))
                rank = rank + 1
                rankX = rankX + 30
        scores.close()
        
        pygame.display.update()

render_game_start_page()