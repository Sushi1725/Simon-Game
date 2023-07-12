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
redLightColour = ('#FF0000')
blueLightColour = ('#003DFF')
yellowLightColour = ('#F0FF00')
greenLightColour = ('#25FF00')
redColour = ('#800000')
blueColour = ('#001E80')
yellowColour = ('#778000')
greenColour = ('#008000')

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

# penguin mode images
bobbingBottom = pygame.image.load('./Assets/penguin_mode/bobbing_bottom.png')
bobbingBottomScaled = pygame.transform.scale(bobbingBottom, (bobbingBottom.get_width()*3, bobbingBottom.get_height()*3))
bobbingTop = pygame.image.load('./Assets/penguin_mode/bobbing_top.png')
bobbingTopScaled = pygame.transform.scale(bobbingTop, (bobbingTop.get_width()*3, bobbingTop.get_height()*3))
lookingUp = pygame.image.load('./Assets/penguin_mode/looking_up.png')
lookingUpScaled = pygame.transform.scale(lookingUp, (lookingUp.get_width()*3, lookingUp.get_height()*3))
platform = pygame.image.load('./Assets/penguin_mode/platform.png')
platformScaled = pygame.transform.scale(platform, (platform.get_width()*3, platform.get_height()*3))

colourWidth = 15
colourLength = 175
offset = 50
redBox1 = pygame.Rect(offset, offset, colourLength, colourWidth)
redBox2 = pygame.Rect(offset, offset, colourWidth, colourLength)
yellowBox1 = pygame.Rect(offset, WINDOW_HEIGHT - offset - colourLength, colourWidth, colourLength)
yellowBox2 = pygame.Rect(offset, WINDOW_HEIGHT - offset - colourWidth, colourLength, colourWidth)
greenBox1 = pygame.Rect(WINDOW_WIDTH - offset - colourLength, offset, colourLength, colourWidth)
greenBox2 = pygame.Rect(WINDOW_WIDTH - offset - colourWidth, offset, colourWidth, colourLength)
blueBox1 = pygame.Rect(WINDOW_WIDTH - offset - colourLength, WINDOW_HEIGHT - offset - colourWidth, colourLength, colourWidth)
blueBox2 = pygame.Rect(WINDOW_WIDTH - offset - colourWidth, WINDOW_HEIGHT - offset - colourLength, colourWidth, colourLength)

# lightning forcefield images
forcefield0 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField0.png')
forcefield1 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField1.png')
forcefield2 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField2.png')
forcefield3 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField3.png')
forcefield4 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField4.png')
forcefield5 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField5.png')
forcefield6 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField6.png')
forcefield7 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField7.png')
forcefield8 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField8.png')
forcefield9 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField9.png')
forcefield10 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField10.png')
empty = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField11.png')

# rocket fire images
redFire0 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_0.png')
redFire0Scaled = pygame.transform.scale(redFire0, (redFire0.get_width()*3, redFire0.get_height()*3))
redFire1 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_1.png')
redFire1Scaled = pygame.transform.scale(redFire1, (redFire1.get_width()*3, redFire1.get_height()*3))
redFire2 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_2.png')
redFire2Scaled = pygame.transform.scale(redFire2, (redFire2.get_width()*3, redFire2.get_height()*3))
redFire3 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_3.png')
redFire3Scaled = pygame.transform.scale(redFire3, (redFire3.get_width()*3, redFire3.get_height()*3))
redFire4 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_4.png')
redFire4Scaled = pygame.transform.scale(redFire4, (redFire4.get_width()*3, redFire4.get_height()*3))
redFire5 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_5.png')
redFire5Scaled = pygame.transform.scale(redFire5, (redFire5.get_width()*3, redFire5.get_height()*3))
redFire6 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_6.png')
redFire6Scaled = pygame.transform.scale(redFire6, (redFire6.get_width()*3, redFire6.get_height()*3))

blueFire0 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_0.png')
blueFire0Scaled = pygame.transform.scale(blueFire0, (blueFire0.get_width()*3, blueFire0.get_height()*3))
blueFire1 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_1.png')
blueFire1Scaled = pygame.transform.scale(blueFire1, (blueFire1.get_width()*3, blueFire1.get_height()*3))
blueFire2 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_2.png')
blueFire2Scaled = pygame.transform.scale(blueFire2, (blueFire2.get_width()*3, blueFire2.get_height()*3))
blueFire3 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_3.png')
blueFire3Scaled = pygame.transform.scale(blueFire3, (blueFire3.get_width()*3, blueFire3.get_height()*3))
blueFire4 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_4.png')
blueFire4Scaled = pygame.transform.scale(blueFire4, (blueFire4.get_width()*3, blueFire4.get_height()*3))
blueFire5 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_5.png')
blueFire5Scaled = pygame.transform.scale(blueFire5, (blueFire5.get_width()*3, blueFire5.get_height()*3))
blueFire6 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_6.png')
blueFire6Scaled = pygame.transform.scale(blueFire6, (blueFire6.get_width()*3, blueFire6.get_height()*3))

nothing = pygame.image.load('./Assets/nothing.png')

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
gameMode = "Penguin"#"Normal"#
FRICTION = 0
gravity = 0.1
boost = False
up = 0.11
imageCounter = 0

# Set new event types
BOOST_EVENT = pygame.event.custom_type()
COLOUR_LIGHT_EVENT = pygame.event.custom_type()
FINISH_SHOWING_PATTERN_EVENT = pygame.event.custom_type()
RETURN_NORMAL_EVENT = pygame.event.custom_type()
CONTINUE_SHOWING_PATTERN_EVENT = pygame.event.custom_type()
LIFE_LOSS_LIGHT_EVENT = pygame.event.custom_type()
LIFE_LOSS_CONTINUE_EVENT = pygame.event.custom_type()

# Set up the penguin
pengSpeed = [0, 0]
pengImage = bobbingBottomScaled
pengPos = [WINDOW_WIDTH//2 - pengImage.get_width()/2, WINDOW_HEIGHT//2]
pengImageLast = bobbingTopScaled
rocketFireAnimation = nothing
fireSlideRed = [redFire0Scaled, redFire1Scaled, redFire2Scaled, redFire3Scaled, redFire4Scaled, redFire5Scaled, redFire6Scaled]
fireSlideBlue = [blueFire0Scaled, blueFire1Scaled, blueFire2Scaled, blueFire3Scaled, blueFire4Scaled, blueFire5Scaled, blueFire6Scaled]
forcefieldSlide = [empty, forcefield0, forcefield1, forcefield2, forcefield3, forcefield4, forcefield5, forcefield6, forcefield7, forcefield8, forcefield9, forcefield10]
slideNum = 0
showLives = False
pengRect = pygame.Rect(pengPos[0], pengPos[1], pengImage.get_width(), pengImage.get_height())
platformRect = pygame.Rect(WINDOW_WIDTH/2 - platformScaled.get_width()/2, WINDOW_HEIGHT/2, platformScaled.get_width(), platformScaled.get_height())
forcefieldNum = 0
forcefieldActive = True
forcefieldOpening = True
forcefieldClosing = False
canRandomPattern = True
pengPatternCounter = 0
patternStarted = False
timerHasBeenSet = False
pengModeLifeStore = life
displayBoxColour = grey

pengModeCanShowPattern = True
canShowPattern = False

##################
# Game Functions #
##################

def sort_scores():
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

def try_function(image, blitLocation): # makes it so that if the player is hovering over a transparent part of an image, the cursor wont change to a hand image
    pos = pygame.mouse.get_pos()
    clickImage = image.convert_alpha()
    try: # only work if the click isnt in a transparent area
        mask = pygame.mask.from_surface(clickImage)
        if mask.get_at((pos[0]-blitLocation[0], pos[1]-blitLocation[1])):
            if image.get_rect(topleft=blitLocation).collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                return True
    except IndexError:  # if the click is in a transparent area, dont worry about it
        pass

def render_game_start_page(): # main screen page
    waiting = True
    global score
    score = 0
    logoBob = 50 # where the logo starts at (y-axis)
    titleText = gameFontStart.render('SIMON', True, white) # write the words
    bobDirection = True # true = down, false = up
    buttonImage = startButtonNormal
    
    sort_scores()
    
    while waiting:
        for event in pygame.event.get(): # if the user closes the window, close the game
            if event.type == QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if try_function(buttonImage, (WINDOW_WIDTH/2 - buttonImage.get_width()/2, WINDOW_HEIGHT-120)):
                    buttonImage = startButtonPressed
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if try_function(settingsScaled, (WINDOW_WIDTH-90, 30)):
                    render_settings_screen()
                if try_function(leaderboardScaled, (WINDOW_WIDTH-88, WINDOW_HEIGHT-90)):
                    render_leaderboard_screen()
                if try_function(buttonImage, (WINDOW_WIDTH/2 - buttonImage.get_width()/2, WINDOW_HEIGHT-120)):
                    buttonImage = startButtonNormal
                    pygame.mouse.set_cursor()
                    waiting = False
    
        # set background colour
        WINDOW.fill(grey)        
        try_function(buttonImage, (WINDOW_WIDTH/2 - buttonImage.get_width()/2, WINDOW_HEIGHT-120))
        try_function(settingsScaled, (WINDOW_WIDTH-90, 30))
        try_function(leaderboardScaled, (WINDOW_WIDTH-88, WINDOW_HEIGHT-90))
        
        if not try_function(buttonImage, (WINDOW_WIDTH/2 - buttonImage.get_width()/2, WINDOW_HEIGHT-120)) and not try_function(settingsScaled, (WINDOW_WIDTH-90, 30)) and not try_function(leaderboardScaled, (WINDOW_WIDTH-88, 510)):
            pygame.mouse.set_cursor()
            buttonImage = startButtonNormal

        # display text and images
        WINDOW.blit(bgYellow, (0,0))
        WINDOW.blit(bgBlue, (0,302))
        WINDOW.blit(bgRed, (402, 0))
        WINDOW.blit(bgGreen, (402,302))
        WINDOW.blit(titleText, (279, 50))
        WINDOW.blit(mainPageImageScaled, (175, logoBob))
        WINDOW.blit(buttonImage, (WINDOW_WIDTH/2 - buttonImage.get_width()/2, 480))
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
        choose_mode()
    while not running:
        render_game_over_screen()

def choose_mode():
    red = ('#FF0000')
    chooseModeScreen = 1
    global gameMode
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
                    chooseModeScreen = chooseModeScreen - 1
                    if chooseModeScreen < 1:
                        chooseModeScreen = 1
                if 675 <= x <= 726 and 299.5 <= y <= 350.5:
                    chooseModeScreen = chooseModeScreen + 1
                    if chooseModeScreen > 2:
                        chooseModeScreen = 2
                if 600 <= x <= 700 and 400 <= y <= 500:
                    render_game_start_page()
                if chooseModeScreen == 1:
                    if 225 <= x <= 575 and 200 <= y <= 275:
                        gameMode = "Easy"
                        waiting = False
                    if 225 <= x <= 575 and 300 <= y <= 375:
                        gameMode = "Normal"
                        waiting = False
                    if 225 <= x <= 575 and 400 <= y <= 475:
                        gameMode = "Hard"
                        waiting = False
                if chooseModeScreen == 2:
                    if 225 <= x <= 575 and 200 <= y <= 275:
                        gameMode = "Penguin"
                        waiting = False
                    
        WINDOW.fill(grey)
        WINDOW.blit(blackGradientScreen, (0,0))
        pygame.draw.rect(WINDOW, black, bg)
        pygame.draw.rect(WINDOW, white, bg, 2)
        credBg = pygame.Rect(150, 50, 500, 100)
        pygame.draw.rect(WINDOW, black, credBg)
        pygame.draw.rect(WINDOW, white, credBg, 2)
        WINDOW.blit(homeButtonScaled, (600, 400))
        WINDOW.blit(nextPageScaled, (75, 299.5))
        WINDOW.blit(backPageScaled, (675, 299.5))
        chooseModeText = gameFontEnd.render('Choose Mode', True, white)
        WINDOW.blit(chooseModeText, (WINDOW_WIDTH/2-(chooseModeText.get_width()/2)+5, 85))
        if homeButtonScaled.get_rect(topleft=(600, 400)).collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if chooseModeScreen == 1:
            cover = pygame.Rect(75, 299.5, 51, 51)
            pygame.draw.rect(WINDOW, black, cover)
            modeBox1 = pygame.Rect(225, 200, 350, 75)
            pygame.draw.rect(WINDOW, black, modeBox1)
            if modeBox1.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                modeBox1Colour = red
            else:
                modeBox1Colour = white
            pygame.draw.rect(WINDOW, modeBox1Colour, modeBox1, 2)
            easyMode = gameFontCred.render('Easy', True, white)
            WINDOW.blit(easyMode, (WINDOW_WIDTH/2-(easyMode.get_width()/2), 225))
            modeBox2 = pygame.Rect(225, 300, 350, 75)
            pygame.draw.rect(WINDOW, black, modeBox2)
            if modeBox2.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                modeBox2Colour = red
            else:
                modeBox2Colour = white
            pygame.draw.rect(WINDOW, modeBox2Colour, modeBox2, 2)
            normalMode = gameFontCred.render('Normal', True, white)
            WINDOW.blit(normalMode, (WINDOW_WIDTH/2-(normalMode.get_width()/2)+5, 325))
            modeBox3 = pygame.Rect(225, 400, 350, 75)
            pygame.draw.rect(WINDOW, black, modeBox3)
            if modeBox3.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                modeBox3Colour = red
            else:
                modeBox3Colour = white
            pygame.draw.rect(WINDOW, modeBox3Colour, modeBox3, 2)
            hardMode = gameFontCred.render('Hard', True, white)
            WINDOW.blit(hardMode, (WINDOW_WIDTH/2-(hardMode.get_width()/2)+5, 425))
            if nextPageScaled.get_rect(topleft=(675, 299.5)).collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if not homeButtonScaled.get_rect(topleft=(600, 400)).collidepoint(pygame.mouse.get_pos()) and not nextPageScaled.get_rect(topleft=(675, 299.5)).collidepoint(pygame.mouse.get_pos()) and not modeBox1.collidepoint(pygame.mouse.get_pos()) and not modeBox2.collidepoint(pygame.mouse.get_pos()) and not modeBox3.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor()
        if chooseModeScreen == 2:
            cover = pygame.Rect(675, 299.5, 51, 51)
            pygame.draw.rect(WINDOW, black, cover)
            modeBox1 = pygame.Rect(225, 200, 350, 75)
            pygame.draw.rect(WINDOW, black, modeBox1)
            if modeBox1.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                modeBox1Colour = red
            else:
                modeBox1Colour = white
            pygame.draw.rect(WINDOW, modeBox1Colour, modeBox1, 2)
            penguinMode = gameFontCred.render('Penguin', True, white)
            WINDOW.blit(penguinMode, (WINDOW_WIDTH/2-(penguinMode.get_width()/2)+5, 225))
            modeBox2 = pygame.Rect(225, 300, 350, 75)
            pygame.draw.rect(WINDOW, black, modeBox2)
            if modeBox2.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                modeBox2Colour = red
            else:
                modeBox2Colour = white
            pygame.draw.rect(WINDOW, modeBox2Colour, modeBox2, 2)
            modeBox3 = pygame.Rect(225, 400, 350, 75)
            pygame.draw.rect(WINDOW, black, modeBox3)
            if modeBox3.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                modeBox3Colour = red
            else:
                modeBox3Colour = white
            pygame.draw.rect(WINDOW, modeBox3Colour, modeBox3, 2)
            if backPageScaled.get_rect(topleft=(75, 299.5)).collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if not homeButtonScaled.get_rect(topleft=(600, 400)).collidepoint(pygame.mouse.get_pos()) and not backPageScaled.get_rect(topleft=(75, 299.5)).collidepoint(pygame.mouse.get_pos()) and not modeBox1.collidepoint(pygame.mouse.get_pos()) and not modeBox2.collidepoint(pygame.mouse.get_pos()) and not modeBox3.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor()
        pygame.display.update()
    while running:
        if gameMode == "Easy":
            random_pattern()
            show_pattern()
            store_player_guess()
        if gameMode == "Normal":
            random_pattern()
            show_pattern()
            store_player_guess()
        if gameMode == "Hard":
            random_pattern()
            show_pattern()
            store_player_guess()
        if gameMode == "Penguin":
            peng_flying_game_mode()

def render_game_simon_play_page(yellowColour = yellowScaled, blueColour = blueScaled, greenColour = greenScaled, redColour = redScaled):
    for event in pygame.event.get():
        if event.type == QUIT:
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
    global pengModeCanShowPattern
    global canRandomPattern
    pattern.append(random.randint(1, 4))
    print(pattern)
    canRandomPattern = False
    # pengModeCanShowPattern = False

def quit():
    global running
    running = False
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def colour_light(name):
    global gameMode
    global timeDelay
    global patternStarted
    pygame.mixer.music.load(f'./Assets/sounds/{name}.wav')
    pygame.mixer.music.play()
    if gameMode == "Easy" or gameMode == "Normal" or gameMode == "Hard":
        pygame.time.delay(timeDelay) # current set time delay (faster as the game progresses)
        render_game_simon_play_page() # move it back into the "all dark" state
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
    if gameMode == "Penguin":
        patternStarted = True
        pygame.time.set_timer(COLOUR_LIGHT_EVENT, timeDelay, 1)
        print('colour got turned off')

def show_pattern():
    # 1 = red
    # 2 = green
    # 3 = yellow
    # 4 = blue
    global redColour
    global greenColour
    global yellowColour
    global blueColour
    global redLightColour
    global greenLightColour
    global yellowLightColour
    global blueLightColour
    global canShowPattern
    global forcefieldClosing
    global pengPatternCounter
    global pattern
    global pengModeLifeStore
    global life
    global displayBoxColour
    
    timeDelay = 500 - 100 * int(len(pattern) / 5) # changing it to an integer makes it round down if is float
    if timeDelay <= 100:
        print('now 100')
        timeDelay = 100
    
    if gameMode == "Easy" or gameMode == "Normal" or gameMode == "Hard":
        render_game_simon_play_page()
        pygame.time.delay(300)
        
        for x in pattern:
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
        
            if x == 1: # 1 = red
                render_game_simon_play_page(redColour = redLightScaled) # change it into light mode
                colour_light('red_a')
            elif x == 2: # 2 = green
                render_game_simon_play_page(greenColour = greenLightScaled) # change it into light mode
                colour_light('green_e-lower')
            elif x == 3: # 3 = yellow
                render_game_simon_play_page(yellowColour = yellowLightScaled) # change it into light mode
                colour_light('yellow_c-sharp')
            elif x == 4: # 4 = blue
                render_game_simon_play_page(blueColour = blueLightScaled) # change it into light mode
                colour_light('blue_e-upper')
            print(pattern)
            pygame.time.delay(timeDelay)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
    if gameMode == 'Penguin' and pengPatternCounter < len(pattern):
        print(f"pengModeCanShowPattern:{pengModeCanShowPattern}, forcefieldActive:{forcefieldActive}, canRandomPattern:{canRandomPattern}, canShowPattern:{canShowPattern}")
        if pattern[pengPatternCounter] == 1: # 1 = red
            displayBoxColour = redLightColour
            redColour, redLightColour = redLightColour, redColour # change it into light mode
            colour_light('red_a')
        elif pattern[pengPatternCounter] == 2: # 2 = green
            displayBoxColour = greenLightColour
            greenColour, greenLightColour = greenLightColour, greenColour # change it into light mode
            colour_light('green_e-lower')
        elif pattern[pengPatternCounter] == 3: # 3 = yellow
            displayBoxColour = yellowLightColour
            yellowColour, yellowLightColour = yellowLightColour, yellowColour # change it into light mode
            colour_light('yellow_c-sharp')
        elif pattern[pengPatternCounter] == 4: # 4 = blue
            displayBoxColour = blueLightColour
            blueColour, blueLightColour = blueLightColour, blueColour # change it into light mode
            colour_light('blue_e-upper')
        pengPatternCounter = pengPatternCounter + 1
        canShowPattern = False
        # if pengPatternCounter < len(pattern):
        #     print('continueing')
        #     pygame.time.set_timer(CONTINUE_SHOWING_PATTERN_EVENT, 1, 1) ### WHOLE GAME WORKS IF THE SECOND NUMBER IS SMALL ENOUGH
    if gameMode == 'Penguin' and pengPatternCounter >= len(pattern):
        if pengModeLifeStore == life:
            print()
            pygame.time.set_timer(FINISH_SHOWING_PATTERN_EVENT, timeDelay-50, 1)
            canShowPattern = False
            pengPatternCounter = 0
        if pengModeLifeStore != life:
            pengModeLifeStore = life
            pygame.time.set_timer(FINISH_SHOWING_PATTERN_EVENT, 2000+timeDelay-50, 1)
            canShowPattern = False
            pengPatternCounter = 0

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
    
    clickBlueScaled = blueScaled.convert_alpha() # changes the image pixels so that the transparent ones wont count
    clickGreenScaled = greenScaled.convert_alpha()
    clickRedScaled = redScaled.convert_alpha()
    clickYellowScaled = yellowScaled.convert_alpha()
    blueScaledPos = (400, 300)
    greenScaledPos = (400, 75)
    redScaledPos = (175, 75) # location theyre blitted at
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
                        colour_light('red_a')
                        playerPattern.append(1) # add the guess to the end of the array
                        check_pattern(playerPattern) # compare it
                        if life != lifeStore:
                            break
                except IndexError:  # if the click is in a transparent area, dont worry about it
                    pass
                try: # only work if the click isnt in a transparent area
                    mask = pygame.mask.from_surface(clickGreenScaled)
                    if mask.get_at((event.pos[0]-greenScaledPos[0], event.pos[1]-greenScaledPos[1])):
                        render_game_simon_play_page(greenColour = greenLightScaled) # change it into light mode
                        colour_light('green_e-lower')
                        playerPattern.append(2) # add it to the end of the array
                        check_pattern(playerPattern)
                        if life != lifeStore:
                            break
                except IndexError:  # if the click is in a transparent area, dont worry about it
                    pass
                try: # only work if the click isnt in a transparent area
                    mask = pygame.mask.from_surface(clickYellowScaled)
                    if mask.get_at((event.pos[0]-yellowScaledPos[0], event.pos[1]-yellowScaledPos[1])):
                        render_game_simon_play_page(yellowColour = yellowLightScaled) # change it into light mode
                        colour_light('yellow_c-sharp')
                        playerPattern.append(3) # add it to the end of the array
                        check_pattern(playerPattern)
                        if life != lifeStore:
                            break
                except IndexError:  # if the click is in a transparent area, dont worry about it
                    pass
                try: # only work if the click isnt in a transparent area
                    mask = pygame.mask.from_surface(clickBlueScaled) # mask makes it so that the translucent part of the image cannot be clicked
                    if mask.get_at((event.pos[0]-blueScaledPos[0], event.pos[1]-blueScaledPos[1])):
                        render_game_simon_play_page(blueColour = blueLightScaled) # change it into light mode
                        colour_light('blue_e-upper')
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
        print('now we checking the user\'s choice')
        global life
        global pengModeLifeStore
        pengModeLifeStore = life
        life = life - 1
        
        global heart1
        global heart2
        global heart3
        global gameMode
        
        global forcefieldActive
        global forcefieldOpening
        global forcefieldClosing
        global canRandomPattern
        global pengPatternCounter
        global patternStarted
        global timerHasBeenSet
        global pengModeCanShowPattern
        global canShowPattern
        
        print(f"forcefieldActive:{forcefieldActive}, forcefieldOpening:{forcefieldOpening}, forcefieldClosing:{forcefieldClosing}, canRandomPattern:{canRandomPattern}, pengPatternCounter:{pengPatternCounter}, patternStarted:{patternStarted}, timerHasBeenSet:{timerHasBeenSet}, pengModeCanShowPattern:{pengModeCanShowPattern}, canShowPattern:{canShowPattern}")
        
        if life == 2:
            pygame.time.set_timer(RETURN_NORMAL_EVENT, 3000, 1)
            heart1 = heartImageEmptyScaled
            if gameMode == "Easy" or gameMode == "Normal" or gameMode == "Hard":
                WINDOW.blit(heart1, (WINDOW_WIDTH-36-36-36-5-5-50, 50))
                pygame.display.update()
                life_loss()
            if gameMode == "Penguin":
                peng_life_loss()
        if life == 1:
            pygame.time.set_timer(RETURN_NORMAL_EVENT, 3000, 1)
            print('one life left')
            heart1 = heartImageEmptyScaled
            heart2 = heartImageEmptyScaled
            if gameMode == "Easy" or gameMode == "Normal" or gameMode == "Hard":
                WINDOW.blit(heart1, (WINDOW_WIDTH-36-36-36-5-5-50, 50))
                WINDOW.blit(heart2, (WINDOW_WIDTH-36-36-5-50, 50))
                pygame.display.update()
                life_loss()
            if gameMode == "Penguin":
                peng_life_loss()
        if life == 0:
            heart1 = heartImageEmptyScaled
            heart2 = heartImageEmptyScaled
            heart3 = heartImageEmptyScaled
            if gameMode == "Easy" or gameMode == "Normal" or gameMode == "Hard":
                WINDOW.blit(heart1, (WINDOW_WIDTH-36-36-36-5-5-50, 50))
                WINDOW.blit(heart2, (WINDOW_WIDTH-36-36-5-50, 50))
                WINDOW.blit(heart3, (WINDOW_WIDTH-36-50, 50))
                pygame.display.update()
                render_save_score_screen()
            if gameMode == "Penguin":
                render_save_score_screen()

def peng_life_loss():
    global redColour
    global redLightColour
    global greenColour
    global greenLightColour
    global yellowColour
    global yellowLightColour
    global blueColour
    global blueLightColour
    global timeDelay
    pygame.time.delay(timeDelay + 150) # NEED A WAY TO FIX THIS, 
    # THE COLOUR_LIGHT FUNCTION IS CALLED WHEN THE PLAYER HITS THE BLOCK AND THEREFORE WILL DISABLE THE beepbeepbeep sound BEFORE IT FINISHES
    
    pygame.mixer.music.load('./Assets/sounds/beep_beep_beep.wav')
    pygame.mixer.music.play()
    print('player got it wrong so sound played and life lost')
    redColour, redLightColour = ('#FF0000'), ('#800000')
    blueColour, blueLightColour = ('#003DFF'), ('#001E80')
    yellowColour, yellowLightColour = ('#F0FF00'), ('#778000')
    greenColour, greenLightColour = ('#25FF00'), ('#008000')
    pygame.time.set_timer(LIFE_LOSS_LIGHT_EVENT, 500, 1)
    pygame.time.set_timer(LIFE_LOSS_CONTINUE_EVENT, 750, 2)
    ## some sort of 750ms break here
    # redColour, redLightColour = redLightColour, redColour # change it into light mode
    # greenColour, greenLightColour = greenLightColour, greenColour # change it into light mode
    # yellowColour, yellowLightColour = yellowLightColour, yellowColour # change it into light mode
    # blueColour, blueLightColour = blueLightColour, blueColour # change it into light mode
    # pygame.time.set_timer(LIFE_LOSS_LIGHT_EVENT, 500, 1)
    # pygame.time.set_timer(LIFE_LOSS_CONTINUE_EVENT, 750, 1)
    # ## some sort of 750ms break here
    # redColour, redLightColour = redLightColour, redColour # change it into light mode
    # greenColour, greenLightColour = greenLightColour, greenColour # change it into light mode
    # yellowColour, yellowLightColour = yellowLightColour, yellowColour # change it into light mode
    # blueColour, blueLightColour = blueLightColour, blueColour # change it into light mode
    # pygame.time.set_timer(COLOUR_LIGHT_EVENT, 500, 1)

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
            linesP2 = ["The game has four coloured", "buttons where each button", "produces a unique tone when", "it is pressed or activated.", "One round in the game", "consists of one or more", "colours lighting up and", "sounding in a random order.", "After, the player must", "reproduce that pattern by", "pressing the buttons.", "As the game progresses,"]
            y = 175
            for o in linesP2:
                WINDOW.blit(gameFont.render(o, True, white), (140, y))
                y = y + 25
        elif textToShowNum == 3:
            cover = pygame.Rect(675, 299.5, 51, 51)
            pygame.draw.rect(WINDOW, black, cover)
            linesP3 = ["the number of buttons", "that needs to be pressed", "increases. The speed which", "the colour pattern is", "played at also gets faster", "every 5 turns. You are", "given 3 lives. Your goal", "is to get the highest", "score in those 3 lives to", "get onto the leaderboard.", ""]
            y = 150
            for p in linesP3:
                WINDOW.blit(gameFont.render(p, True, white), (140, y))
                y = y + 25
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

def peng_flying_game_mode():
    global imageCounter
    global boost
    global redLightColour
    global blueLightColour
    global yellowLightColour
    global greenLightColour
    global redColour
    global blueColour
    global yellowColour
    global greenColour
    global forcefieldOpening
    global forcefieldActive
    global forcefieldClosing
    global canShowPattern
    global pengModeCanShowPattern
    global patternStarted
    
    global playerPattern
    global redColour
    global greenColour
    global yellowColour
    global blueColour
    global redLightColour
    global greenLightColour
    global yellowLightColour
    global blueLightColour
    global forcefieldClosing
    global canRandomPattern
    global canShowPattern
    global forcefieldOpening
    global forcefieldActive
    global timeDelay
    global pengPatternCounter
    global pattern
    global boost
    global patternStarted
    global timerHasBeenSet
    global displayBoxColour

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == BOOST_EVENT: 
                boost = False
                print(imageCounter)
            if event.type == LIFE_LOSS_LIGHT_EVENT:
                redColour, redLightColour = ('#800000'), ('#FF0000')
                blueColour, blueLightColour = ('#001E80'), ('#003DFF')
                yellowColour, yellowLightColour = ('#778000'), ('#F0FF00')
                greenColour, greenLightColour = ('#008000'), ('#25FF00')
            if event.type == RETURN_NORMAL_EVENT:
                print('now returning to normal - repeating the process')
                forcefieldActive = True
                forcefieldOpening = True
                forcefieldClosing = False
                canRandomPattern = True
                pengModeCanShowPattern = True
                canShowPattern = False
                patternStarted = False
            if event.type == CONTINUE_SHOWING_PATTERN_EVENT:
                print('in')
                print(pengPatternCounter)
                if pengPatternCounter < len(pattern):
                    print('first time')
                    canRandomPattern = False
                    pengModeCanShowPattern = True
                    canShowPattern = True
                    timerHasBeenSet = False
            if event.type == FINISH_SHOWING_PATTERN_EVENT:
                print('ending the showing, now for user input')
                forcefieldClosing = True
                forcefieldActive = False
                forcefieldOpening = False
            if event.type == BOOST_EVENT: 
                boost = False
                print(imageCounter)
            if event.type == LIFE_LOSS_CONTINUE_EVENT:
                redColour, redLightColour = ('#FF0000'), ('#800000')
                blueColour, blueLightColour = ('#003DFF'), ('#001E80')
                yellowColour, yellowLightColour = ('#F0FF00'), ('#778000')
                greenColour, greenLightColour = ('#25FF00'), ('#008000')
                pygame.time.set_timer(LIFE_LOSS_LIGHT_EVENT, 500, 1)
        
        # refresh display
        WINDOW.fill(grey)
        
        displayBox = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        pygame.draw.rect(WINDOW, displayBoxColour, displayBox) # to display the current colour pattern
        coverPrev = pygame.Rect(10, 10, WINDOW_WIDTH-20, WINDOW_HEIGHT-20)
        pygame.draw.rect(WINDOW, grey, coverPrev)

        # draw elements
        # WINDOW.blit((gameFont.render('Score: 0', True, white)), (50, 50))
        
        ########## Draw Borders of Game Area ##########
        redBox1 = pygame.Rect(offset, offset, colourLength, colourWidth)
        redBox2 = pygame.Rect(offset, offset, colourWidth, colourLength)
        yellowBox1 = pygame.Rect(offset, WINDOW_HEIGHT - offset - colourLength, colourWidth, colourLength)
        yellowBox2 = pygame.Rect(offset, WINDOW_HEIGHT - offset - colourWidth, colourLength, colourWidth)
        greenBox1 = pygame.Rect(WINDOW_WIDTH - offset - colourLength, offset, colourLength, colourWidth)
        greenBox2 = pygame.Rect(WINDOW_WIDTH - offset - colourWidth, offset, colourWidth, colourLength)
        blueBox1 = pygame.Rect(WINDOW_WIDTH - offset - colourLength, WINDOW_HEIGHT - offset - colourWidth, colourLength, colourWidth)
        blueBox2 = pygame.Rect(WINDOW_WIDTH - offset - colourWidth, WINDOW_HEIGHT - offset - colourLength, colourWidth, colourLength)
        pygame.draw.rect(WINDOW, redColour, redBox1)
        pygame.draw.rect(WINDOW, redColour, redBox2)
        pygame.draw.rect(WINDOW, yellowColour, yellowBox1)
        pygame.draw.rect(WINDOW, yellowColour, yellowBox2)
        pygame.draw.rect(WINDOW, greenColour, greenBox1)
        pygame.draw.rect(WINDOW, greenColour, greenBox2)
        pygame.draw.rect(WINDOW, blueColour, blueBox1)
        pygame.draw.rect(WINDOW, blueColour, blueBox2)
        ###############################################
        global forcefieldNum
        WINDOW.blit(platformScaled, (WINDOW_WIDTH/2 - platformScaled.get_width()/2, WINDOW_HEIGHT/2))
        
        ###
        if imageCounter % 3 == 0: # 50ms per frame
            if forcefieldOpening == True:
                # set somethig to make forcefieldNum = 0 once only
                forcefieldNum = forcefieldNum + 1
                if forcefieldNum > 7:
                    forcefieldNum = 8
                    forcefieldOpening = False
            elif forcefieldClosing == True:
                # set somethig to make forcefieldNum = 10 once only
                forcefieldNum = forcefieldNum - 1
                if forcefieldNum < 0:
                    forcefieldNum = 0
                    forcefieldClosing = False
                    forcefieldActive = False
                    pengModeCanShowPattern = False
        if forcefieldActive == True and forcefieldOpening == False and forcefieldClosing == False:
            if imageCounter % 9 == 0: # 75ms per frame
                forcefieldNum = forcefieldNum + 1
                if forcefieldNum > 11:
                    forcefieldNum = 8
        ### to be put into show player pattern
        if forcefieldNum == 11 and canRandomPattern == False and canShowPattern == False and patternStarted == False:
            canShowPattern = True
        WINDOW.blit(forcefieldSlide[forcefieldNum], (WINDOW_WIDTH/2 - forcefieldSlide[forcefieldNum].get_width()/2, WINDOW_HEIGHT/2 - forcefieldSlide[forcefieldNum].get_height()/2 - 35))
        
        # make this in the middle and flash up when the player dies x times
        if showLives:
            WINDOW.blit(heart1, (WINDOW_WIDTH-36-36-36-5-5-50, 50))
            WINDOW.blit(heart2, (WINDOW_WIDTH-36-36-5-50, 50))
            WINDOW.blit(heart3, (WINDOW_WIDTH-36-50, 50))
        
        pygame.time.Clock().tick(FPS)
        
        game_loop()
        # pygame.display.update()
        imageCounter = imageCounter + 1
        # print(imageCounter)

# Define a function to apply friction to the penguin's speed
def apply_friction():
    pengSpeed[0] *= 1 - FRICTION
    pengSpeed[1] *= 1 - FRICTION

# Define a function to apply gravitational force to the penguin's speed
def apply_gravity():
    pengSpeed[1] += gravity

# Define a function to update the penguin's position
def update_penguin_position():
    global pengImage
    global imageCounter
    global pengImageLast
    global rocketFireAnimation
    global slideNum
    global fireSlideRed
    global boost
    global pengRect
    pengPos[0] += pengSpeed[0]
    pengPos[1] += pengSpeed[1]
    # Update the position of the penguin on the screen
    WINDOW.blit(pengImage, pengPos)
    pengRect = pygame.Rect(pengPos[0], pengPos[1], pengImage.get_width(), pengImage.get_height())
    # pygame.draw.rect(WINDOW, white, pengRect)
    
    ############ ANIMATION ############
    if imageCounter % 45 == 0 and pengPos[1] + pengImage.get_height() >= WINDOW_HEIGHT: # every 3/4 seconds if on the floor
        if pengImageLast == bobbingTopScaled:
            pengImage = bobbingTopScaled
            pengImageLast = bobbingBottomScaled
            return # dont go to the next if
        if pengImageLast == bobbingBottomScaled:
            pengImage = bobbingBottomScaled
            pengImageLast = bobbingTopScaled
            return
    ###################################
    
    fireSlide = fireSlideRed    
    if boost:
        fireSlide = fireSlideBlue
    else:
        fireSlide = fireSlideRed
    
    WINDOW.blit(rocketFireAnimation, (pengPos[0] + (pengImage.get_width()/2) - (rocketFireAnimation.get_width()/2), pengPos[1] + pengImage.get_height()))
    pressed = pygame.key.get_pressed()
    if (pressed[K_UP]) and imageCounter % 5 == 0: # 12 fps if currently flying
        slideNum = slideNum + 1
        if slideNum > 6:
            slideNum = 0
        rocketFireAnimation = fireSlide[slideNum]
    elif (not pressed[K_UP]): # when not up button being pressed
        rocketFireAnimation = nothing

def check_pos():
    global pengImage
    global gravity
    # Limit the penguin's position to within the walls of the screen
    if pengPos[0] < 0: # if touching the left wall
        pengPos[0] = 0
        pengSpeed[0] = 0
    elif pengPos[0] + pengImage.get_width() > WINDOW_WIDTH: # if touching the right wall
        pengPos[0] = WINDOW_WIDTH - pengImage.get_width()
        pengSpeed[0] = 0
    if pengPos[1] < 0: # if touching the top wall
        pengPos[1] = 0
        pengSpeed[1] = 0
    elif pengPos[1] + pengImage.get_height() > WINDOW_HEIGHT: # if touching the bottom wall
        pengPos[1] = WINDOW_HEIGHT - pengImage.get_height()
        pengSpeed[1] = 0
        pengSpeed[0] = 0
    if pengPos[0] < platformScaled.get_width() + WINDOW_WIDTH/2 - platformScaled.get_width()/2 and pengPos[0] > WINDOW_WIDTH/2 - platformScaled.get_width()/2 - pengImage.get_width():
        if pengPos[1] > WINDOW_HEIGHT/2 - pengImage.get_height() + 1:
            pengPos[1] = WINDOW_HEIGHT/2 - pengImage.get_height()
            pengSpeed[1] = 0
            pengSpeed[0] = 0
            gravity = 0
        if pengPos[1] < WINDOW_HEIGHT/2 - pengImage.get_height():
            gravity = 0.1
    else:
        gravity = 0.1
    # if pygame.Rect.colliderect(pengRect, platformRect):
    #     if pengPos[0] < WINDOW_WIDTH/2 - platformScaled.get_width()/2: # to the left
    #         pengPos[0] = pengPos[0]
    #         pengSpeed[0] = 0
    #     elif pengPos[0] > WINDOW_WIDTH/2 + platformScaled.get_width()/2 - 1: # to the right
    #         pengPos[0] = pengPos[0]
    #         pengSpeed[0] = 0
    #     if pengPos[1] < WINDOW_HEIGHT/2: # above
    #         pressed = pygame.key.get_pressed()
    #         if (not pressed[K_UP]):
    #             gravity = 0
    #             pengSpeed[1] = 0
    #             pengPos[1] = WINDOW_HEIGHT/2 - pengImage.get_height()
    #         else:
    #             gravity = 0.1
            
    #     if pengPos[1] > WINDOW_HEIGHT/2 + platformScaled.get_height(): # below
    #         pengPos[1] = pengPos[1]

def apply_key():
    global pengImage
    global boost
    if boost:
        up = 0.25
    else:
        up = 0.15
    pressed = pygame.key.get_pressed()
    if (pressed[K_UP]):
        pengSpeed[1] -= up
        pengImage = lookingUpScaled
    if (pressed[K_RIGHT]):
        pengSpeed[0] += 0.05
    if (pressed[K_LEFT]):
        pengSpeed[0] -= 0.05
    if (pressed[K_DOWN]):
        pengSpeed[1] += 0.0
    if boost != True: # make sure you cant start the boost while the boost is on
        if (pressed[K_SPACE]):
            boost = True
            pygame.time.set_timer(BOOST_EVENT, 5000, 1) # start the timer every sec

def check_wall_pos(wallArea):
    global pengPos
    global pengSpeed
    pointToMoveToX = WINDOW_WIDTH/2 - pengImage.get_width()/2
    pointToMoveToY = WINDOW_HEIGHT/2 - pengImage.get_height()
    
    if wallArea == "topLeft":
        # print("(" + str(offset+colourLength-pengImage.get_width()) + ", " + str(offset+colourLength-pengImage.get_height()) + ")")
        pengSpeed[1] = 0
        pengSpeed[0] = 0
        gradient = (pointToMoveToY - pengPos[1])/(pointToMoveToX - pengPos[0])
        while pengPos[0] < pointToMoveToX and pengPos[1] < pointToMoveToY:
            pengPos[0] = pengPos[0] + 1
            pengPos[1] = pengPos[1] + gradient
            WINDOW.blit(pengImage, pengPos)
            pygame.display.update()
    if wallArea == "topRight":
        # print("(" + str(WINDOW_WIDTH-offset-colourLength-pengImage.get_width()) + ", " + str(offset+colourLength-pengImage.get_height()) + ")")
        pengSpeed[1] = 0
        pengSpeed[0] = 0
        gradient = (pointToMoveToY - pengPos[1])/(pointToMoveToX - pengPos[0])
        while pengPos[0] > pointToMoveToX and pengPos[1] < pointToMoveToY:
            pengPos[0] = pengPos[0] - 1
            pengPos[1] = pengPos[1] - gradient
            WINDOW.blit(pengImage, pengPos)
            pygame.display.update()
    if wallArea == "bottomLeft":
        # print("(" + str(offset+colourLength-pengImage.get_width()) + ", " + str(WINDOW_HEIGHT-offset-colourLength+pengImage.get_height()) + ")")
        pengSpeed[1] = 0
        pengSpeed[0] = 0
        gradient = (pointToMoveToY - pengPos[1])/(pointToMoveToX - pengPos[0])
        while pengPos[0] < pointToMoveToX and pengPos[1] > pointToMoveToY:
            pengPos[0] = pengPos[0] + 1
            pengPos[1] = pengPos[1] + gradient
            WINDOW.blit(pengImage, pengPos)
            pygame.display.update()
    if wallArea == "bottomRight":
        # print("(" + str(offset+colourLength-pengImage.get_width()) + ", " + str(WINDOW_HEIGHT-offset-colourLength+pengImage.get_height()) + ")")
        pengSpeed[1] = 0
        pengSpeed[0] = 0
        gradient = (pointToMoveToY - pengPos[1])/(pointToMoveToX - pengPos[0])
        while pengPos[0] > pointToMoveToX and pengPos[1] > pointToMoveToY:
            pengPos[0] = pengPos[0] - 1
            pengPos[1] = pengPos[1] - gradient
            WINDOW.blit(pengImage, pengPos)
            pygame.display.update()

def penguin_mode_store_player_guess():
    # 1 = red
    # 2 = green
    # 3 = yellow
    # 4 = blue
    global playerPattern
    global pattern
    global lifeStore
    global life
    global score
    global pengImage
    global pengPos
    global pengRect
    global redColour
    global greenColour
    global yellowColour
    global blueColour
    global redLightColour
    global greenLightColour
    global yellowLightColour
    global blueLightColour
    global canShowPattern
    global canRandomPattern
    global pengModeCanShowPattern
    global pengModeLifeStore
    
    pengRect = pygame.Rect(pengPos[0], pengPos[1], pengImage.get_width(), pengImage.get_height())
    
    if len(playerPattern) < len(pattern): # so that we check each item of the pattern
        if pygame.Rect.colliderect(pengRect, redBox1): #if the player touches a box
            redColour, redLightColour = redLightColour, redColour # change it into light mode
            colour_light('red_a')
            playerPattern.append(1) # add the guess to the end of the array
            check_wall_pos("topLeft")
            check_pattern(playerPattern) # compare it
            # if life != lifeStore:
            #     return # break out of the if (return doenst do it)
        elif pygame.Rect.colliderect(pengRect, redBox2):
            redColour, redLightColour = redLightColour, redColour # change it into light mode
            colour_light('red_a')
            playerPattern.append(1) # add the guess to the end of the array
            check_wall_pos("topLeft")
            check_pattern(playerPattern) # compare it
            # if life != lifeStore:
            #     return # break out of the if (return doenst do it)
        elif pygame.Rect.colliderect(pengRect, greenBox1):
            greenColour, greenLightColour = greenLightColour, greenColour # change it into light mode
            colour_light('green_e-lower')
            playerPattern.append(2) # add the guess to the end of the array
            check_wall_pos("topRight")
            check_pattern(playerPattern) # compare it
            # if life != lifeStore:
            #     return # break out of the if (return doenst do it)
        elif pygame.Rect.colliderect(pengRect, greenBox2):
            greenColour, greenLightColour = greenLightColour, greenColour # change it into light mode
            colour_light('green_e-lower')
            playerPattern.append(2) # add the guess to the end of the array
            check_wall_pos("topRight")
            check_pattern(playerPattern) # compare it
            # if life != lifeStore:
            #     return # break out of the if (return doenst do it)
        elif pygame.Rect.colliderect(pengRect, yellowBox1):
            yellowColour, yellowLightColour = yellowLightColour, yellowColour # change it into light mode
            colour_light('yellow_c-sharp')
            playerPattern.append(3) # add the guess to the end of the array
            check_wall_pos("bottomLeft")
            check_pattern(playerPattern) # compare it
            # if life != lifeStore:
            #     return # break out of the if (return doenst do it)
        elif pygame.Rect.colliderect(pengRect, yellowBox2):
            yellowColour, yellowLightColour = yellowLightColour, yellowColour # change it into light mode
            colour_light('yellow_c-sharp')
            playerPattern.append(3) # add the guess to the end of the array
            check_wall_pos("bottomLeft")
            check_pattern(playerPattern) # compare it
            # if life != lifeStore:
            #     return # break out of the if (return doenst do it)
        elif pygame.Rect.colliderect(pengRect, blueBox1):
            blueColour, blueLightColour = blueLightColour, blueColour # change it into light mode
            colour_light('blue_e-upper')
            playerPattern.append(4) # add the guess to the end of the array
            check_wall_pos("bottomRight")
            check_pattern(playerPattern) # compare it
            # if life != lifeStore:
            #     return # break out of the if (return doenst do it)
        elif pygame.Rect.colliderect(pengRect, blueBox2):
            blueColour, blueLightColour = blueLightColour, blueColour # change it into light mode
            colour_light('blue_e-upper')
            playerPattern.append(4) # add the guess to the end of the array
            check_wall_pos("bottomRight")
            check_pattern(playerPattern) # compare it
            # if life != lifeStore:
            #     return # break out of the if (return doenst do it)
    
    pygame.display.update()
    if len(playerPattern) >= len(pattern): ########## ADD IN TO THE GAME
        if pengModeLifeStore == life:
            pygame.time.set_timer(RETURN_NORMAL_EVENT, 1000, 1)
            playerPattern = []
        if pengModeLifeStore != life:
            pengModeLifeStore = life
            pygame.time.set_timer(RETURN_NORMAL_EVENT, 3000, 1)
            playerPattern = []
    
    #     if life != lifeStore:
    #             break
    # if len(playerPattern) == len(pattern) and life == lifeStore:
    #     score = score + 1
    #     pygame.mixer.music.load('./Assets/sounds/ding.wav')
    #     pygame.mixer.music.play()
    #     pygame.time.delay(1500) # wait
    # lifeStore = life
    

# Define the game loop
def game_loop():
    global imageCounter
    global playerPattern
    global forcefieldOpening
    global forcefieldActive
    global pengModeCanShowPattern
    global redColour
    global greenColour
    global yellowColour
    global blueColour
    global redLightColour
    global greenLightColour
    global yellowLightColour
    global blueLightColour
    global forcefieldClosing
    global canRandomPattern
    global canShowPattern
    global pengModeCanShowPattern
    global forcefieldOpening
    global forcefieldActive
    global timeDelay
    global pengPatternCounter
    global pattern
    global boost
    global patternStarted
    global timerHasBeenSet
    global displayBoxColour
    
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == COLOUR_LIGHT_EVENT:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            redColour, redLightColour = ('#800000'), ('#FF0000')
            blueColour, blueLightColour = ('#001E80'), ('#003DFF')
            yellowColour, yellowLightColour = ('#778000'), ('#F0FF00')
            greenColour, greenLightColour = ('#008000'), ('#25FF00')
            displayBoxColour = grey
        if event.type == LIFE_LOSS_LIGHT_EVENT:
            redColour, redLightColour = ('#800000'), ('#FF0000')
            blueColour, blueLightColour = ('#001E80'), ('#003DFF')
            yellowColour, yellowLightColour = ('#778000'), ('#F0FF00')
            greenColour, greenLightColour = ('#008000'), ('#25FF00')
        if event.type == RETURN_NORMAL_EVENT:
            print('now returning to normal - repeating the process')
            forcefieldActive = True
            forcefieldOpening = True
            forcefieldClosing = False
            canRandomPattern = True
            pengModeCanShowPattern = True
            canShowPattern = False
            patternStarted = False
        if event.type == CONTINUE_SHOWING_PATTERN_EVENT:
            print('in')
            print(pengPatternCounter)
            if pengPatternCounter < len(pattern):
                print('first time')
                canRandomPattern = False
                pengModeCanShowPattern = True
                canShowPattern = True
                timerHasBeenSet = False
        if event.type == FINISH_SHOWING_PATTERN_EVENT:
            print('ending the showing, now for user input')
            forcefieldClosing = True
            forcefieldActive = False
            forcefieldOpening = False
        if event.type == BOOST_EVENT: 
            boost = False
            print(imageCounter)
        if event.type == LIFE_LOSS_CONTINUE_EVENT:
            redColour, redLightColour = ('#FF0000'), ('#800000')
            blueColour, blueLightColour = ('#003DFF'), ('#001E80')
            yellowColour, yellowLightColour = ('#F0FF00'), ('#778000')
            greenColour, greenLightColour = ('#25FF00'), ('#008000')
            pygame.time.set_timer(LIFE_LOSS_LIGHT_EVENT, 500, 1)
    
    apply_friction() # Apply friction to the penguin's speed
    apply_gravity() # Apply gravitational force to the penguin's speed
    apply_key() # check if the player presses any movement keys
    update_penguin_position() # Update the penguin's position
    check_pos() # check the penguin's position and bound it inside the viewable area
    if pengModeCanShowPattern == True:
        # forcefieldOpening = True # NNED TO MAKE IT TRUE SONEWHERE ELSE
        forcefieldActive = True
    
        if canRandomPattern == True:
            print('got a random pattern')
            random_pattern() # NOTICE this is called every second - change
            # print('called')
        # print(pattern)
        # print(canShowPattern)
        if canShowPattern == True:
            show_pattern()
            playerPattern = []
        if canShowPattern == False and pengPatternCounter < len(pattern) and pengPatternCounter > 0 and timerHasBeenSet == False:
            print('conitinuer')
            # print(pengPatternCounter)
            # canShowPattern = True############ GET SOME WAY TO TURN  THIS IF OFF ONCE IT IS CALLED AND SOME WAY TO TURN IT BACK ON
            pygame.time.set_timer(CONTINUE_SHOWING_PATTERN_EVENT, timeDelay+250, 1) ### WHOLE GAME WORKS IF THE SECOND NUMBER IS SMALL ENOUGH
            timerHasBeenSet = True
        
    penguin_mode_store_player_guess() # problem solved - because its not being called
        ###### ALL SOLVED  ##### THE PLAYE IS NOW ONLY FROZEN CAUSE ^^^ IS BEING CALLED TOO FAST
    
    ########## NOTE WHEN THE PATTERN IS BEING SHOWN, THE PLAYER SHOULDNT BE ABLE TO TOUCH ANY OF THE BLOCK TO CHOOSE THEIR PATTERN
    
    
    pygame.display.update() # Update the Pygame display


########## BIG PROBLEM #########
# AS OF RIGHT NOW, THE CHECK CHOICE FOR THE LOSE LIFE THIS BREAKS WHEN THE PLAYER GUESSES WRONG ON THE LAST GUESS
# E.G. 1 GUESS, THEY GET IT WRONG, BROKEY
# 2 GUESS, THEY GET THE SECOND ONE WRONG, BROKEY...

render_game_start_page()