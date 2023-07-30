import pygame
import sys
import random
from pygame.locals import *
import csv
import ctypes
import json

# Game Setup
FPS = 60
pygame.init()
window_width = 800
window_height = 600
resizeScale = 1
pygame.mixer.init()

# rgb values of colours used
WHITE = ('#FFFFFF')
GREY = ('#131313')
BLACK = ('#000000')
RED = ('#FF0000')
redLightColour = ('#FF0000')
blueLightColour = ('#003DFF')
yellowLightColour = ('#F0FF00')
greenLightColour = ('#25FF00')
redColour = ('#800000')
blueColour = ('#001E80')
yellowColour = ('#778000')
greenColour = ('#008000')

# load all the images (Every asset needs a "scaled" version so that when resizing the game, variables are premade to store the scaled version)
logo = pygame.image.load('./Assets/simon_logo.png') # 32 x 32
mainPageImageScaled = pygame.transform.scale(logo, (450, 450)) # 14.0625 times larger
startButtonNormal = pygame.image.load('./Assets/main_menu_page_images/start_game_image.png') # 207 x 88
startButtonNormalScaled = pygame.transform.scale(startButtonNormal, (207, 88))
startButtonPressed = pygame.image.load('./Assets/main_menu_page_images/start_game_image_2.png') # 207 x 88
startButtonPressedScaled = pygame.transform.scale(startButtonPressed, (207, 88))
settings = pygame.image.load('./Assets/main_menu_page_images/gear_cog.png') # 547 x 600
settingsScaled = pygame.transform.scale(settings, (64, 70)) # (8.546875 times smaller, )
settingsScaled2 = pygame.transform.scale(settings, (109.4, 120))
leaderboard = pygame.image.load('./Assets/main_menu_page_images/victory_cup.png') # 17 x 17
leaderboardScaled = pygame.transform.scale(leaderboard, (68, 68))
exit = pygame.image.load('./Assets/main_menu_page_images/close_game_2.png') # 26 x 26
exitScaled = pygame.transform.scale(exit, (68, 68))
bgGreen = pygame.image.load('./Assets/main_menu_page_images/bg_green.png') # 400 x 300
bgGreenScaled = pygame.transform.scale(bgGreen, (400, 300))
bgRed = pygame.image.load('./Assets/main_menu_page_images/bg_red.png') # 400 x 300
bgRedScaled = pygame.transform.scale(bgRed, (400, 300))
bgYellow = pygame.image.load('./Assets/main_menu_page_images/bg_yellow.png') # 400 x 300
bgYellowScaled = pygame.transform.scale(bgYellow, (400, 300))
bgBlue = pygame.image.load('./Assets/main_menu_page_images/bg_blue.png') # 400 x 300
bgBlueScaled = pygame.transform.scale(bgBlue, (400, 300))

heartImageFull = pygame.image.load('./Assets/game_images/heart_full.png') # 9 x 9
heartImageFullScaled = pygame.transform.scale(heartImageFull, (36, 36))
heartImageEmpty = pygame.image.load('./Assets/game_images/heart_empty.png') # 9 x 9
heartImageEmptyScaled = pygame.transform.scale(heartImageEmpty, (36, 36))

blueLight = pygame.image.load('./Assets/game_images/blue_light.png') # 9 x 9
blueLightScaled = pygame.transform.scale(blueLight, (225, 225))
blue = pygame.image.load('./Assets/game_images/blue.png') # 9 x 9
blueScaled = pygame.transform.scale(blue, (225, 225))
greenLight = pygame.image.load('./Assets/game_images/green_light.png') # 9 x 9
greenLightScaled = pygame.transform.scale(greenLight, (225, 225))
green = pygame.image.load('./Assets/game_images/green.png') # 9 x 9
greenScaled = pygame.transform.scale(green, (225, 225))
redLight = pygame.image.load('./Assets/game_images/red_light.png') # 9 x 9
redLightScaled = pygame.transform.scale(redLight, (225, 225))
red = pygame.image.load('./Assets/game_images/red.png') # 9 x 9
redScaled = pygame.transform.scale(red, (225, 225))
yellowLight = pygame.image.load('./Assets/game_images/yellow_light.png') # 9 x 9
yellowLightScaled = pygame.transform.scale(yellowLight, (225, 225))
yellow = pygame.image.load('./Assets/game_images/yellow.png') # 9 x 9
yellowScaled = pygame.transform.scale(yellow, (225, 225))

blackGradientScreen = pygame.image.load('./Assets/main_menu_page_images/black_bg.png') # 800 x 600
blackGradientScreenScaled = pygame.transform.scale(blackGradientScreen, (800, 600))
bg = pygame.Rect(50, 100, 700, 450)

soundOn = pygame.image.load('./Assets/setting_images/sound_on.png') # 18 x 18
soundOnScaled = pygame.transform.scale(soundOn, (54, 54))
soundOff = pygame.image.load('./Assets/setting_images/sound_off.png') # 29 x 29
soundOffScaled = pygame.transform.scale(soundOff, (87, 87))
soundSlider = pygame.image.load('./Assets/setting_images/slider.png') # 13 x 13
soundSliderScaled = pygame.transform.scale(soundSlider, (26, 26))

homeButton = pygame.image.load('./Assets/end_game_images/home_button.png') # 20 x 20
homeButtonScaled = pygame.transform.scale(homeButton, (100, 100))
restartButton = pygame.image.load('./Assets/end_game_images/restart_button.png') # 9 x 9
restartButtonScaled = pygame.transform.scale(restartButton, (95, 95))
restartButtonWhite = pygame.image.load('./Assets/end_game_images/restart_button_white.png') # 9 x 9
restartButtonWhiteScaled = pygame.transform.scale(restartButtonWhite, (50, 50))

nextPage = pygame.image.load('./Assets/info_images/page_left.png') # 17 x 17
nextPageScaled = pygame.transform.scale(nextPage, (51, 51))
backPage = pygame.image.load('./Assets/info_images/page_right.png') # 17 x 17
backPageScaled = pygame.transform.scale(backPage, (51, 51))

# penguin mode images
bobbingBottom = pygame.image.load('./Assets/penguin_mode/bobbing_bottom.png') # 15 x 14
bobbingBottomScaled = pygame.transform.scale(bobbingBottom, (bobbingBottom.get_width()*3, bobbingBottom.get_height()*3))
bobbingTop = pygame.image.load('./Assets/penguin_mode/bobbing_top.png') # 15 x 14
bobbingTopScaled = pygame.transform.scale(bobbingTop, (bobbingTop.get_width()*3, bobbingTop.get_height()*3))

lookingUp = pygame.image.load('./Assets/penguin_mode/looking_up.png') # 12 x 15
lookingUpScaled = pygame.transform.scale(lookingUp, (lookingUp.get_width()*3, lookingUp.get_height()*3))
lookingUpBlueLit = pygame.image.load('./Assets/penguin_mode/looking_up_blue_lit.png') # 12 x 15
lookingUpBlueLitScaled = pygame.transform.scale(lookingUpBlueLit, (lookingUpBlueLit.get_width()*3, lookingUpBlueLit.get_height()*3))
lookingUpGreenLit = pygame.image.load('./Assets/penguin_mode/looking_up_green_lit.png') # 12 x 15
lookingUpGreenLitScaled = pygame.transform.scale(lookingUpGreenLit, (lookingUpGreenLit.get_width()*3, lookingUpGreenLit.get_height()*3))
lookingUpRedLit = pygame.image.load('./Assets/penguin_mode/looking_up_red_lit.png') # 12 x 15
lookingUpRedLitScaled = pygame.transform.scale(lookingUpRedLit, (lookingUpRedLit.get_width()*3, lookingUpRedLit.get_height()*3))
lookingUpYellowLit = pygame.image.load('./Assets/penguin_mode/looking_up_yellow_lit.png') # 12 x 15
lookingUpYellowLitScaled = pygame.transform.scale(lookingUpYellowLit, (lookingUpYellowLit.get_width()*3, lookingUpYellowLit.get_height()*3))

layingDownL = pygame.image.load('./Assets/penguin_mode/laying_down_left.png') # 17 x 7
layingDownLScaled = pygame.transform.scale(layingDownL, (layingDownL.get_width()*3, layingDownL.get_height()*3))
layingDownR = pygame.image.load('./Assets/penguin_mode/laying_down_right.png') # 17 x 7
layingDownRScaled = pygame.transform.scale(layingDownR, (layingDownR.get_width()*3, layingDownR.get_height()*3))

lookingLeft = pygame.image.load('./Assets/penguin_mode/looking_left.png') # 13 x 13
lookingLeftScaled = pygame.transform.scale(lookingLeft, (lookingLeft.get_width()*3, lookingLeft.get_height()*3))
lookingLeftBlue = pygame.image.load('./Assets/penguin_mode/looking_left_blue_lit.png') # 13 x 13
lookingLeftBlueScaled = pygame.transform.scale(lookingLeftBlue, (lookingLeftBlue.get_width()*3, lookingLeftBlue.get_height()*3))
lookingLeftGreen = pygame.image.load('./Assets/penguin_mode/looking_left_green_lit.png') # 13 x 13
lookingLeftGreenScaled = pygame.transform.scale(lookingLeftGreen, (lookingLeftGreen.get_width()*3, lookingLeftGreen.get_height()*3))
lookingLeftRed = pygame.image.load('./Assets/penguin_mode/looking_left_red_lit.png') # 13 x 13
lookingLeftRedScaled = pygame.transform.scale(lookingLeftRed, (lookingLeftRed.get_width()*3, lookingLeftRed.get_height()*3))
lookingLeftYellow = pygame.image.load('./Assets/penguin_mode/looking_left_yellow_lit.png') # 13 x 13
lookingLeftYellowScaled = pygame.transform.scale(lookingLeftYellow, (lookingLeftYellow.get_width()*3, lookingLeftYellow.get_height()*3))

lookingRight = pygame.image.load('./Assets/penguin_mode/looking_right.png') # 13 x 13
lookingRightScaled = pygame.transform.scale(lookingRight, (lookingRight.get_width()*3, lookingRight.get_height()*3))
lookingRightBlue = pygame.image.load('./Assets/penguin_mode/looking_right_blue_lit.png') # 13 x 13
lookingRightBlueScaled = pygame.transform.scale(lookingRightBlue, (lookingRightBlue.get_width()*3, lookingRightBlue.get_height()*3))
lookingRightGreen = pygame.image.load('./Assets/penguin_mode/looking_right_green_lit.png') # 13 x 13
lookingRightGreenScaled = pygame.transform.scale(lookingRightGreen, (lookingRightGreen.get_width()*3, lookingRightGreen.get_height()*3))
lookingRightRed = pygame.image.load('./Assets/penguin_mode/looking_right_red_lit.png') # 13 x 13
lookingRightRedScaled = pygame.transform.scale(lookingRightRed, (lookingRightRed.get_width()*3, lookingRightRed.get_height()*3))
lookingRightYellow = pygame.image.load('./Assets/penguin_mode/looking_right_yellow_lit.png') # 13 x 13
lookingRightYellowScaled = pygame.transform.scale(lookingRightYellow, (lookingRightYellow.get_width()*3, lookingRightYellow.get_height()*3))

platform = pygame.image.load('./Assets/penguin_mode/platform.png') # 26 x 4
platformScaled = pygame.transform.scale(platform, (platform.get_width()*3, platform.get_height()*3))

colourWidth = 15
colourLength = 175
offsetX = 125
offsetY = 25
redBox1 = pygame.Rect(int(offsetX * resizeScale), int(offsetY * resizeScale), int(colourLength * resizeScale), int(colourWidth * resizeScale))
redBox2 = pygame.Rect(int(offsetX * resizeScale), int(offsetY * resizeScale), int(colourWidth * resizeScale), int(colourLength * resizeScale))
yellowBox1 = pygame.Rect(int(offsetX * resizeScale), int((window_height - offsetY - colourLength) * resizeScale), int(colourWidth * resizeScale), int(colourLength * resizeScale))
yellowBox2 = pygame.Rect(int(offsetX * resizeScale), int((window_height - offsetY - colourWidth) * resizeScale), int(colourLength * resizeScale), int(colourWidth * resizeScale))
greenBox1 = pygame.Rect(int((window_width - offsetX - colourLength) * resizeScale), int(offsetY * resizeScale), int(colourLength * resizeScale), int(colourWidth * resizeScale))
greenBox2 = pygame.Rect(int((window_width - offsetX - colourWidth) * resizeScale), int(offsetY * resizeScale), int(colourWidth * resizeScale), int(colourLength * resizeScale))
blueBox1 = pygame.Rect(int((window_width - offsetX - colourLength) * resizeScale), int((window_height - offsetY - colourWidth) * resizeScale), int(colourLength * resizeScale), int(colourWidth * resizeScale))
blueBox2 = pygame.Rect(int((window_width - offsetX - colourWidth) * resizeScale), int((window_height - offsetY - colourLength) * resizeScale), int(colourWidth * resizeScale), int(colourLength * resizeScale))

# lightning forcefield images
forcefield0 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField0.png') # 170 x 170
forcefield0Scaled = pygame.transform.scale(forcefield0, (170, 170))
forcefield1 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField1.png') # 170 x 170
forcefield1Scaled = pygame.transform.scale(forcefield1, (170, 170))
forcefield2 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField2.png') # 170 x 170
forcefield2Scaled = pygame.transform.scale(forcefield2, (170, 170))
forcefield3 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField3.png') # 170 x 170
forcefield3Scaled = pygame.transform.scale(forcefield3, (170, 170))
forcefield4 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField4.png') # 170 x 170
forcefield4Scaled = pygame.transform.scale(forcefield4, (170, 170))
forcefield5 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField5.png') # 170 x 170
forcefield5Scaled = pygame.transform.scale(forcefield5, (170, 170))
forcefield6 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField6.png') # 170 x 170
forcefield6Scaled = pygame.transform.scale(forcefield6, (170, 170))
forcefield7 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField7.png') # 170 x 170
forcefield7Scaled = pygame.transform.scale(forcefield7, (170, 170))
forcefield8 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField8.png') # 170 x 170
forcefield8Scaled = pygame.transform.scale(forcefield8, (170, 170))
forcefield9 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField9.png') # 170 x 170
forcefield9Scaled = pygame.transform.scale(forcefield9, (170, 170))
forcefield10 = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField10.png') # 170 x 170
forcefield10Scaled = pygame.transform.scale(forcefield10, (170, 170))
empty = pygame.image.load('./Assets/penguin_mode/lightning_forcefield/lightningForceField11.png') # 170 x 170
emptyScaled = pygame.transform.scale(empty, (170, 170))

# rocket fire images
redFire0 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_0.png') # 10 x 19
redFire0Scaled = pygame.transform.scale(redFire0, (redFire0.get_width()*3, redFire0.get_height()*3))
redFire1 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_1.png') # 10 x 19
redFire1Scaled = pygame.transform.scale(redFire1, (redFire1.get_width()*3, redFire1.get_height()*3))
redFire2 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_2.png') # 10 x 19
redFire2Scaled = pygame.transform.scale(redFire2, (redFire2.get_width()*3, redFire2.get_height()*3))
redFire3 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_3.png') # 10 x 19
redFire3Scaled = pygame.transform.scale(redFire3, (redFire3.get_width()*3, redFire3.get_height()*3))
redFire4 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_4.png') # 10 x 19
redFire4Scaled = pygame.transform.scale(redFire4, (redFire4.get_width()*3, redFire4.get_height()*3))
redFire5 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_5.png') # 10 x 19
redFire5Scaled = pygame.transform.scale(redFire5, (redFire5.get_width()*3, redFire5.get_height()*3))
redFire6 = pygame.image.load('./Assets/penguin_mode/red_fire/red_fire_6.png') # 10 x 19
redFire6Scaled = pygame.transform.scale(redFire6, (redFire6.get_width()*3, redFire6.get_height()*3))

blueFire0 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_0.png') # 10 x 19
blueFire0Scaled = pygame.transform.scale(blueFire0, (blueFire0.get_width()*3, blueFire0.get_height()*3))
blueFire1 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_1.png') # 10 x 19
blueFire1Scaled = pygame.transform.scale(blueFire1, (blueFire1.get_width()*3, blueFire1.get_height()*3))
blueFire2 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_2.png') # 10 x 19
blueFire2Scaled = pygame.transform.scale(blueFire2, (blueFire2.get_width()*3, blueFire2.get_height()*3))
blueFire3 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_3.png') # 10 x 19
blueFire3Scaled = pygame.transform.scale(blueFire3, (blueFire3.get_width()*3, blueFire3.get_height()*3))
blueFire4 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_4.png') # 10 x 19
blueFire4Scaled = pygame.transform.scale(blueFire4, (blueFire4.get_width()*3, blueFire4.get_height()*3))
blueFire5 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_5.png') # 10 x 19
blueFire5Scaled = pygame.transform.scale(blueFire5, (blueFire5.get_width()*3, blueFire5.get_height()*3))
blueFire6 = pygame.image.load('./Assets/penguin_mode/blue_fire/blue_fire_6.png') # 10 x 19
blueFire6Scaled = pygame.transform.scale(blueFire6, (blueFire6.get_width()*3, blueFire6.get_height()*3))

bomb = pygame.image.load("./Assets/penguin_mode/bomb.png") # 9 x 11
bombScaled = pygame.transform.scale(bomb, (bomb.get_width() * 3, bomb.get_height() * 3))
cherry = pygame.image.load("./Assets/penguin_mode/cherry.png") # 25 x 21
cherryScaled = pygame.transform.scale(cherry, (cherry.get_width() * 2, cherry.get_height() * 2))
petrol = pygame.image.load("./Assets/penguin_mode/petrol.png") # 11 x 16
petrolScaled = pygame.transform.scale(petrol, (petrol.get_width() * 3, petrol.get_height() * 3))
petrolLifeScaled = pygame.transform.scale(petrol, (petrol.get_width() * 5, petrol.get_height() * 5))

nothing = pygame.image.load('./Assets/nothing.png') # 32 x 32
nothingScaled = pygame.transform.scale(nothing, (32, 32))

# load all the fonts
GAMEPLAY_FONT = './Assets/fonts/Press_Start_2P/PressStart2P-Regular.ttf'
gameFontStart = pygame.font.Font(GAMEPLAY_FONT, 50) # size 50 font
gameFont = pygame.font.Font(GAMEPLAY_FONT, 20) # size 20 font
gameFontSubtitle = pygame.font.Font(GAMEPLAY_FONT, 24) # size 24 font
gameFontEnd = pygame.font.Font(GAMEPLAY_FONT, 40) # size 40 font
gameFontCred = pygame.font.Font(GAMEPLAY_FONT, 30) # size 30 font

# initialise the window of the game
window = pygame.display.set_mode((window_width, window_height)) # creates the window
pygame.display.set_caption('Simon: The Game') # sets the name of the window
pygame.display.set_icon(logo) # sets the window's logo to the image

# store settings
settingsDict = {
    "up": K_UP,
    "down": K_DOWN,
    "left": K_LEFT,
    "right": K_RIGHT,
    "boost": K_SPACE,
    "unlockedExtraModes": False
}

# Load settings
try:
    with open("settings.json", "r") as file:
        settingsDict = json.load(file)
except FileNotFoundError:
    print("Settings file not found. Using default settings.")
except json.JSONDecodeError:
    print("Error decoding settings file. Using default settings.")

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
sliderX = int(resizeScale * 692)
soundImage = soundOnScaled
soundLocation = (int(resizeScale * 100), int(resizeScale * 200))
gameMode = "Normal"
gravity = 0.1
boost = False
up = 0.11
imageCounter = 0
soundPlayed = False

# Set new event types
BOOST_EVENT = pygame.event.custom_type()
COLOUR_LIGHT_EVENT = pygame.event.custom_type()
FINISH_SHOWING_PATTERN_EVENT = pygame.event.custom_type()
RETURN_NORMAL_EVENT = pygame.event.custom_type()
CONTINUE_SHOWING_PATTERN_EVENT = pygame.event.custom_type()
LIFE_LOSS_LIGHT_EVENT = pygame.event.custom_type()
LIFE_LOSS_CONTINUE_EVENT = pygame.event.custom_type()

# Load Sounds Used Globally
hoverOverButtonSound = pygame.mixer.Sound("./Assets/sounds/hover over button.wav")
mainMenuTune = pygame.mixer.Sound('./Assets/sounds/main menu tune.wav')
pygame.mixer.Channel(1).play(mainMenuTune, -1)

# Set up the penguin
pengSpeed = [0, 0]
pengImage = bobbingBottomScaled
pengPos = [window_width//2 - pengImage.get_width()/2, window_height//2]
pengImageLast = bobbingTopScaled
rocketFireAnimation = nothingScaled
fireSlideRed = [redFire0Scaled, redFire1Scaled, redFire2Scaled, redFire3Scaled, redFire4Scaled, redFire5Scaled, redFire6Scaled]
fireSlideBlue = [blueFire0Scaled, blueFire1Scaled, blueFire2Scaled, blueFire3Scaled, blueFire4Scaled, blueFire5Scaled, blueFire6Scaled]
forcefieldSlide = [emptyScaled, forcefield0Scaled, forcefield1Scaled, forcefield2Scaled, forcefield3Scaled, forcefield4Scaled, forcefield5Scaled, forcefield6Scaled, forcefield7Scaled, forcefield8Scaled, forcefield9Scaled, forcefield10Scaled]
slideNum = 0
showLives = False
pengRect = pygame.Rect(pengPos[0], pengPos[1], pengImage.get_width(), pengImage.get_height())
platformRect = pygame.Rect(window_width/2 - platformScaled.get_width()/2, window_height/2, platformScaled.get_width(), platformScaled.get_height())
forcefieldNum = 0
forcefieldActive = True
forcefieldOpening = True
forcefieldClosing = False
canRandomPattern = True
pengPatternCounter = 0
patternStarted = False
timerHasBeenSet = False
pengModeLifeStore = life
displayBoxColour = GREY
all_items = []

pengModeCanShowPattern = True
canShowPattern = False

##################
# Game Functions #
##################

############### Add screen to allow player to change their player inputs

def sort_scores(file):
    sortedFile = []
    scoreFile = open(f"./Files/high_scores_{file}.csv")
    fileReader = csv.reader(scoreFile, delimiter=",")
    for Score, Name in fileReader:
        sortedFile = sorted(fileReader, key=lambda row: int(row[0]), reverse=True)
    scoreFile.close()

    scoreFile2 = open(f"./Files/high_scores_{file}.csv", "w", newline='')
    fileWriter = csv.writer(scoreFile2, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
    txtFile = open(f"./Files/high_scores_{file}.txt", "w", newline='')
    txtFileWriter = csv.writer(txtFile, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
    fileWriter.writerow(['Score', 'Name'])
    for i, j in enumerate(sortedFile):
        fileWriter.writerow(sortedFile[i])
        txtFileWriter.writerow(sortedFile[i])
    scoreFile2.close()
    txtFile.close()


def remove_transparent_pixels(image, blitLocation): # makes it so that if the player is hovering over a transparent part of an image, the cursor wont change to a hand image
    global soundPlayed
    pos = pygame.mouse.get_pos()
    clickImage = image.convert_alpha()
    try: # only work if the click isnt in a transparent area
        mask = pygame.mask.from_surface(clickImage)
        if mask.get_at((pos[0]-blitLocation[0], pos[1]-blitLocation[1])):
            if image.get_rect(topleft=blitLocation).collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if not soundPlayed:
                    pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                    soundPlayed = True
                return True
        else:
            soundPlayed = False
    except IndexError:  # if the click is in a transparent area, dont worry about it
        pass


def render_game_start_page(): # main screen page
    waiting = True
    global score
    score = 0
    logoBob = 50 # where the logo starts at (y-axis)
    titleText = gameFontStart.render('SIMON', True, WHITE) # write the words
    bobDirection = True # true = down, false = up
    buttonImage = startButtonNormalScaled
    
    try:
        sort_scores("Easy")
        sort_scores("Normal")
        sort_scores("Hard")
        sort_scores("Penguin")
        sort_scores("Ben")
        sort_scores("Insane")
    except PermissionError:
        pass
    while waiting:
        for event in pygame.event.get(): # if the user closes the window, close the game
            if event.type == QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if remove_transparent_pixels(buttonImage, ((int(window_width * resizeScale)/2 - buttonImage.get_width()/2), int((window_height-120) * resizeScale))):
                    buttonImage = startButtonPressedScaled
                if remove_transparent_pixels(settingsScaled, (int((window_width-90) * resizeScale), int(30 * resizeScale))):
                    render_settings_screen()
                if exitScaled.get_rect(topleft=(int(resizeScale * 25), int(resizeScale * 507))).collidepoint(pygame.mouse.get_pos()):
                    quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if remove_transparent_pixels(leaderboardScaled, (int((window_width-88) * resizeScale), int((window_height-90) * resizeScale))):
                    render_leaderboard_screen()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and buttonImage == startButtonPressedScaled:
                if remove_transparent_pixels(buttonImage, ((int(window_width * resizeScale)/2 - buttonImage.get_width()/2), int((window_height-120) * resizeScale))):
                    buttonImage = startButtonNormalScaled
                    pygame.mouse.set_cursor()
                    waiting = False
    
        # set background grey
        window.fill(GREY)        
        remove_transparent_pixels(buttonImage, ((int(window_width * resizeScale)/2 - buttonImage.get_width()/2), int((window_height-120) * resizeScale)))
        remove_transparent_pixels(settingsScaled, (int((window_width-90) * resizeScale), int(30 * resizeScale)))
        remove_transparent_pixels(leaderboardScaled, (int((window_width-88) * resizeScale), int((window_height-90) * resizeScale)))
        if exitScaled.get_rect(topleft=(int(resizeScale * 25), int(resizeScale * 507))).collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        if not exitScaled.get_rect(topleft=(int(resizeScale * 25), int(resizeScale * 507))).collidepoint(pygame.mouse.get_pos()) and not remove_transparent_pixels(buttonImage, ((int(window_width * resizeScale)/2 - buttonImage.get_width()/2), int((window_height-120) * resizeScale))) and not remove_transparent_pixels(settingsScaled, (int((window_width-90) * resizeScale), int(30 * resizeScale))) and not remove_transparent_pixels(leaderboardScaled, (int((window_width-88) * resizeScale), int((window_height-90) * resizeScale))):
            pygame.mouse.set_cursor()
            buttonImage = startButtonNormalScaled

        # display text and images
        window.blit(bgYellowScaled, (int(0 * resizeScale), int(0 * resizeScale)))
        window.blit(bgBlueScaled, (int(0 * resizeScale), int(302 * resizeScale)))
        window.blit(bgRedScaled, (int(402 * resizeScale), int(0 * resizeScale)))
        window.blit(bgGreenScaled, (int(402 * resizeScale), int(302 * resizeScale)))
        window.blit(titleText, (int(279 * resizeScale), int(50 * resizeScale)))
        window.blit(mainPageImageScaled, (int(175 * resizeScale), int(logoBob * resizeScale)))
        window.blit(buttonImage, ((int(800 * resizeScale) - buttonImage.get_width())/2, int(480 * resizeScale)))
        window.blit(settingsScaled, (int((window_width-90) * resizeScale), int(30 * resizeScale)))
        window.blit(leaderboardScaled, (int((window_width-88) * resizeScale), int(510 * resizeScale)))
        window.blit(exitScaled, (int(resizeScale * 25), int(resizeScale * 507)))
        ### draw an exit image and add click checking for it
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
    modeBox1 = pygame.Rect(int(225 * resizeScale), int(200 * resizeScale), int(350 * resizeScale), int(75 * resizeScale))
    modeBox2 = pygame.Rect(int(225 * resizeScale), int(300 * resizeScale), int(350 * resizeScale), int(75 * resizeScale))
    modeBox3 = pygame.Rect(int(225 * resizeScale), int(400 * resizeScale), int(350 * resizeScale), int(75 * resizeScale))
    credBg = pygame.Rect(int(150 * resizeScale), int(50 * resizeScale), int(500 * resizeScale), int(100 * resizeScale))
    chooseModeText = gameFontEnd.render('Choose Mode', True, WHITE)
    chooseModeScreen = 1
    global gameMode
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if remove_transparent_pixels(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale))):
                    chooseModeScreen = chooseModeScreen - 1
                    if chooseModeScreen < 1:
                        chooseModeScreen = 1
                if settingsDict["unlockedExtraModes"] == True and remove_transparent_pixels(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale))):
                    chooseModeScreen = chooseModeScreen + 1
                    if chooseModeScreen > 2:
                        chooseModeScreen = 2
                if remove_transparent_pixels(homeButtonScaled, (int(600 * resizeScale), int(400 * resizeScale))):
                    render_game_start_page()
                if chooseModeScreen == 1:
                    if modeBox1.collidepoint(pygame.mouse.get_pos()):
                        gameMode = "Easy"
                        waiting = False
                    if modeBox2.collidepoint(pygame.mouse.get_pos()):
                        gameMode = "Normal"
                        waiting = False
                    if modeBox3.collidepoint(pygame.mouse.get_pos()):
                        gameMode = "Hard"
                        waiting = False
                if chooseModeScreen == 2:
                    if modeBox1.collidepoint(pygame.mouse.get_pos()):
                        gameMode = "Penguin"
                        waiting = False
        window.fill(GREY)
        window.blit(blackGradientScreenScaled, (0, 0))
        pygame.draw.rect(window, BLACK, bg)
        if resizeScale < 0.5:
            lineThickness = 1
        else:
            lineThickness = int(resizeScale * 2)
        pygame.draw.rect(window, WHITE, bg, lineThickness)
        pygame.draw.rect(window, BLACK, credBg)
        pygame.draw.rect(window, WHITE, credBg, lineThickness)
        window.blit(homeButtonScaled, (int(600 * resizeScale), int(400 * resizeScale)))
        window.blit(chooseModeText, (int(resizeScale * window_width)/2-(chooseModeText.get_width()/2)+int(resizeScale * 5), int(85 * resizeScale)))
        remove_transparent_pixels(homeButtonScaled, (int(600 * resizeScale), int(400 * resizeScale)))
        if chooseModeScreen == 1:
            if settingsDict["unlockedExtraModes"] == True:
                window.blit(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale)))
            for i in range(3):
                if i == 0:
                    modeBoxColour = WHITE
                    modeText = 'Easy'
                    textYPos = 225
                    modeBox = modeBox1
                elif i == 1:
                    modeBoxColour = WHITE
                    modeText = 'Normal'
                    textYPos = 325
                    modeBox = modeBox2
                elif i == 2:
                    modeBoxColour = WHITE
                    modeText = 'Hard'
                    textYPos = 425
                    modeBox = modeBox3
                pygame.draw.rect(window, BLACK, modeBox)
                if modeBox.collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    modeBoxColour = RED
                    if not soundPlayed:
                        pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                        soundPlayed = True
                else:
                    modeBoxColour = WHITE
                    soundPlayed = False
                if resizeScale < 0.5:
                    lineThickness = 1
                else:
                    lineThickness = int(resizeScale * 2)
                pygame.draw.rect(window, modeBoxColour, modeBox, lineThickness)
                modeTextDisplay = gameFontCred.render(modeText, True, WHITE)
                window.blit(modeTextDisplay, (int(resizeScale * window_width)/2-(modeTextDisplay.get_width()/2), int(textYPos * resizeScale)))
            if settingsDict["unlockedExtraModes"] == True:
                remove_transparent_pixels(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale)))
                if not remove_transparent_pixels(homeButtonScaled, (int(600 * resizeScale), int(400 * resizeScale))) and not remove_transparent_pixels(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale))) and not modeBox1.collidepoint(pygame.mouse.get_pos()) and not modeBox2.collidepoint(pygame.mouse.get_pos()) and not modeBox3.collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor()
            elif not remove_transparent_pixels(homeButtonScaled, (int(600 * resizeScale), int(400 * resizeScale))) and not modeBox1.collidepoint(pygame.mouse.get_pos()) and not modeBox2.collidepoint(pygame.mouse.get_pos()) and not modeBox3.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor()
        if chooseModeScreen == 2:
            window.blit(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale)))
            for i in range(3):
                if i == 0:
                    modeBoxColour = WHITE
                    modeText = 'Penguin'
                    textYPos = 225
                    modeBox = modeBox1
                elif i == 1:
                    modeBoxColour = WHITE
                    modeText = ''
                    textYPos = 325
                    modeBox = modeBox2
                elif i == 2:
                    modeBoxColour = WHITE
                    modeText = ''
                    textYPos = 425
                    modeBox = modeBox3
                pygame.draw.rect(window, BLACK, modeBox)
                if modeBox.collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    modeBoxColour = RED
                    if not soundPlayed:
                        pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                        soundPlayed = True
                else:
                    modeBoxColour = WHITE
                    soundPlayed = False
                if resizeScale < 0.5:
                    lineThickness = 1
                else:
                    lineThickness = int(resizeScale * 2)
                pygame.draw.rect(window, modeBoxColour, modeBox, lineThickness)
                modeTextDisplay = gameFontCred.render(modeText, True, WHITE)
                window.blit(modeTextDisplay, (int(resizeScale * window_width)/2-(modeTextDisplay.get_width()/2), int(textYPos * resizeScale)))
            remove_transparent_pixels(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale)))
            if not remove_transparent_pixels(homeButtonScaled, (int(600 * resizeScale), int(400 * resizeScale))) and not remove_transparent_pixels(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale))) and not modeBox1.collidepoint(pygame.mouse.get_pos()) and not modeBox2.collidepoint(pygame.mouse.get_pos()) and not modeBox3.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor()
        pygame.display.update()
    while running:
        if gameMode == "Easy":
            pygame.mixer.Channel(1).stop()
            pygame.mixer.Channel(2).stop()
            random_pattern()
            show_pattern()
            store_player_guess()
        if gameMode == "Normal":
            pygame.mixer.Channel(1).stop()
            pygame.mixer.Channel(2).stop()
            random_pattern()
            show_pattern()
            store_player_guess()
        if gameMode == "Hard":
            pygame.mixer.Channel(1).stop()
            pygame.mixer.Channel(2).stop()
            random_pattern()
            show_pattern()
            store_player_guess()
        if gameMode == "Penguin":
            pygame.mixer.Channel(1).stop()
            pygame.mixer.Channel(2).stop()
            peng_flying_game_mode()


def render_game_simon_play_page(yellowClickBlock = yellowScaled, blueClickBlock = blueScaled, greenClickBlock = greenScaled, redClickBlock = redScaled):
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
    window.fill(GREY)
    score_text = gameFont.render('Score: ' + str(score), True, WHITE)
    window.blit(score_text, (int(50 * resizeScale), int(50 * resizeScale)))
    window.blit(heart1, (int((window_width-36-36-36-5-5-50) * resizeScale), int(50 * resizeScale)))
    window.blit(heart2, (int((window_width-36-36-5-50) * resizeScale), int(50 * resizeScale)))
    window.blit(heart3, (int((window_width-36-50) * resizeScale), int(50 * resizeScale)))
    window.blit(yellowClickBlock, (int(175 * resizeScale), int(300 * resizeScale)))
    window.blit(blueClickBlock, (int(400 * resizeScale), int(300 * resizeScale)))
    window.blit(greenClickBlock, (int(400 * resizeScale), int(75 * resizeScale)))
    window.blit(redClickBlock, (int(175 * resizeScale), int(75 * resizeScale)))
    
    if gameMode == "Easy":
        window.blit(restartButtonWhiteScaled, (int(resizeScale * 30), int(resizeScale * 520)))
        # if restartButtonWhiteScaled.get_rect(topleft=(int(resizeScale * 30), int(resizeScale * 520))).collidepoint(pygame.mouse.get_pos()):
        tempFont = pygame.font.Font(None, int(24 * resizeScale))
        notifText = tempFont.render('Replay Pattern (Lose one score.)', True, WHITE)
        window.blit(notifText, (int(90 * resizeScale), int(550 * resizeScale)))
        # restartButtonScaled.get_rect(topleft=(int(421 * resizeScale), int(300 * resizeScale)))
    #########
    # add a replay choice button for easy mode
    #########
    
    pygame.display.update()


def random_pattern():
    global canRandomPattern
    global flagForRestart
    pattern.append(random.randint(1, 4))
    print(pattern)
    canRandomPattern = False
    flagForRestart = True


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
    global pengImage
    colourSound = pygame.mixer.Sound(f'./Assets/sounds/{name}.wav')
    pygame.mixer.Channel(2).play(colourSound)
    if gameMode == "Easy" or gameMode == "Normal" or gameMode == "Hard":
        pygame.time.delay(timeDelay) # current set time delay (faster as the game progresses)
        render_game_simon_play_page(yellowClickBlock = yellowScaled, blueClickBlock = blueScaled, greenClickBlock = greenScaled, redClickBlock = redScaled) # move it back into the "all dark" state
        pygame.mixer.Channel(2).stop()
    if gameMode == "Penguin":
        if name == 'red_a':
            pengImage = lookingUpRedLitScaled
        elif name == 'green_e-lower':
            pengImage = lookingUpGreenLitScaled
        elif name == 'yellow_c-sharp':
            pengImage = lookingUpYellowLitScaled
        elif name == 'blue_e-upper':
            pengImage = lookingUpBlueLitScaled
        patternStarted = True
        pygame.time.set_timer(COLOUR_LIGHT_EVENT, timeDelay, 1)


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
    global timeDelay
    
    timeDelay = 500 - 100 * int(len(pattern) / 5) # changing it to an integer makes it round down if is float
    if timeDelay <= 100:
        print('now 100')
        timeDelay = 100
    
    if gameMode == "Hard":
        timeDelay = 400 - 100 * int(len(pattern) / 3) # changing it to an integer makes it round down if is float
        if timeDelay <= 100:
            print('now 100')
            timeDelay = 100
    print(timeDelay)
    
    if gameMode == "Easy" or gameMode == "Normal" or gameMode == "Hard":
        render_game_simon_play_page(yellowClickBlock = yellowScaled, blueClickBlock = blueScaled, greenClickBlock = greenScaled, redClickBlock = redScaled)
        pygame.time.delay(300)
        
        for x in pattern:
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
            if x == 1: # 1 = red
                render_game_simon_play_page(yellowClickBlock = yellowScaled, blueClickBlock = blueScaled, greenClickBlock = greenScaled, redClickBlock = redLightScaled) # change it into light mode
                colour_light('red_a')
            elif x == 2: # 2 = green
                render_game_simon_play_page(yellowClickBlock = yellowScaled, blueClickBlock = blueScaled, greenClickBlock = greenLightScaled, redClickBlock = redScaled) # change it into light mode
                colour_light('green_e-lower')
            elif x == 3: # 3 = yellow
                render_game_simon_play_page(yellowClickBlock = yellowLightScaled, blueClickBlock = blueScaled, greenClickBlock = greenScaled, redClickBlock = redScaled) # change it into light mode
                colour_light('yellow_c-sharp')
            elif x == 4: # 4 = blue
                render_game_simon_play_page(yellowClickBlock = yellowScaled, blueClickBlock = blueLightScaled, greenClickBlock = greenScaled, redClickBlock = redScaled) # change it into light mode
                colour_light('blue_e-upper')
            print(pattern)
            pygame.time.delay(timeDelay)
    
    if gameMode == 'Penguin' and pengPatternCounter < len(pattern):
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
    if gameMode == 'Penguin' and pengPatternCounter >= len(pattern):
        if pengModeLifeStore == life:
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
    blueScaledPos = (int(resizeScale * 400), int(resizeScale * 300))
    greenScaledPos = (int(resizeScale * 400), int(resizeScale * 75))
    redScaledPos = (int(resizeScale * 175), int(resizeScale * 75)) # location theyre blitted at
    yellowScaledPos = (int(resizeScale * 175), int(resizeScale * 300))
    
    while len(playerPattern) < len(pattern): # so that we check each item of the pattern
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gameMode == "Easy":
                    if restartButtonWhiteScaled.get_rect(topleft=(int(resizeScale * 30), int(resizeScale * 520))).collidepoint(pygame.mouse.get_pos()):
                        score = score - 1
                        show_pattern()
                try: # only work if the click isnt in a transparent area
                    mask = pygame.mask.from_surface(clickRedScaled)
                    if mask.get_at((event.pos[0]-redScaledPos[0], event.pos[1]-redScaledPos[1])):
                        render_game_simon_play_page(yellowClickBlock = yellowScaled, blueClickBlock = blueScaled, greenClickBlock = greenScaled, redClickBlock = redLightScaled) # change it into light mode
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
                        render_game_simon_play_page(yellowClickBlock = yellowScaled, blueClickBlock = blueScaled, greenClickBlock = greenLightScaled, redClickBlock = redScaled) # change it into light mode
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
                        render_game_simon_play_page(yellowClickBlock = yellowLightScaled, blueClickBlock = blueScaled, greenClickBlock = greenScaled, redClickBlock = redScaled) # change it into light mode
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
                        render_game_simon_play_page(yellowClickBlock = yellowScaled, blueClickBlock = blueLightScaled, greenClickBlock = greenScaled, redClickBlock = redScaled) # change it into light mode
                        colour_light('blue_e-upper')
                        playerPattern.append(4) # add it to the end of the array
                        check_pattern(playerPattern)
                        if life != lifeStore:
                            break
                except IndexError:  # if the click is in a transparent area, dont worry about it
                    pass
        if restartButtonWhiteScaled.get_rect(topleft=(int(resizeScale * 30), int(resizeScale * 520))).collidepoint(pygame.mouse.get_pos()):
            # tempFont = pygame.font.Font(None, int(24 * resizeScale))
            # notifText = tempFont.render('Replay Pattern (Lose one score.)', True, WHITE)
            # window.blit(notifText, (int(140 * resizeScale), int(535 * resizeScale)))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if life != lifeStore:
            break
        if not restartButtonWhiteScaled.get_rect(topleft=(int(resizeScale * 30), int(resizeScale * 520))).collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor()

    if len(playerPattern) == len(pattern) and life == lifeStore:
        score = score + 1
        pygame.time.delay(500) # wait
        dingSound = pygame.mixer.Sound('./Assets/sounds/ding.wav')
        pygame.mixer.Channel(2).play(dingSound)
        pygame.time.delay(1000) # wait
    lifeStore = life


def life_loss():
    beepBeepBeepSound = pygame.mixer.Sound('./Assets/sounds/beep_beep_beep.wav')
    pygame.mixer.Channel(2).play(beepBeepBeepSound)
    render_game_simon_play_page(blueClickBlock = blueLightScaled, yellowClickBlock = yellowLightScaled, greenClickBlock = greenLightScaled, redClickBlock = redLightScaled)
    pygame.time.delay(500)
    render_game_simon_play_page(yellowClickBlock = yellowScaled, blueClickBlock = blueScaled, greenClickBlock = greenScaled, redClickBlock = redScaled)
    pygame.time.delay(250)
    render_game_simon_play_page(blueClickBlock = blueLightScaled, yellowClickBlock = yellowLightScaled, greenClickBlock = greenLightScaled, redClickBlock = redLightScaled)
    pygame.time.delay(500)
    render_game_simon_play_page(yellowClickBlock = yellowScaled, blueClickBlock = blueScaled, greenClickBlock = greenScaled, redClickBlock = redScaled)
    pygame.time.delay(250)
    render_game_simon_play_page(blueClickBlock = blueLightScaled, yellowClickBlock = yellowLightScaled, greenClickBlock = greenLightScaled, redClickBlock = redLightScaled)
    pygame.time.delay(500)
    pygame.mixer.Channel(2).stop()
    render_game_simon_play_page(yellowClickBlock = yellowScaled, blueClickBlock = blueScaled, greenClickBlock = greenScaled, redClickBlock = redScaled)


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
        
        if life >= 3 and gameMode == "Penguin":
            pygame.time.set_timer(RETURN_NORMAL_EVENT, 3000, 1)
            peng_life_loss()
        if life == 2:
            pygame.time.set_timer(RETURN_NORMAL_EVENT, 3000, 1)
            heart1 = heartImageEmptyScaled
            if gameMode == "Easy" or gameMode == "Normal" or gameMode == "Hard":
                window.blit(heart1, (int((window_width-36-36-36-5-5-50) * resizeScale), int(50 * resizeScale)))
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
                window.blit(heart1, (int((window_width-36-36-36-5-5-50) * resizeScale), int(50 * resizeScale)))
                window.blit(heart2, (int((window_width-36-36-5-50) * resizeScale), int(50 * resizeScale)))
                pygame.display.update()
                life_loss()
            if gameMode == "Penguin":
                peng_life_loss()
        if life == 0:
            heart1 = heartImageEmptyScaled
            heart2 = heartImageEmptyScaled
            heart3 = heartImageEmptyScaled
            if gameMode == "Easy" or gameMode == "Normal" or gameMode == "Hard":
                window.blit(heart1, (int((window_width-36-36-36-5-5-50) * resizeScale), int(50 * resizeScale)))
                window.blit(heart2, (int((window_width-36-36-5-50) * resizeScale), int(50 * resizeScale)))
                window.blit(heart3, (int((window_width-36-50) * resizeScale), int(50 * resizeScale)))
                pygame.display.update()
                print('goin')
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
    pygame.time.delay(timeDelay + 150)
    
    beepBeepBeepSound = pygame.mixer.Sound('./Assets/sounds/beep_beep_beep.wav')
    pygame.mixer.Channel(2).play(beepBeepBeepSound)
    print('player got it wrong so sound played and life lost')
    redColour, redLightColour = ('#FF0000'), ('#800000')
    blueColour, blueLightColour = ('#003DFF'), ('#001E80')
    yellowColour, yellowLightColour = ('#F0FF00'), ('#778000')
    greenColour, greenLightColour = ('#25FF00'), ('#008000')
    pygame.time.set_timer(LIFE_LOSS_LIGHT_EVENT, 500, 1)
    pygame.time.set_timer(LIFE_LOSS_CONTINUE_EVENT, 750, 2)


def render_settings_screen():
    waiting = True
    credBoxColour = WHITE
    infoBoxColour = WHITE
    selectResBoxColour = WHITE
    credBox = pygame.Rect(int(295 * resizeScale), int(330 * resizeScale), int(210 * resizeScale), int(60 * resizeScale))
    infoBox = pygame.Rect(int(362.5 * resizeScale), int(260 * resizeScale), int(75 * resizeScale), int(60 * resizeScale))
    selectResBox = pygame.Rect(int(265 * resizeScale), int(400 * resizeScale), int(270 * resizeScale), int(60 * resizeScale))
    okText = gameFontEnd.render("OK", True, WHITE)
    infoText = gameFontSubtitle.render("i", True, WHITE)
    credText = gameFontSubtitle.render("Credits", True, WHITE)
    selectResText = gameFontSubtitle.render("Resolution", True, WHITE)
    global volume
    global sliderX
    global soundImage
    global soundLocation
    switching = 1
    invisVolumeBox = pygame.Rect(int(resizeScale * 180), int(resizeScale * 215), int(resizeScale * 525), int(resizeScale * 26))
    changingVolume = False
    settingsPage = 1
    global settingsDict
    upInputBox = pygame.Rect(int(resizeScale * 425), int(resizeScale * 200), int(resizeScale * 250), int(resizeScale * 40))
    downInputBox = pygame.Rect(int(resizeScale * 425), int(resizeScale * 250), int(resizeScale * 250), int(resizeScale * 40))
    leftInputBox = pygame.Rect(int(resizeScale * 425), int(resizeScale * 300), int(resizeScale * 250), int(resizeScale * 40))
    rightInputBox = pygame.Rect(int(resizeScale * 425), int(resizeScale * 350), int(resizeScale * 250), int(resizeScale * 40))
    boostInputBox = pygame.Rect(int(resizeScale * 425), int(resizeScale * 400), int(resizeScale * 250), int(resizeScale * 40))
    upInputBoxActive = False
    downInputBoxActive = False
    leftInputBoxActive = False
    rightInputBoxActive = False
    boostInputBoxActive = False
    
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if settingsPage == 1 and event.type == pygame.MOUSEMOTION and event.buttons == (1, 0, 0): # slider
                # print(int(resizeScale * event.pos[0]))
                if changingVolume:
                    if event.rel[0] != 0:
                        sliderX = event.pos[0] - soundSliderScaled.get_width()/2
                        if sliderX > int(resizeScale * 700): # constrict the location of the slider to the most right of the slider line
                            sliderX = int(resizeScale * 700)
                        if sliderX < int(resizeScale * 178): # constrict the location of the slider to the most left of the slider line
                            sliderX = int(resizeScale * 178)
                            soundImage = soundOffScaled
                            soundLocation = (int(resizeScale * 85), int(resizeScale * 185))
                            pygame.mixer.Channel(1).set_volume(0)
                            pygame.mixer.Channel(2).set_volume(0)
                            pygame.mixer.Channel(3).set_volume(0)
                            switching = 1
                        else:
                            soundImage = soundOnScaled
                            soundLocation = (int(resizeScale * 100), int(resizeScale * 200))
                            pygame.mixer.Channel(1).set_volume(volume)
                            pygame.mixer.Channel(2).set_volume(volume)
                            pygame.mixer.Channel(3).set_volume(volume)
                            sliderXOrigPos = sliderX
                            switching = 2
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if okText.get_rect(topleft=(((int(resizeScale * window_width)-okText.get_width())/2), int(475 * resizeScale))).collidepoint(pygame.mouse.get_pos()):
                    waiting = False
                if settingsPage == 1:
                    if invisVolumeBox.collidepoint(pygame.mouse.get_pos()):
                        sliderX = event.pos[0] - soundSliderScaled.get_width()/2
                        changingVolume = True
                        if sliderX > int(resizeScale * 700): # constrict the location of the slider to the most right of the slider line
                            sliderX = int(resizeScale * 700)
                        if sliderX < int(resizeScale * 178): # constrict the location of the slider to the most left of the slider line
                            sliderX = int(resizeScale * 178)
                            soundImage = soundOffScaled
                            switching = 1
                            soundLocation = (int(resizeScale * 85), int(resizeScale * 185))
                            pygame.mixer.Channel(1).set_volume(0)
                            pygame.mixer.Channel(2).set_volume(0)
                            pygame.mixer.Channel(3).set_volume(0)
                        else:
                            soundImage = soundOnScaled
                            soundLocation = (int(resizeScale * 100), int(resizeScale * 200))
                            sliderXOrigPos = sliderX
                            switching = 2
                    else:
                        changingVolume = False
                    if remove_transparent_pixels(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale))):
                        settingsPage = 2
                    elif credBox.collidepoint(pygame.mouse.get_pos()):
                        render_credits_screen()
                    elif infoBox.collidepoint(pygame.mouse.get_pos()):
                        render_game_rules_screen()
                    elif selectResBox.collidepoint(pygame.mouse.get_pos()):
                        render_choose_res_screen()
                    if soundImage.get_rect(topleft=(soundLocation)).collidepoint(pygame.mouse.get_pos()):
                        if switching == 1:
                            sliderXOrigPos = sliderX
                            soundImage = soundOffScaled
                            soundLocation = (int(resizeScale * 85), int(resizeScale * 185))
                            pygame.mixer.Channel(1).set_volume(0)
                            pygame.mixer.Channel(2).set_volume(0)
                            pygame.mixer.Channel(3).set_volume(0)
                            sliderX = int(resizeScale * 178)
                            switching = 2
                            break
                        if switching == 2:
                            sliderX = sliderXOrigPos
                            soundImage = soundOnScaled
                            soundLocation = (int(resizeScale * 100), int(resizeScale * 200))
                            pygame.mixer.Channel(1).set_volume(volume)
                            pygame.mixer.Channel(2).set_volume(volume)
                            pygame.mixer.Channel(3).set_volume(volume)
                            switching = 1
                            break
                if settingsPage == 2:
                    if upInputBox.collidepoint(pygame.mouse.get_pos()):
                        upTextAllowed = False
                        downTextAllowed = True
                        leftTextAllowed = True
                        rightTextAllowed = True
                        boostTextAllowed = True
                        # settingsDict["up"] = ''
                        upInputBoxActive = True
                        downInputBoxActive = False
                        leftInputBoxActive = False
                        rightInputBoxActive = False
                        boostInputBoxActive = False
                    elif downInputBox.collidepoint(pygame.mouse.get_pos()):
                        upTextAllowed = True
                        downTextAllowed = False
                        leftTextAllowed = True
                        rightTextAllowed = True
                        boostTextAllowed = True
                        # settingsDict["down"] = ''
                        upInputBoxActive = False
                        downInputBoxActive = True
                        leftInputBoxActive = False
                        rightInputBoxActive = False
                        boostInputBoxActive = False
                    elif leftInputBox.collidepoint(pygame.mouse.get_pos()):
                        upTextAllowed = True
                        downTextAllowed = True
                        leftTextAllowed = False
                        rightTextAllowed = True
                        boostTextAllowed = True
                        # settingsDict["left"] = ''
                        upInputBoxActive = False
                        downInputBoxActive = False
                        leftInputBoxActive = True
                        rightInputBoxActive = False
                        boostInputBoxActive = False
                    elif rightInputBox.collidepoint(pygame.mouse.get_pos()):
                        upTextAllowed = True
                        downTextAllowed = True
                        leftTextAllowed = True
                        rightTextAllowed = False
                        boostTextAllowed = True
                        # settingsDict["right"] = ''
                        upInputBoxActive = False
                        downInputBoxActive = False
                        leftInputBoxActive = False
                        rightInputBoxActive = True
                        boostInputBoxActive = False
                    elif boostInputBox.collidepoint(pygame.mouse.get_pos()):
                        upTextAllowed = True
                        downTextAllowed = True
                        leftTextAllowed = True
                        rightTextAllowed = True
                        boostTextAllowed = False
                        # settingsDict["boost"] = ''
                        upInputBoxActive = False
                        downInputBoxActive = False
                        leftInputBoxActive = False
                        rightInputBoxActive = False
                        boostInputBoxActive = True
                    else:
                        upTextAllowed = True
                        downTextAllowed = True
                        leftTextAllowed = True
                        rightTextAllowed = True
                        boostTextAllowed = True
                        upInputBoxActive = False
                        downInputBoxActive = False
                        leftInputBoxActive = False
                        rightInputBoxActive = False
                        boostInputBoxActive = False
                    
                    if remove_transparent_pixels(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale))):
                        settingsPage = 1
            if event.type == pygame.KEYDOWN:
                if type(event.unicode) == str:
                    upTextAllowed = True
                    downTextAllowed = True
                    leftTextAllowed = True
                    rightTextAllowed = True
                    boostTextAllowed = True
                    if upInputBoxActive == True:
                        upInputBoxActive = False
                        settingsDict["up"] = event.key
                        with open("settings.json", "w") as file:
                            json.dump(settingsDict, file)
                    if downInputBoxActive == True:
                        downInputBoxActive = False
                        settingsDict["down"] = event.key
                        with open("settings.json", "w") as file:
                            json.dump(settingsDict, file)
                    if leftInputBoxActive == True:
                        leftInputBoxActive = False
                        settingsDict["left"] = event.key
                        with open("settings.json", "w") as file:
                            json.dump(settingsDict, file)
                    if rightInputBoxActive == True:
                        rightInputBoxActive = False
                        settingsDict["right"] = event.key
                        with open("settings.json", "w") as file:
                            json.dump(settingsDict, file)
                    if boostInputBoxActive == True:
                        boostInputBoxActive = False
                        settingsDict["boost"] = event.key
                        with open("settings.json", "w") as file:
                            json.dump(settingsDict, file)

        if resizeScale < 0.5:
            lineThickness = 1
        else:
            lineThickness = int(resizeScale * 2)
        window.fill(GREY)
        window.blit(blackGradientScreenScaled, (0, 0))
        pygame.draw.rect(window, BLACK, bg)
        pygame.draw.rect(window, WHITE, bg, lineThickness)
        if settingsPage == 1:
            if credBox.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                credBoxColour = RED
                if not soundPlayed:
                    pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                    soundPlayed = True
            else:
                credBoxColour = WHITE
                soundPlayed = False
            if infoBox.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                infoBoxColour = RED
                if not soundPlayed:
                    pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                    soundPlayed = True
            else:
                infoBoxColour = WHITE
                soundPlayed = False
            if selectResBox.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                selectResBoxColour = RED
                if not soundPlayed:
                    pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                    soundPlayed = True
            else:
                selectResBoxColour = WHITE
                soundPlayed = False
            if okText.get_rect(topleft=(((int(resizeScale * window_width)-okText.get_width())/2), int(475 * resizeScale))).collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            pygame.draw.rect(window, BLACK, credBox)
            pygame.draw.rect(window, credBoxColour, credBox, lineThickness)
            pygame.draw.rect(window, BLACK, infoBox)
            pygame.draw.rect(window, infoBoxColour, infoBox, lineThickness)
            pygame.draw.rect(window, BLACK, selectResBox)
            pygame.draw.rect(window, selectResBoxColour, selectResBox, lineThickness)
            remove_transparent_pixels(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale)))
            if not remove_transparent_pixels(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale))) and not credBox.collidepoint(pygame.mouse.get_pos()) and not infoBox.collidepoint(pygame.mouse.get_pos()) and not selectResBox.collidepoint(pygame.mouse.get_pos()) and not okText.get_rect(topleft=(((int(resizeScale * window_width)-okText.get_width())/2), int(475 * resizeScale))).collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor()
            window.blit(infoText, ((int(resizeScale * window_width)-infoText.get_width())/2, int(285 * resizeScale)))
            window.blit(credText, ((int(resizeScale * window_width)-credText.get_width())/2, int(350 * resizeScale)))
            window.blit(selectResText, ((int(resizeScale * window_width)-selectResText.get_width())/2, int(420 * resizeScale)))
            window.blit(soundImage, soundLocation)
            window.blit(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale)))
            pygame.draw.line(window, WHITE, (int(180 * resizeScale), int(227 * resizeScale)), (int(705 * resizeScale), int(227 * resizeScale)), lineThickness) # volume goes up to 525
            window.blit(soundSliderScaled, (sliderX, int(215 * resizeScale))) # make it so that the x location is proportional to the volume
            volume = (sliderX - int(resizeScale * 180)) / int(resizeScale * 525)
            sliderX = (volume * int(resizeScale * 525)) + int(resizeScale * 180)
            pygame.mixer.Channel(1).set_volume(volume)
            pygame.mixer.Channel(2).set_volume(volume) # sliderScaled = (26, 26)
            pygame.mixer.Channel(3).set_volume(volume)
        if settingsPage == 2:
            remove_transparent_pixels(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale)))
            window.blit(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale)))
            
            upInputBox = pygame.Rect(int(resizeScale * 425), int(resizeScale * 200), int(resizeScale * 250), int(resizeScale * 40))
            if upInputBox.collidepoint(pygame.mouse.get_pos()):
                upInputBoxColour = RED
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                upInputBoxColour = WHITE
            upInputText = gameFont.render("UP", True, WHITE)
            try:
                upText = chr(int(settingsDict["up"]))
                if settingsDict["up"] == 32:
                    upText = "SPACEBAR"
            except ValueError:
                if settingsDict["up"] == 1073741906:
                    upText = "UP Arrow"
                elif settingsDict["up"] == 1073741905:
                    upText = "DOWN Arrow"
                elif settingsDict["up"] == 1073741904:
                    upText = "LEFT Arrow"
                elif settingsDict["up"] == 1073741903:
                    upText = "RIGHT Arrow"
                elif settingsDict["up"] == 32:
                    upText = "SPACEBAR"
                pass
            upPlayerInputText = gameFont.render(upText, True, WHITE)
            downInputBox = pygame.Rect(int(resizeScale * 425), int(resizeScale * 250), int(resizeScale * 250), int(resizeScale * 40))
            if downInputBox.collidepoint(pygame.mouse.get_pos()):
                downInputBoxColour = RED
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                downInputBoxColour = WHITE
            downInputText = gameFont.render("DOWN", True, WHITE)
            try:
                downText = chr(int(settingsDict["down"]))
                if settingsDict["down"] == 32:
                    upText = "SPACEBAR"
            except ValueError:
                if settingsDict["down"] == 1073741906:
                    downText = "UP Arrow"
                elif settingsDict["down"] == 1073741905:
                    downText = "DOWN Arrow"
                elif settingsDict["down"] == 1073741904:
                    downText = "LEFT Arrow"
                elif settingsDict["down"] == 1073741903:
                    downText = "RIGHT Arrow"
                elif settingsDict["down"] == 32:
                    downText = "SPACEBAR"
                pass
            downPlayerInputText = gameFont.render(downText, True, WHITE)
            leftInputBox = pygame.Rect(int(resizeScale * 425), int(resizeScale * 300), int(resizeScale * 250), int(resizeScale * 40))
            if leftInputBox.collidepoint(pygame.mouse.get_pos()):
                leftInputBoxColour = RED
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                leftInputBoxColour = WHITE
            leftInputText = gameFont.render("LEFT", True, WHITE)
            try:
                leftText = chr(int(settingsDict["left"]))
                if settingsDict["left"] == 32:
                    upText = "SPACEBAR"
            except ValueError:
                if settingsDict["left"] == 1073741906:
                    leftText = "UP Arrow"
                elif settingsDict["left"] == 1073741905:
                    leftText = "DOWN Arrow"
                elif settingsDict["left"] == 1073741904:
                    leftText = "LEFT Arrow"
                elif settingsDict["left"] == 1073741903:
                    leftText = "RIGHT Arrow"
                elif settingsDict["left"] == 32:
                    leftText = "SPACEBAR"
                pass
            leftPlayerInputText = gameFont.render(leftText, True, WHITE)
            rightInputBox = pygame.Rect(int(resizeScale * 425), int(resizeScale * 350), int(resizeScale * 250), int(resizeScale * 40))
            if rightInputBox.collidepoint(pygame.mouse.get_pos()):
                rightInputBoxColour = RED
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                rightInputBoxColour = WHITE
            rightInputText = gameFont.render("RIGHT", True, WHITE)
            try:
                rightText = chr(int(settingsDict["right"]))
                if settingsDict["right"] == 32:
                    upText = "SPACEBAR"
            except ValueError:
                if settingsDict["right"] == 1073741906:
                    rightText = "UP Arrow"
                elif settingsDict["right"] == 1073741905:
                    rightText = "DOWN Arrow"
                elif settingsDict["right"] == 1073741904:
                    rightText = "LEFT Arrow"
                elif settingsDict["right"] == 1073741903:
                    rightText = "RIGHT Arrow"
                elif settingsDict["right"] == 32:
                    rightText = "SPACEBAR"
                pass
            rightPlayerInputText = gameFont.render(rightText, True, WHITE)
            boostInputBox = pygame.Rect(int(resizeScale * 425), int(resizeScale * 400), int(resizeScale * 250), int(resizeScale * 40))
            if boostInputBox.collidepoint(pygame.mouse.get_pos()):
                boostInputBoxColour = RED
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                boostInputBoxColour = WHITE
            boostInputText = gameFont.render("BOOST/JUMP", True, WHITE)
            try:
                boostText = chr(int(settingsDict["boost"]))
                if settingsDict["boost"] == 32:
                    boostText = "SPACEBAR"
            except ValueError:
                if settingsDict["boost"] == 1073741906:
                    boostText = "UP Arrow"
                elif settingsDict["boost"] == 1073741905:
                    boostText = "DOWN Arrow"
                elif settingsDict["boost"] == 1073741904:
                    boostText = "LEFT Arrow"
                elif settingsDict["boost"] == 1073741903:
                    boostText = "RIGHT Arrow"
                pass
            boostPlayerInputText = gameFont.render(boostText, True, WHITE)
            
            pygame.draw.rect(window, BLACK, upInputBox)
            pygame.draw.rect(window, upInputBoxColour, upInputBox, lineThickness)
            window.blit(upInputText, (upInputBox.x + upInputBox.w/2 - upInputText.get_width()/2 - int(resizeScale * 300), upInputBox.y + upInputBox.h/2 - upInputText.get_height()/2))
            if upTextAllowed == True:
                window.blit(upPlayerInputText, (upInputBox.x + upInputBox.w/2 - upPlayerInputText.get_width()/2, upInputBox.y + upInputBox.h/2 - upPlayerInputText.get_height()/2))
            pygame.draw.rect(window, BLACK, downInputBox)
            pygame.draw.rect(window, downInputBoxColour, downInputBox, lineThickness)
            window.blit(downInputText, (downInputBox.x + downInputBox.w/2 - downInputText.get_width()/2 - int(resizeScale * 300), downInputBox.y + downInputBox.h/2 - downInputText.get_height()/2))
            if downTextAllowed == True:
                window.blit(downPlayerInputText, (downInputBox.x + downInputBox.w/2 - downPlayerInputText.get_width()/2, downInputBox.y + downInputBox.h/2 - downPlayerInputText.get_height()/2))
            pygame.draw.rect(window, BLACK, leftInputBox)
            pygame.draw.rect(window, leftInputBoxColour, leftInputBox, lineThickness)
            window.blit(leftInputText, (leftInputBox.x + leftInputBox.w/2 - leftInputText.get_width()/2 - int(resizeScale * 300), leftInputBox.y + leftInputBox.h/2 - leftInputText.get_height()/2))
            if leftTextAllowed == True:
                window.blit(leftPlayerInputText, (leftInputBox.x + leftInputBox.w/2 - leftPlayerInputText.get_width()/2, leftInputBox.y + leftInputBox.h/2 - leftPlayerInputText.get_height()/2))
            pygame.draw.rect(window, BLACK, rightInputBox)
            pygame.draw.rect(window, rightInputBoxColour, rightInputBox, lineThickness)
            window.blit(rightInputText, (rightInputBox.x + rightInputBox.w/2 - rightInputText.get_width()/2 - int(resizeScale * 300), rightInputBox.y + rightInputBox.h/2 - rightInputText.get_height()/2))
            if rightTextAllowed == True:
                window.blit(rightPlayerInputText, (rightInputBox.x + rightInputBox.w/2 - rightPlayerInputText.get_width()/2, rightInputBox.y + rightInputBox.h/2 - rightPlayerInputText.get_height()/2))
            pygame.draw.rect(window, BLACK, boostInputBox)
            pygame.draw.rect(window, boostInputBoxColour, boostInputBox, lineThickness)
            window.blit(boostInputText, (boostInputBox.x + boostInputBox.w/2 - boostInputText.get_width()/2 - int(resizeScale * 300), boostInputBox.y + boostInputBox.h/2 - boostInputText.get_height()/2))
            if boostTextAllowed == True:
                window.blit(boostPlayerInputText, (boostInputBox.x + boostInputBox.w/2 - boostPlayerInputText.get_width()/2, boostInputBox.y + boostInputBox.h/2 - boostPlayerInputText.get_height()/2))
            
            
            if okText.get_rect(topleft=(((int(resizeScale * window_width)-okText.get_width())/2), int(475 * resizeScale))).collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if not upInputBox.collidepoint(pygame.mouse.get_pos()) and not downInputBox.collidepoint(pygame.mouse.get_pos()) and not leftInputBox.collidepoint(pygame.mouse.get_pos()) and not rightInputBox.collidepoint(pygame.mouse.get_pos()) and not boostInputBox.collidepoint(pygame.mouse.get_pos()) and not remove_transparent_pixels(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale))) and not okText.get_rect(topleft=(((int(resizeScale * window_width)-okText.get_width())/2), int(475 * resizeScale))).collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor()
            ###### allow for player to change their keybinds
        
        window.blit(okText, (((int(resizeScale * window_width)-okText.get_width())/2), int(475 * resizeScale)))
        window.blit(settingsScaled2, (int(345.3 * resizeScale), int(50 * resizeScale)))
        pygame.display.update() #^^^ 177 cause 1 empty *2 + 1


def render_choose_res_screen():
    screenWidthInputValue, screenHeightInputValue = "", ""
    inputBoxScreenWidthActive, inputBoxScreenHeightActive = False, False
    errorMessage = ""
    newlineMessage = ""
    fullScreenAllow = "Not Decided"
    tooLarge, tooSimilar = False, False
    
    cursor_timer = 0
    cursor_active = True
    CURSOR_BLINK_INTERVAL = 500
    
    submitInputButtonColour = (200, 200, 200)
    submitInputButtonActiveColour = (100, 100, 100)

    waiting = True
    clock = pygame.time.Clock()
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN: # has parts for enter button click
                if remove_transparent_pixels(homeButtonScaled, (int(600 * resizeScale), int(400 * resizeScale))):
                    render_game_start_page()
                elif inputBoxScreenWidth.collidepoint(pygame.mouse.get_pos()):
                    inputBoxScreenWidthActive = True
                    inputBoxScreenHeightActive = False
                elif inputBoxScreenHeight.collidepoint(pygame.mouse.get_pos()):
                    inputBoxScreenHeightActive = True
                    inputBoxScreenWidthActive = False
                elif newlineMessage == "Would you like to go fullscreen instead?":
                    if newlineMessageClickNo.collidepoint(pygame.mouse.get_pos()):
                        fullScreenAllow = "No"
                    if newlineMessageClickYes.collidepoint(pygame.mouse.get_pos()):
                        fullScreenAllow = "Yes"
                else:
                    inputBoxScreenWidthActive = False
                    inputBoxScreenHeightActive = False
                    fullScreenAllow = "Not Decided"

                if submitInputButton.collidepoint(pygame.mouse.get_pos()):
                    if len(screenHeightInputValue) > 2 or len(screenWidthInputValue) > 2:
                        if screen_width > float(screenWidthInputValue) > screen_width - 75 or screen_height > float(screenHeightInputValue) > screen_height - 75: # if input is similar
                            errorMessage = "That resolution seems quite close to fullscreen."
                            newlineMessage = "Would you like to go fullscreen instead?"
                            tooSimilar = True
                        elif float(screenWidthInputValue) > screen_width or float(screenHeightInputValue) > screen_height: # if its too large
                            errorMessage = "Invalid input! Integer exceeds screen resolution."
                            newlineMessage = "Would you like to go fullscreen instead?"
                            tooLarge = True
                        elif int(float(screenHeightInputValue)) < 100: # if too small
                            errorMessage = "Resolution too small, please increase desired resolution."
                        else: # if its a good value
                            print("New Resolution: " + screenWidthInputValue + " × " + screenHeightInputValue)
                            errorMessage = "Resolution Changed Successfully."
                            newlineMessage = f"New resolution is: {int(screenWidthInputValue.split('.')[0])} × {int(screenHeightInputValue.split('.')[0])}"
                            resize_assets(int(screenWidthInputValue.split('.')[0]), int(screenHeightInputValue.split('.')[0]))
                            screenWidthInputValue, screenHeightInputValue = "", ""
                    else:
                        try:
                            if int(screenHeightInputValue) < 100: # if they type 23 or 99 etc
                                errorMessage = "Resolution too small, please increase desired resolution."
                        except ValueError:
                            pass
            elif event.type == pygame.KEYDOWN:
                if inputBoxScreenWidthActive: # for the left box
                    if event.key == pygame.K_RETURN:
                        if len(screenWidthInputValue) > 2:
                            if screen_width > float(screenWidthInputValue) > screen_width - 75 or screen_height > float(screenHeightInputValue) > screen_height - 75: # input too similar?
                                errorMessage = "That resolution seems quite close to fullscreen."
                                newlineMessage = "Would you like to go fullscreen instead?"
                                tooSimilar = True
                            elif float(screenWidthInputValue) > screen_width or float(screenHeightInputValue) > screen_height: # too large?
                                errorMessage = "Invalid input! Integer exceeds screen resolution."
                                newlineMessage = "Would you like to go fullscreen instead?"
                                tooLarge = True
                            elif int(screenWidthInputValue) < 100: # too small?
                                errorMessage = "Resolution too small, please increase desired resolution."
                            else: # is passed
                                print("New Resolution: " + screenWidthInputValue + " × " + screenHeightInputValue)
                                errorMessage = "Resolution Changed Successfully."
                                newlineMessage = f"New resolution is: {int(screenWidthInputValue.split('.')[0])} × {int(screenHeightInputValue.split('.')[0])}"
                                resize_assets(int(screenWidthInputValue.split('.')[0]), int(screenHeightInputValue.split('.')[0]))
                                screenWidthInputValue, screenHeightInputValue = "", ""
                        else:
                            try:
                                if int(screenWidthInputValue) < 100: # for inputs like 23 or 99 etc...
                                    errorMessage = "Resolution too small, please increase desired resolution."
                            except ValueError:
                                pass
                    elif event.key == pygame.K_BACKSPACE:
                        screenWidthInputValue = screenWidthInputValue[:-1]
                        if screenWidthInputValue != '':
                            screenHeightInputValue = str(float(screenWidthInputValue) * (3/4))
                        else:
                            screenHeightInputValue = ''
                    elif event.unicode.isdigit() and len(screenWidthInputValue) < 4:  # Limit to 4 digits
                        screenWidthInputValue += event.unicode
                        errorMessage = ""
                        newlineMessage = ""
                        if screenWidthInputValue == '':
                            screenHeightInputValue = ''
                        screenHeightInputValue = str(float(screenWidthInputValue) * (3/4))
                        print(screenWidthInputValue + " × " + screenHeightInputValue)
                    elif len(screenWidthInputValue) < 4:
                        errorMessage = "Invalid input! Enter an integer."
                if inputBoxScreenHeightActive: # for the right box
                    if event.key == pygame.K_RETURN:
                        if len(screenHeightInputValue) > 2:
                            if screen_width > float(screenWidthInputValue) > screen_width - 75 or screen_height > float(screenHeightInputValue) > screen_height - 75: # if input similar
                                errorMessage = "That resolution seems quite close to fullscreen."
                                newlineMessage =  "Would you like to go fullscreen instead?"
                                tooSimilar = True
                            elif float(screenWidthInputValue) > screen_width or float(screenHeightInputValue) > screen_height: # if too large
                                errorMessage = "Invalid input! Integer exceeds screen resolution."
                                newlineMessage = "Would you like to go fullscreen instead?"
                                tooLarge = True
                            elif int(screenHeightInputValue) < 100: # too small
                                errorMessage = "Resolution too small, please increase desired resolution."
                            else:
                                print("New Resolution: " + screenWidthInputValue + " × " + screenHeightInputValue)
                                errorMessage = "Resolution Changed Successfully."
                                newlineMessage = f"New resolution is: {int(screenWidthInputValue.split('.')[0])} × {int(screenHeightInputValue.split('.')[0])}"
                                resize_assets(int(screenWidthInputValue.split('.')[0]), int(screenHeightInputValue.split('.')[0]))
                                screenWidthInputValue, screenHeightInputValue = "", ""
                        else:
                            try:
                                if int(screenHeightInputValue) < 100: # for 23 or 99 etc
                                    errorMessage = "Resolution too small, please increase desired resolution."
                            except ValueError:
                                pass
                    elif event.key == pygame.K_BACKSPACE:
                        screenHeightInputValue = screenHeightInputValue[:-1]
                        if screenHeightInputValue != '':
                            screenWidthInputValue = str(float(screenHeightInputValue) * (4/3))
                        else:
                            screenWidthInputValue = ''
                    elif event.unicode.isdigit() and len(screenHeightInputValue) < 4:  # Limit to 4 digits
                        screenHeightInputValue += event.unicode
                        errorMessage = ""
                        newlineMessage = ""
                        if screenHeightInputValue == '':
                            screenWidthInputValue = ''
                        screenWidthInputValue = str(float(screenHeightInputValue) * (4/3))
                        print(screenWidthInputValue + " × " + screenHeightInputValue)
                    elif len(screenHeightInputValue) < 4:
                        errorMessage = "Invalid input! Enter an integer."

        
        screen_width, screen_height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1) # Get the user's screen resolution
        inputBoxScreenWidth = pygame.Rect(int(150 * resizeScale), int(250 * resizeScale), int(175 * resizeScale), int(32 * resizeScale))
        inputBoxScreenHeight = pygame.Rect(int(400 * resizeScale), int(250 * resizeScale), int(175 * resizeScale), int(32 * resizeScale))
        font = pygame.font.Font(None, int(32 * resizeScale))
        errorMessageFont = pygame.font.Font(None, int(24 * resizeScale))
        submitInputButton = pygame.Rect(int(585 * resizeScale), int(250 * resizeScale), int(80 * resizeScale), int(32 * resizeScale))
        resBg = pygame.Rect(int(100 * resizeScale), int(50 * resizeScale), int(600 * resizeScale), int(100 * resizeScale))
        px = font.render('px', True, WHITE)
        resText = gameFontStart.render('Choose Res', True, WHITE)
        xText = font.render('×', True, WHITE)
        
        # Clear the screen
        window.fill(GREY)
        window.blit(blackGradientScreenScaled, (0, 0))
        pygame.draw.rect(window, BLACK, bg)
        if resizeScale < 0.5:
            lineThickness = 1
        else:
            lineThickness = int(resizeScale * 2)
        pygame.draw.rect(window, WHITE, bg, lineThickness)
        pygame.draw.rect(window, BLACK, resBg)
        pygame.draw.rect(window, WHITE, resBg, lineThickness)
        window.blit(homeButtonScaled, (int(600 * resizeScale), int(400 * resizeScale)))
        window.blit(resText, (((int(resizeScale * window_width) - resText.get_width())/2), int(75 * resizeScale)))
        pygame.draw.rect(window, WHITE, inputBoxScreenWidth, lineThickness)
        screenInputTextWidth = font.render(screenWidthInputValue.split('.')[0], True, WHITE)
        window.blit(screenInputTextWidth, (int(155 * resizeScale), int(255 * resizeScale)))
        pygame.draw.rect(window, WHITE, inputBoxScreenHeight, lineThickness)
        screenInputTextHeight = font.render(screenHeightInputValue.split('.')[0], True, WHITE)
        window.blit(screenInputTextHeight, (int(405 * resizeScale), int(255 * resizeScale)))
        window.blit(px, (int(295 * resizeScale), int(255 * resizeScale)))
        window.blit(px, (int(545 * resizeScale), int(255 * resizeScale)))
        window.blit(xText, (int(356 * resizeScale), int(255 * resizeScale)))
### ^^^ the above xText, px, etc... shouldnt have  * resizeScale)

        # blinking text cursor
        if resizeScale < 0.5:
            lineThickness = 1
        else:
            lineThickness = int(resizeScale * 2)
        if inputBoxScreenWidthActive:
            cursor_timer = cursor_timer + clock.get_time()
            if cursor_timer >= CURSOR_BLINK_INTERVAL:
                cursor_active = not cursor_active
                cursor_timer = 0
            if cursor_active:
                cursor_pos_x = inputBoxScreenWidth.x + 5 + screenInputTextWidth.get_width()
                pygame.draw.line(window, WHITE, (cursor_pos_x, inputBoxScreenWidth.y + 5), (cursor_pos_x, inputBoxScreenWidth.y + inputBoxScreenWidth.height - 5), lineThickness)
        if inputBoxScreenHeightActive:
            cursor_timer = cursor_timer + clock.get_time()
            if cursor_timer >= CURSOR_BLINK_INTERVAL:
                cursor_active = not cursor_active
                cursor_timer = 0
            if cursor_active:
                cursor_pos_x = inputBoxScreenHeight.x + 5 + screenInputTextHeight.get_width()
                pygame.draw.line(window, WHITE, (cursor_pos_x, inputBoxScreenHeight.y + 5), (cursor_pos_x, inputBoxScreenHeight.y + inputBoxScreenHeight.height - 5), lineThickness)

        if errorMessage:
            errorText = errorMessageFont.render(errorMessage, True, RED)
            window.blit(errorText, ((int(resizeScale * window_width) - errorText.get_width())/2, inputBoxScreenWidth.y + inputBoxScreenWidth.height + int(resizeScale * 20)))
        if newlineMessage:
            newlineMessageText = errorMessageFont.render(newlineMessage, True, RED)
            window.blit(newlineMessageText, ((int(resizeScale * window_width) - newlineMessageText.get_width())/2, inputBoxScreenWidth.y + inputBoxScreenWidth.height + int(resizeScale * 50)))
        
        if newlineMessage == "Would you like to go fullscreen instead?":
            if newlineMessageClickNo.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                newlineMessageClickNoColour = RED
                if not soundPlayed:
                    pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                    soundPlayed = True
            else:
                newlineMessageClickNoColour = WHITE
                soundPlayed = False
            if newlineMessageClickYes.collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                newlineMessageClickYesColour = RED
                if not soundPlayed:
                    pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                    soundPlayed = True
            else:
                newlineMessageClickYesColour = WHITE
                soundPlayed = False
            pygame.draw.rect(window, BLACK, newlineMessageClickNo)
            pygame.draw.rect(window, newlineMessageClickNoColour, newlineMessageClickNo, lineThickness)
            window.blit(newlineMessageClickNoText, (newlineMessageClickNo.x + newlineMessageClickNo.w/2 - newlineMessageClickNoText.get_width()/2, newlineMessageClickNo.y + newlineMessageClickNo.h/2 - newlineMessageClickNoText.get_height()/2))
            
            pygame.draw.rect(window, BLACK, newlineMessageClickYes)
            pygame.draw.rect(window, newlineMessageClickYesColour, newlineMessageClickYes, lineThickness)
            window.blit(newlineMessageClickYesText, (newlineMessageClickYes.x + newlineMessageClickYes.w/2 - newlineMessageClickYesText.get_width()/2, newlineMessageClickYes.y + newlineMessageClickYes.h/2 - newlineMessageClickYesText.get_height()/2))
            
            if tooLarge == True:
                if fullScreenAllow == "Yes":
                    screenWidthInputValue = str(float(screen_height) * (4/3))
                    resize_assets(int(screenWidthInputValue.split('.')[0]), screen_height, True)
                    fullScreenAllow = "Not Decided"
                    errorMessage = "Resolution Changed Successfully."
                    newlineMessage = f"New resolution is: {int(screenWidthInputValue.split('.')[0])} × {screen_height}"
                    screenWidthInputValue, screenHeightInputValue = "", ""
                elif fullScreenAllow == "No":
                    screenWidthInputValue = str(float(screen_height) * (4/3))
                    newlineMessage = f"Then please choose a resolution smaller than {int(screenWidthInputValue.split('.')[0])} × {screen_height}"
                    fullScreenAllow = "Not Decided"
                    screenWidthInputValue, screenHeightInputValue = "", ""
            if tooSimilar == True:
                if fullScreenAllow == "Yes":
                    screenWidthInputValue = str(float(screen_height) * (4/3))
                    resize_assets(int(screenWidthInputValue.split('.')[0]), screen_height, True)
                    fullScreenAllow = "Not Decided"
                    errorMessage = "Resolution Changed Successfully."
                    newlineMessage = f"New resolution is: {int(screenWidthInputValue.split('.')[0])} × {screen_height}"
                    screenWidthInputValue, screenHeightInputValue = "", ""
                elif fullScreenAllow == "No":
                    try:
                        resize_assets(int(screenWidthInputValue.split('.')[0]), int(screenHeightInputValue.split('.')[0]))
                        fullScreenAllow = "Not Decided"
                        errorMessage = "Resolution Changed Successfully."
                        newlineMessage = f"New resolution is: {int(screenWidthInputValue.split('.')[0])} × {int(screenHeightInputValue.split('.')[0])}"
                        screenWidthInputValue, screenHeightInputValue = "", ""
                    except ValueError:
                        pass
        
        newlineMessageClickNo = pygame.Rect(int(225 * resizeScale), int(400 * resizeScale), int(150 * resizeScale), int(75 * resizeScale))
        newlineMessageClickYes = pygame.Rect(int(425 * resizeScale), int(400 * resizeScale), int(150 * resizeScale), int(75 * resizeScale))
        newlineMessageClickNoText = gameFontSubtitle.render("No", True, WHITE)
        newlineMessageClickYesText = gameFontSubtitle.render("Yes", True, WHITE)
        
        # Render the "Enter" button
        if len(screenWidthInputValue) == 3 or len(screenWidthInputValue) == 4:
            buttonColour = submitInputButtonActiveColour 
        else:
            buttonColour = submitInputButtonColour
        pygame.draw.rect(window, buttonColour, submitInputButton)
        enter_text = font.render("Enter", True, WHITE)
        enter_rect = enter_text.get_rect(center=submitInputButton.center)
        window.blit(enter_text, enter_rect)

        # Update the display
        pygame.display.update()

        remove_transparent_pixels(homeButtonScaled, (int(resizeScale * 600), int(resizeScale * 400)))
        # Change cursor image if hovering over input box
        if inputBoxScreenWidth.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        if inputBoxScreenHeight.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        
        if not inputBoxScreenHeight.collidepoint(pygame.mouse.get_pos()) and not inputBoxScreenWidth.collidepoint(pygame.mouse.get_pos()) and not remove_transparent_pixels(homeButtonScaled, (int(resizeScale * 600), int(resizeScale * 400))) and not newlineMessageClickNo.collidepoint(pygame.mouse.get_pos()) and not newlineMessageClickYes.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor()

        clock.tick(60)


def resize_assets(new_width, new_height, choseFullScreen = False):
    global window_width, window_height
    global resizeScale
    global window
    if choseFullScreen:
        window = pygame.display.set_mode((new_width, new_height), pygame.FULLSCREEN) # Resize the game window
    else:
        window = pygame.display.set_mode((new_width, new_height)) # Resize the game window
    resizeScale = new_width / window_width # Calculate scale factors for asset resizing
    
    # Resize assets
    global gameFontStart
    global gameFont
    global gameFontSubtitle
    global gameFontEnd
    global gameFontCred
    
    gameFontStart = pygame.font.Font(GAMEPLAY_FONT, int(50 * resizeScale)) # size 50 font
    gameFont = pygame.font.Font(GAMEPLAY_FONT, int(20 * resizeScale)) # size 20 font
    gameFontSubtitle = pygame.font.Font(GAMEPLAY_FONT, int(24 * resizeScale)) # size 24 font
    gameFontEnd = pygame.font.Font(GAMEPLAY_FONT, int(40 * resizeScale)) # size 40 font
    gameFontCred = pygame.font.Font(GAMEPLAY_FONT, int(30 * resizeScale)) # size 30 font
    
    global bg
    bg = pygame.Rect(int(50 * resizeScale), int(100 * resizeScale), int(700 * resizeScale), int(450 * resizeScale))
    
    global mainPageImageScaled
    mainPageImageScaled = pygame.transform.scale(logo, (int(resizeScale * 450), int(resizeScale * 450)))
    global settingsScaled
    settingsScaled = pygame.transform.scale(settings, (int(resizeScale * 64), int(resizeScale * 70)))
    global settingsScaled2
    settingsScaled2 = pygame.transform.scale(settings, (int(resizeScale * 109.4), int(resizeScale * 120)))
    global leaderboardScaled
    leaderboardScaled = pygame.transform.scale(leaderboard, (int(resizeScale * 68), int(resizeScale * 68)))
    global exitScaled
    exitScaled = pygame.transform.scale(exit, (int(resizeScale * 68), int(resizeScale * 68)))
    global heartImageFullScaled
    heartImageFullScaled = pygame.transform.scale(heartImageFull, (int(resizeScale * 36), int(resizeScale * 36)))
    global heartImageEmptyScaled
    heartImageEmptyScaled = pygame.transform.scale(heartImageEmpty, (int(resizeScale * 36), int(resizeScale * 36)))
    global heart1
    global heart2
    global heart3
    heart1 = heartImageFullScaled
    heart2 = heartImageFullScaled
    heart3 = heartImageFullScaled
    global blueLightScaled
    blueLightScaled = pygame.transform.scale(blueLight, (int(resizeScale * 225), int(resizeScale * 225)))
    global blueScaled
    blueScaled = pygame.transform.scale(blue, (int(resizeScale * 225), int(resizeScale * 225)))
    global greenLightScaled
    greenLightScaled = pygame.transform.scale(greenLight, (int(resizeScale * 225), int(resizeScale * 225)))
    global greenScaled
    greenScaled = pygame.transform.scale(green, (int(resizeScale * 225), int(resizeScale * 225)))
    global redLightScaled
    redLightScaled = pygame.transform.scale(redLight, (int(resizeScale * 225), int(resizeScale * 225)))
    global redScaled
    redScaled = pygame.transform.scale(red, (int(resizeScale * 225), int(resizeScale * 225)))
    global yellowLightScaled
    yellowLightScaled = pygame.transform.scale(yellowLight, (int(resizeScale * 225), int(resizeScale * 225)))
    global yellowScaled
    yellowScaled = pygame.transform.scale(yellow, (int(resizeScale * 225), int(resizeScale * 225)))
    global soundOnScaled
    soundOnScaled = pygame.transform.scale(soundOn, (int(resizeScale * 54), int(resizeScale * 54)))
    global soundOffScaled
    soundOffScaled = pygame.transform.scale(soundOff, (int(resizeScale * 87), int(resizeScale * 87)))
    global soundSliderScaled
    soundSliderScaled = pygame.transform.scale(soundSlider, (int(resizeScale * 26), int(resizeScale * 26)))
    global sliderX
    global soundImage
    global soundLocation
    sliderX = (volume * int(resizeScale * 525)) + int(resizeScale * 180)
    print(volume)
    if volume > 0:
        soundImage = soundOnScaled
        soundLocation = (int(resizeScale * 100), int(resizeScale * 200))
    else:
        soundImage = soundOffScaled
        soundLocation = (int(resizeScale * 85), int(resizeScale * 185))
    global homeButtonScaled
    homeButtonScaled = pygame.transform.scale(homeButton, (int(resizeScale * 100), int(resizeScale * 100)))
    global restartButtonScaled
    restartButtonScaled = pygame.transform.scale(restartButton, (int(resizeScale * 95), int(resizeScale * 95)))
    global nextPageScaled
    nextPageScaled = pygame.transform.scale(nextPage, (int(resizeScale * 51), int(resizeScale * 51)))
    global backPageScaled
    backPageScaled = pygame.transform.scale(backPage, (int(resizeScale * 51), int(resizeScale * 51)))
    global bobbingBottomScaled
    bobbingBottomScaled = pygame.transform.scale(bobbingBottom, (int(resizeScale * bobbingBottom.get_width()*3), int(resizeScale * bobbingBottom.get_height()*3)))
    global bobbingTopScaled
    bobbingTopScaled = pygame.transform.scale(bobbingTop, (int(resizeScale * bobbingTop.get_width()*3), int(resizeScale * bobbingTop.get_height()*3)))
    global lookingUpScaled
    lookingUpScaled = pygame.transform.scale(lookingUp, (int(resizeScale * lookingUp.get_width()*3), int(resizeScale * lookingUp.get_height()*3)))
    global lookingUpBlueLitScaled
    lookingUpBlueLitScaled = pygame.transform.scale(lookingUpBlueLit, (int(resizeScale * lookingUpBlueLit.get_width()*3), int(resizeScale * lookingUpBlueLit.get_height()*3)))
    global lookingUpGreenLitScaled
    lookingUpGreenLitScaled = pygame.transform.scale(lookingUpGreenLit, (int(resizeScale * lookingUpGreenLit.get_width()*3), int(resizeScale * lookingUpGreenLit.get_height()*3)))
    global lookingUpRedLitScaled
    lookingUpRedLitScaled = pygame.transform.scale(lookingUpRedLit, (int(resizeScale * lookingUpRedLit.get_width()*3), int(resizeScale * lookingUpRedLit.get_height()*3)))
    global lookingUpYellowLitScaled
    lookingUpYellowLitScaled = pygame.transform.scale(lookingUpYellowLit, (int(resizeScale * lookingUpYellowLit.get_width()*3), int(resizeScale * lookingUpYellowLit.get_height()*3)))
    global layingDownLScaled
    layingDownLScaled = pygame.transform.scale(layingDownL, (int(resizeScale * layingDownL.get_width()*3), int(resizeScale * layingDownL.get_height()*3)))
    global layingDownRScaled
    layingDownRScaled = pygame.transform.scale(layingDownR, (int(resizeScale * layingDownR.get_width()*3), int(resizeScale * layingDownR.get_height()*3)))
    global lookingLeftScaled
    lookingLeftScaled = pygame.transform.scale(lookingLeft, (int(resizeScale * lookingLeft.get_width()*3), int(resizeScale * lookingLeft.get_height()*3)))
    global lookingLeftBlueScaled
    lookingLeftBlueScaled = pygame.transform.scale(lookingLeftBlue, (int(resizeScale * lookingLeftBlue.get_width()*3), int(resizeScale * lookingLeftBlue.get_height()*3)))
    global lookingLeftGreenScaled
    lookingLeftGreenScaled = pygame.transform.scale(lookingLeftGreen, (int(resizeScale * lookingLeftGreen.get_width()*3), int(resizeScale * lookingLeftGreen.get_height()*3)))
    global lookingLeftRedScaled
    lookingLeftRedScaled = pygame.transform.scale(lookingLeftRed, (int(resizeScale * lookingLeftRed.get_width()*3), int(resizeScale * lookingLeftRed.get_height()*3)))
    global lookingLeftYellowScaled
    lookingLeftYellowScaled = pygame.transform.scale(lookingLeftYellow, (int(resizeScale * lookingLeftYellow.get_width()*3), int(resizeScale * lookingLeftYellow.get_height()*3)))
    global lookingRightScaled
    lookingRightScaled = pygame.transform.scale(lookingRight, (int(resizeScale * lookingRight.get_width()*3), int(resizeScale * lookingRight.get_height()*3)))
    global lookingRightBlueScaled
    lookingRightBlueScaled = pygame.transform.scale(lookingRightBlue, (int(resizeScale * lookingRightBlue.get_width()*3), int(resizeScale * lookingRightBlue.get_height()*3)))
    global lookingRightGreenScaled
    lookingRightGreenScaled = pygame.transform.scale(lookingRightGreen, (int(resizeScale * lookingRightGreen.get_width()*3), int(resizeScale * lookingRightGreen.get_height()*3)))
    global lookingRightRedScaled
    lookingRightRedScaled = pygame.transform.scale(lookingRightRed, (int(resizeScale * lookingRightRed.get_width()*3), int(resizeScale * lookingRightRed.get_height()*3)))
    global lookingRightYellowScaled
    lookingRightYellowScaled = pygame.transform.scale(lookingRightYellow, (int(resizeScale * lookingRightYellow.get_width()*3), int(resizeScale * lookingRightYellow.get_height()*3)))
    global platformScaled
    platformScaled = pygame.transform.scale(platform, (int(resizeScale * platform.get_width()*3), int(resizeScale * platform.get_height()*3)))
    global startButtonNormalScaled
    startButtonNormalScaled = pygame.transform.scale(startButtonNormal, (int(resizeScale * 207), int(resizeScale * 88)))
    global startButtonPressedScaled
    startButtonPressedScaled = pygame.transform.scale(startButtonPressed, (int(resizeScale * 207), int(resizeScale * 88)))
    global bgGreenScaled
    bgGreenScaled = pygame.transform.scale(bgGreen, (int(resizeScale * 400), int(resizeScale * 300)))
    global bgRedScaled
    bgRedScaled = pygame.transform.scale(bgRed, (int(resizeScale * 400), int(resizeScale * 300)))
    global bgYellowScaled
    bgYellowScaled = pygame.transform.scale(bgYellow, (int(resizeScale * 400), int(resizeScale * 300)))
    global bgBlueScaled
    bgBlueScaled = pygame.transform.scale(bgBlue, (int(resizeScale * 400), int(resizeScale * 300)))
    global blackGradientScreenScaled
    blackGradientScreenScaled = pygame.transform.scale(blackGradientScreen, (int(resizeScale * 800), int(resizeScale * 600)))
    global forcefield0Scaled
    forcefield0Scaled = pygame.transform.scale(forcefield0, (int(resizeScale * 170), int(resizeScale * 170)))
    global forcefield1Scaled
    forcefield1Scaled = pygame.transform.scale(forcefield1, (int(resizeScale * 170), int(resizeScale * 170)))
    global forcefield2Scaled
    forcefield2Scaled = pygame.transform.scale(forcefield2, (int(resizeScale * 170), int(resizeScale * 170)))
    global forcefield3Scaled
    forcefield3Scaled = pygame.transform.scale(forcefield3, (int(resizeScale * 170), int(resizeScale * 170)))
    global forcefield4Scaled
    forcefield4Scaled = pygame.transform.scale(forcefield4, (int(resizeScale * 170), int(resizeScale * 170)))
    global forcefield5Scaled
    forcefield5Scaled = pygame.transform.scale(forcefield5, (int(resizeScale * 170), int(resizeScale * 170)))
    global forcefield6Scaled
    forcefield6Scaled = pygame.transform.scale(forcefield6, (int(resizeScale * 170), int(resizeScale * 170)))
    global forcefield7Scaled
    forcefield7Scaled = pygame.transform.scale(forcefield7, (int(resizeScale * 170), int(resizeScale * 170)))
    global forcefield8Scaled
    forcefield8Scaled = pygame.transform.scale(forcefield8, (int(resizeScale * 170), int(resizeScale * 170)))
    global forcefield9Scaled
    forcefield9Scaled = pygame.transform.scale(forcefield9, (int(resizeScale * 170), int(resizeScale * 170)))
    global forcefield10Scaled
    forcefield10Scaled = pygame.transform.scale(forcefield10, (int(resizeScale * 170), int(resizeScale * 170)))
    global emptyScaled
    emptyScaled = pygame.transform.scale(empty, (int(resizeScale * 170), int(resizeScale * 170)))
    global redFire0Scaled
    redFire0Scaled = pygame.transform.scale(redFire0, (int(resizeScale * redFire0.get_width()*3), int(resizeScale * redFire0.get_height()*3)))
    global redFire1Scaled
    redFire1Scaled = pygame.transform.scale(redFire1, (int(resizeScale * redFire1.get_width()*3), int(resizeScale * redFire1.get_height()*3)))
    global redFire2Scaled
    redFire2Scaled = pygame.transform.scale(redFire2, (int(resizeScale * redFire2.get_width()*3), int(resizeScale * redFire2.get_height()*3)))
    global redFire3Scaled
    redFire3Scaled = pygame.transform.scale(redFire3, (int(resizeScale * redFire3.get_width()*3), int(resizeScale * redFire3.get_height()*3)))
    global redFire4Scaled
    redFire4Scaled = pygame.transform.scale(redFire4, (int(resizeScale * redFire4.get_width()*3), int(resizeScale * redFire4.get_height()*3)))
    global redFire5Scaled
    redFire5Scaled = pygame.transform.scale(redFire5, (int(resizeScale * redFire5.get_width()*3), int(resizeScale * redFire5.get_height()*3)))
    global redFire6Scaled
    redFire6Scaled = pygame.transform.scale(redFire6, (int(resizeScale * redFire6.get_width()*3), int(resizeScale * redFire6.get_height()*3)))
    global blueFire0Scaled
    blueFire0Scaled = pygame.transform.scale(blueFire0, (int(resizeScale * blueFire0.get_width()*3), int(resizeScale * blueFire0.get_height()*3)))
    global blueFire1Scaled
    blueFire1Scaled = pygame.transform.scale(blueFire1, (int(resizeScale * blueFire1.get_width()*3), int(resizeScale * blueFire1.get_height()*3)))
    global blueFire2Scaled
    blueFire2Scaled = pygame.transform.scale(blueFire2, (int(resizeScale * blueFire2.get_width()*3), int(resizeScale * blueFire2.get_height()*3)))
    global blueFire3Scaled
    blueFire3Scaled = pygame.transform.scale(blueFire3, (int(resizeScale * blueFire3.get_width()*3), int(resizeScale * blueFire3.get_height()*3)))
    global blueFire4Scaled
    blueFire4Scaled = pygame.transform.scale(blueFire4, (int(resizeScale * blueFire4.get_width()*3), int(resizeScale * blueFire4.get_height()*3)))
    global blueFire5Scaled
    blueFire5Scaled = pygame.transform.scale(blueFire5, (int(resizeScale * blueFire5.get_width()*3), int(resizeScale * blueFire5.get_height()*3)))
    global blueFire6Scaled
    blueFire6Scaled = pygame.transform.scale(blueFire6, (int(resizeScale * blueFire6.get_width()*3), int(resizeScale * blueFire6.get_height()*3)))
    global nothingScaled
    nothingScaled = pygame.transform.scale(nothing, (int(resizeScale * 32), int(resizeScale * 32)))
    global pengImage
    pengImage = bobbingBottomScaled
    global pengPos
    pengPos = [int(resizeScale * window_width)//2 - pengImage.get_width()/2, int(resizeScale * window_height)//2]
    global pengImageLast
    pengImageLast = bobbingTopScaled
    global fireSlideRed
    fireSlideRed = [redFire0Scaled, redFire1Scaled, redFire2Scaled, redFire3Scaled, redFire4Scaled, redFire5Scaled, redFire6Scaled]
    global fireSlideBlue
    fireSlideBlue = [blueFire0Scaled, blueFire1Scaled, blueFire2Scaled, blueFire3Scaled, blueFire4Scaled, blueFire5Scaled, blueFire6Scaled]
    global forcefieldSlide
    forcefieldSlide = [emptyScaled, forcefield0Scaled, forcefield1Scaled, forcefield2Scaled, forcefield3Scaled, forcefield4Scaled, forcefield5Scaled, forcefield6Scaled, forcefield7Scaled, forcefield8Scaled, forcefield9Scaled, forcefield10Scaled]
    global bombScaled
    bombScaled = pygame.transform.scale(bomb, (int(resizeScale * bomb.get_width() * 3), int(resizeScale * bomb.get_height() * 3)))
    global cherryScaled
    cherryScaled = pygame.transform.scale(cherry, (int(resizeScale * cherry.get_width() * 2), int(resizeScale * cherry.get_height() * 2)))
    global petrolScaled
    petrolScaled = pygame.transform.scale(petrol, (int(resizeScale * petrol.get_width() * 3), int(resizeScale * petrol.get_height() * 3)))
    global petrolLifeScaled
    petrolLifeScaled = pygame.transform.scale(petrol, (int(resizeScale * petrol.get_width() * 5), int(resizeScale * petrol.get_height() * 5)))
    global images
    images = [bombScaled.convert_alpha(), cherryScaled.convert_alpha(), petrolScaled.convert_alpha()]
    global restartButtonWhiteScaled
    restartButtonWhiteScaled = pygame.transform.scale(restartButtonWhite, (int(resizeScale * 50), int(resizeScale * 50)))


def render_credits_screen():
    credBg = pygame.Rect(int(200 * resizeScale), int(50 * resizeScale), int(400 * resizeScale), int(100 * resizeScale))
    credText = gameFontStart.render('Credits', True, WHITE)
    ben = gameFontCred.render('Benjamin See', True, WHITE)
    shou = gameFontCred.render('Shou-Yi Lai', True, WHITE)
    tanya = gameFontCred.render('Tanya W.', True, WHITE)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if remove_transparent_pixels(homeButtonScaled, (int(600 * resizeScale), int(400 * resizeScale))):
                    render_game_start_page()
        window.fill(GREY)
        window.blit(blackGradientScreenScaled, (0,0))
        pygame.draw.rect(window, BLACK, bg)
        if resizeScale < 0.5:
            lineThickness = 1
        else:
            lineThickness = int(resizeScale * 2)
        pygame.draw.rect(window, WHITE, bg, lineThickness)
        pygame.draw.rect(window, BLACK, credBg)
        pygame.draw.rect(window, WHITE, credBg, lineThickness)
        window.blit(homeButtonScaled, (int(600 * resizeScale), int(400 * resizeScale)))
        window.blit(credText, (int(225 * resizeScale), int(75 * resizeScale)))
        window.blit(ben, (int(150 * resizeScale), int(200 * resizeScale)))
        window.blit(shou, (int(150 * resizeScale), int(300 * resizeScale)))
        window.blit(tanya, (int(150 * resizeScale), int(400 * resizeScale)))
        remove_transparent_pixels(homeButtonScaled, (int(600 * resizeScale), int(400 * resizeScale)))
        if not remove_transparent_pixels(homeButtonScaled, (int(600 * resizeScale), int(400 * resizeScale))):
            pygame.mouse.set_cursor()
        pygame.display.update()


def render_game_rules_screen():
    waiting = True
    textToShowNum = 1
    goHomeTextColour = WHITE
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if remove_transparent_pixels(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale))):
                    textToShowNum = textToShowNum - 1
                    if textToShowNum < 1:
                        textToShowNum = 1
                if remove_transparent_pixels(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale))):
                    textToShowNum = textToShowNum + 1
                    if textToShowNum > 3:
                        textToShowNum = 3
                if goHomeText.get_rect(topleft=(int(225 * resizeScale), int(475 * resizeScale))).collidepoint(pygame.mouse.get_pos()) and textToShowNum == 3:
                    render_game_start_page()
        window.fill(GREY)
        window.blit(blackGradientScreenScaled, (0,0))
        pygame.draw.rect(window, BLACK, bg)
        if resizeScale < 0.5:
            lineThickness = 1
        else:
            lineThickness = int(resizeScale * 2)
        pygame.draw.rect(window, WHITE, bg, lineThickness)
        titleText = gameFontEnd.render('Game Rules', True, WHITE)
        window.blit(titleText, (int(205 * resizeScale), int(35 * resizeScale)))
        pageNum = gameFont.render(str(textToShowNum) + "/3", True, WHITE)
        window.blit(pageNum, ((int(window_width * resizeScale)-pageNum.get_width()-int(70 * resizeScale)), int(515 * resizeScale)))
        if textToShowNum == 1:
            window.blit(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale)))
            remove_transparent_pixels(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale)))
            linesP1 = ["The following game is a", "python recreation of the", "1978 children's toy 'Simon'", "by Ralph H. Baer and", "Howard J. Morrison"]
            y = int(250 * resizeScale)
            for n in linesP1:
                text = gameFont.render(n, True, WHITE)
                window.blit(text, ((int(resizeScale * window_width)-text.get_width())/2, y))
                y = y + int(25 * resizeScale)
            if not remove_transparent_pixels(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale))):
                pygame.mouse.set_cursor()
        elif textToShowNum == 2:
            window.blit(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale)))
            window.blit(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale)))
            remove_transparent_pixels(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale)))
            remove_transparent_pixels(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale)))
            linesP2 = ["The game has four coloured", "buttons where each button", "produces a unique tone when", "it is pressed or activated.", "One round in the game", "consists of one or more", "colours lighting up and", "sounding in a random order.", "After, the player must", "reproduce that pattern by", "pressing the buttons.", "As the game progresses,"]
            y = int(175 * resizeScale)
            for o in linesP2:
                window.blit(gameFont.render(o, True, WHITE), (int(140 * resizeScale), y))
                y = y + int(25 * resizeScale)
            if not remove_transparent_pixels(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale))) and not remove_transparent_pixels(backPageScaled, (int(675 * resizeScale), int(299.5 * resizeScale))):
                pygame.mouse.set_cursor()
        elif textToShowNum == 3:
            window.blit(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale)))
            remove_transparent_pixels(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale)))
            linesP3 = ["the number of buttons", "that needs to be pressed", "increases. The speed which", "the colour pattern is", "played at also gets faster", "every 5 turns. You are", "given 3 lives. Your goal", "is to get the highest", "score in those 3 lives to", "get onto the leaderboard.", ""]
            y = int(150 * resizeScale)
            for p in linesP3:
                window.blit(gameFont.render(p, True, WHITE), (int(140 * resizeScale), y))
                y = y + int(25 * resizeScale)
            page3line12 = gameFont.render("Good Luck :)", True, WHITE)
            window.blit(page3line12, ((int(window_width * resizeScale)-page3line12.get_width())/2, int(425 * resizeScale)))
            window.blit(goHomeText, (int(225 * resizeScale), int(475 * resizeScale)))
            if goHomeText.get_rect(topleft=(int(225 * resizeScale), int(475 * resizeScale))).collidepoint(pygame.mouse.get_pos()):
                goHomeTextColour = RED
                if not soundPlayed:
                    pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                    soundPlayed = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                goHomeTextColour = WHITE
                soundPlayed = False
            if not remove_transparent_pixels(nextPageScaled, (int(75 * resizeScale), int(299.5 * resizeScale))) and not goHomeText.get_rect(topleft=(int(225 * resizeScale), int(475 * resizeScale))).collidepoint(pygame.mouse.get_pos()):
                pygame.mouse.set_cursor()
        goHomeText = gameFontCred.render('Back to Game', True, goHomeTextColour)
        pygame.display.update()


def render_game_over_screen():
    # reset the game variables
    global storeScore
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
    pattern = []
    global timeDelay
    timeDelay = 500
    global playerPattern
    playerPattern = []
    global boost
    boost = False
    global up
    up = 0.11
    global imageCounter
    imageCounter = 0
    global pengSpeed
    pengSpeed = [0, 0]
    global pengImage
    pengImage = bobbingBottomScaled
    global pengPos
    pengPos = [int(resizeScale * window_width)//2 - pengImage.get_width()/2, int(resizeScale * window_height)//2]
    global pengImageLast
    pengImageLast = bobbingTopScaled
    global rocketFireAnimation
    rocketFireAnimation = nothingScaled
    global slideNum
    slideNum = 0
    global showLives
    showLives = False
    global forcefieldNum
    forcefieldNum = 0
    global forcefieldActive
    forcefieldActive = True
    global forcefieldOpening
    forcefieldOpening = True
    global forcefieldClosing
    forcefieldClosing = False
    global canRandomPattern
    canRandomPattern = True
    global pengPatternCounter
    pengPatternCounter = 0
    global patternStarted
    patternStarted = False
    global timerHasBeenSet
    timerHasBeenSet = False
    global pengModeLifeStore
    pengModeLifeStore = life
    global displayBoxColour
    displayBoxColour = GREY
    global pengModeCanShowPattern
    pengModeCanShowPattern = True
    global canShowPattern
    canShowPattern = False
    global flagForRestart
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if remove_transparent_pixels(homeButtonScaled, (int(279 * resizeScale), int(300 * resizeScale))):
                    pygame.mixer.Channel(1).play(mainMenuTune, -1)
                    render_game_start_page()
                elif restartButtonScaled.get_rect(topleft=(int(421 * resizeScale), int(300 * resizeScale))).collidepoint(pygame.mouse.get_pos()):
                    lifeStore = 1
                    pengModeLifeStore = 1
                    waiting = False
                    flagForRestart = False
        window.fill(GREY)
        window.blit(blackGradientScreenScaled, (0, 0))
        gameOverText = gameFontEnd.render('Game Over', True, WHITE) # write the words
        window.blit(gameOverText, (int(223 * resizeScale), int(200 * resizeScale)))
        gameOverText = gameFont.render('Score: ' + str(storeScore), True, WHITE) # write the words
        window.blit(gameOverText, (int(50 * resizeScale), int(50 * resizeScale)))
        window.blit(homeButtonScaled, (int(279 * resizeScale), int(300 * resizeScale)))
        window.blit(restartButtonScaled, (int(421 * resizeScale), int(300 * resizeScale)))
        
        remove_transparent_pixels(homeButtonScaled, (int(279 * resizeScale), int(300 * resizeScale)))
        if restartButtonScaled.get_rect(topleft=(int(421 * resizeScale), int(300 * resizeScale))).collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if not soundPlayed:
                pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                soundPlayed = True
        else:
            soundPlayed = False
        if not remove_transparent_pixels(homeButtonScaled, (int(279 * resizeScale), int(300 * resizeScale))) and not restartButtonScaled.get_rect(topleft=(int(421 * resizeScale), int(300 * resizeScale))).collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor()
        
        pygame.display.update()


def render_save_score_screen():
    row1 = ['A' ,'B' ,'C' ,'D' ,'E' ,'F' ,'G' ,'H' ,'I' ,'J']
    row1X = [172, 220, 268, 316, 364, 412, 460, 508, 556, 604]
    for i, j in enumerate(row1X):
        store = int(resizeScale * row1X.pop(i))
        row1X.insert(i, store)
    row1Y = int(resizeScale * 160)

    row2 = ['K' ,'L' ,'M' ,'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T']
    row2X = [172, 220, 268, 316, 364, 412, 460, 508, 556, 604]
    for i, j in enumerate(row2X):
        store = int(resizeScale * row2X.pop(i))
        row2X.insert(i, store)
    row2Y = int(resizeScale * 200)

    row3 = ['U' ,'V' ,'W' ,'X' ,'Y' ,'Z']
    row3X = [172, 220, 268, 316, 364, 412, 460, 508]
    for i, j in enumerate(row3X):
        store = int(resizeScale * row3X.pop(i))
        row3X.insert(i, store)
    row3Y = int(resizeScale * 240)
    global initial
    initial = []
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = [0, 1, 2, 3, 4, 5]
    errorTextColour = BLACK
    okTextColour = WHITE
    okText = gameFontEnd.render('OK', True, okTextColour)
    saveBg = pygame.Rect(int(300 * resizeScale), int(25 * resizeScale), int(200 * resizeScale), int(100 * resizeScale))
    titleText = gameFontEnd.render('Save', True, WHITE)
    hyphen = gameFontSubtitle.render('-', True, WHITE)
    delete = gameFontSubtitle.render('DEL', True, WHITE)
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if okText.get_rect(topleft=(int(625 * resizeScale), int(475 * resizeScale))).collidepoint(pygame.mouse.get_pos()):
                    if len(initial) == 3:
                        update_file()
                        render_game_over_screen()
                        waiting = False
                    else:
                        print('Please Choose 3 Letters')
                        errorTextColour = WHITE
                for e in nums:
                    row1Letter = gameFontSubtitle.render(row1[e], True, WHITE)
                    if row1Letter.get_rect(topleft=(row1X[e], row1Y)).collidepoint(pygame.mouse.get_pos()) and len(initial) < 3:
                        initial.append(row1[e])
                        print(initial)
                        errorTextColour = BLACK
                for f in nums:
                    row2Letter = gameFontSubtitle.render(row2[f], True, WHITE)
                    if row2Letter.get_rect(topleft=(row2X[f], row2Y)).collidepoint(pygame.mouse.get_pos()) and len(initial) < 3:
                        initial.append(row2[f])
                        print(initial)
                        errorTextColour = BLACK
                for g in num:
                    row3Letter = gameFontSubtitle.render(row3[g], True, WHITE)
                    if row3Letter.get_rect(topleft=(row3X[g], row3Y)).collidepoint(pygame.mouse.get_pos()) and len(initial) < 3:
                        initial.append(row3[g])
                        print(initial)
                        errorTextColour = BLACK
                if delete.get_rect(topleft=(int(resizeScale * 556), row3Y)).collidepoint(pygame.mouse.get_pos()):
                    errorTextColour = BLACK
                    try:
                        initial.pop(-1)
                    except IndexError:
                        pass
                if hyphen.get_rect(topleft=(int(resizeScale * 484), row3Y)).collidepoint(pygame.mouse.get_pos()):
                    if len(initial) < 3:
                        initial.append('-')
                        print(initial)
                        errorTextColour = BLACK
        window.fill(GREY)
        window.blit(blackGradientScreenScaled, (0, 0))
        pygame.draw.rect(window, BLACK, bg)
        if resizeScale < 0.5:
            lineThicknessBox = 1
        else:
            lineThicknessBox = int(resizeScale * 2)
        pygame.draw.rect(window, WHITE, bg, lineThicknessBox)
        pygame.draw.rect(window, BLACK, saveBg)
        pygame.draw.rect(window, WHITE, saveBg, lineThicknessBox)
        window.blit(titleText, (((int(resizeScale * window_width)-titleText.get_width())/2), int(55 * resizeScale)))
        if okText.get_rect(topleft=(int(625 * resizeScale), int(475 * resizeScale))).collidepoint(pygame.mouse.get_pos()):
            okTextColour = RED
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if not soundPlayed:
                pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                soundPlayed = True
        else:
            okTextColour = WHITE
            soundPlayed = False
        okText = gameFontEnd.render('OK', True, okTextColour)
        window.blit(okText, (int(625 * resizeScale), int(475 * resizeScale)))
        
        if resizeScale < 0.5:
            lineThickness = 1
        else:
            lineThickness = int(resizeScale * 4)
        
        for i, j in zip(row1, row1X):
            window.blit(gameFontSubtitle.render(i, True, WHITE), (j, row1Y))
            if gameFontSubtitle.render(i, True, WHITE).get_rect(topleft=(j, row1Y)).collidepoint(pygame.mouse.get_pos()):
                pygame.draw.line(window, RED, (j-int(resizeScale * 2), row1Y+int(resizeScale * 24)), (j+int(resizeScale * 24), row1Y+int(resizeScale * 24)), lineThickness)
            if not soundPlayed:
                pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                soundPlayed = True
        else:
            soundPlayed = False
        for a, b in zip(row2, row2X):
            window.blit(gameFontSubtitle.render(a, True, WHITE), (b, row2Y))
            if gameFontSubtitle.render(a, True, WHITE).get_rect(topleft=(b, row2Y)).collidepoint(pygame.mouse.get_pos()):
                pygame.draw.line(window, RED, (b-int(resizeScale * 2), row2Y+int(resizeScale * 24)), (b+int(resizeScale * 24), row2Y+int(resizeScale * 24)), lineThickness)
            if not soundPlayed:
                pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                soundPlayed = True
        else:
            soundPlayed = False
        for c, d in zip(row3, row3X):
            window.blit(gameFontSubtitle.render(c, True, WHITE), (d, row3Y))
            if gameFontSubtitle.render(c, True, WHITE).get_rect(topleft=(d, row3Y)).collidepoint(pygame.mouse.get_pos()):
                pygame.draw.line(window, RED, (d-int(resizeScale * 2), row3Y+int(resizeScale * 24)), (d+int(resizeScale * 24), row3Y+int(resizeScale * 24)), lineThickness)
            if not soundPlayed:
                pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                soundPlayed = True
        else:
            soundPlayed = False
        
        window.blit(hyphen, (int(resizeScale * 484), row3Y))
        window.blit(delete, (int(resizeScale * 556), row3Y))
        if hyphen.get_rect(topleft=(int(resizeScale * 484), row3Y)).collidepoint(pygame.mouse.get_pos()):
            pygame.draw.line(window, RED, (int(resizeScale * 486), row3Y+int(resizeScale * 24)), (int(resizeScale * 508), row3Y+int(resizeScale * 24)), lineThickness)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if not soundPlayed:
                pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                soundPlayed = True
        else:
            soundPlayed = False
        if delete.get_rect(topleft=(int(resizeScale * 556), row3Y)).collidepoint(pygame.mouse.get_pos()):
            pygame.draw.line(window, RED, (int(resizeScale * 554), row3Y+int(resizeScale * 24)), (int(resizeScale * 556)+delete.get_width(), row3Y+int(resizeScale * 24)), lineThickness)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if not soundPlayed:
                pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                soundPlayed = True
        else:
            soundPlayed = False
        pygame.draw.line(window, WHITE, (int(resizeScale * 285), int(resizeScale * 450)), (int(resizeScale * 355), int(resizeScale * 450)), lineThickness)
        pygame.draw.line(window, WHITE, (int(resizeScale * 365), int(resizeScale * 450)), (int(resizeScale * 435), int(resizeScale * 450)), lineThickness)
        pygame.draw.line(window, WHITE, (int(resizeScale * 445), int(resizeScale * 450)), (int(resizeScale * 515), int(resizeScale * 450)), lineThickness)
        try:
            letter1 = gameFontStart.render(initial[0], True, WHITE)
            window.blit(letter1, ((((int(resizeScale * 70)-letter1.get_width())/2)+int(resizeScale * 288)), int(resizeScale * 400)))
        except IndexError:
            pass
        try:
            letter2 = gameFontStart.render(initial[1], True, WHITE)
            window.blit(letter2, ((((int(resizeScale * 70)-letter2.get_width())/2)+int(resizeScale * 368)), int(resizeScale * 400)))
        except IndexError:
            pass
        try:
            letter3 = gameFontStart.render(initial[2], True, WHITE)
            window.blit(letter3, ((((int(resizeScale * 70)-letter3.get_width())/2)+int(resizeScale * 448)), int(resizeScale * 400)))
        except IndexError:
            pass
        errorText = gameFont.render('Please Choose 3 Letters', True, errorTextColour)
        window.blit(errorText, ((int(resizeScale * window_width)-errorText.get_width())/2, int(resizeScale * 525)))
        
        if not okText.get_rect(topleft=(int(625 * resizeScale), int(475 * resizeScale))).collidepoint(pygame.mouse.get_pos()) and not delete.get_rect(topleft=(int(resizeScale * 556), row3Y)).collidepoint(pygame.mouse.get_pos()) and not hyphen.get_rect(topleft=(int(resizeScale * 484), row3Y)).collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor()
        
        pygame.display.update()


def update_file():
    # # The 'a' means append (as opposed to 'w' for write which will clear the file before writing.)
    try:
        highScores = open(f'./Files/high_scores_{gameMode}.csv', 'a', newline='')
    except PermissionError:
        return
    fileWriter = csv.writer(highScores, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
    fileWriter.writerow([score, initial[0] + initial[1] + initial[2]])
    print('High Scores saved to file.')
    highScores.close()


def render_leaderboard_screen():
    waiting = True
    modeBox1 = pygame.Rect(int(225 * resizeScale), int(200 * resizeScale), int(350 * resizeScale), int(75 * resizeScale))
    modeBox2 = pygame.Rect(int(225 * resizeScale), int(300 * resizeScale), int(350 * resizeScale), int(75 * resizeScale))
    modeBox3 = pygame.Rect(int(225 * resizeScale), int(400 * resizeScale), int(350 * resizeScale), int(75 * resizeScale))
    modeBox4 = pygame.Rect(int(412.5 * resizeScale), int(175 * resizeScale), int(262.5 * resizeScale), int(75 * resizeScale))
    modeBox5 = pygame.Rect(int(412.5 * resizeScale), int(275 * resizeScale), int(262.5 * resizeScale), int(75 * resizeScale))
    modeBox6 = pygame.Rect(int(412.5 * resizeScale), int(375 * resizeScale), int(262.5 * resizeScale), int(75 * resizeScale))
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if settingsDict["unlockedExtraModes"] == False:
                    if modeBox1.collidepoint(pygame.mouse.get_pos()):
                        show_rankings("Easy")
                    if modeBox2.collidepoint(pygame.mouse.get_pos()):
                        show_rankings("Normal")
                    if modeBox3.collidepoint(pygame.mouse.get_pos()):
                        show_rankings("Hard")
                if settingsDict["unlockedExtraModes"] == True:
                    if modeBox1.collidepoint(pygame.mouse.get_pos()):
                        show_rankings("Easy")
                    if modeBox2.collidepoint(pygame.mouse.get_pos()):
                        show_rankings("Normal")
                    if modeBox3.collidepoint(pygame.mouse.get_pos()):
                        show_rankings("Hard")
                    if modeBox4.collidepoint(pygame.mouse.get_pos()):
                        show_rankings("Penguin")
                    if modeBox5.collidepoint(pygame.mouse.get_pos()):
                        show_rankings("Ben")
                    if modeBox6.collidepoint(pygame.mouse.get_pos()):
                        show_rankings("Insane")
                if remove_transparent_pixels(homeButtonScaled, (int(resizeScale * 650), int(resizeScale * 450))):
                    render_game_start_page()
        window.fill(GREY)
        window.blit(blackGradientScreenScaled, (0,0))
        pygame.draw.rect(window, BLACK, bg)
        if resizeScale < 0.5:
            lineThickness = 1
        else:
            lineThickness = int(resizeScale * 2)
        pygame.draw.rect(window, WHITE, bg, lineThickness)
        leaderboardBg = pygame.Rect(int(100 * resizeScale), int(25 * resizeScale), int(600 * resizeScale), int(100 * resizeScale))
        pygame.draw.rect(window, BLACK, leaderboardBg)
        pygame.draw.rect(window, WHITE, leaderboardBg, lineThickness)
        titleText = gameFontEnd.render('High Scores', True, WHITE)
        window.blit(titleText, ((int(resizeScale * window_width) - titleText.get_width())/2, int(resizeScale * 55)))
        window.blit(homeButtonScaled, (int(resizeScale * 650), int(resizeScale * 450)))
        remove_transparent_pixels(homeButtonScaled, (int(resizeScale * 650), int(resizeScale * 450)))
        if settingsDict["unlockedExtraModes"] == False and not modeBox1.collidepoint(pygame.mouse.get_pos()) and not modeBox2.collidepoint(pygame.mouse.get_pos()) and not modeBox3.collidepoint(pygame.mouse.get_pos()) and not remove_transparent_pixels(homeButtonScaled, (int(resizeScale * 650), int(resizeScale * 450))):
            pygame.mouse.set_cursor()
        elif settingsDict["unlockedExtraModes"] == True and not modeBox1.collidepoint(pygame.mouse.get_pos()) and not modeBox2.collidepoint(pygame.mouse.get_pos()) and not modeBox3.collidepoint(pygame.mouse.get_pos()) and not modeBox4.collidepoint(pygame.mouse.get_pos()) and not modeBox5.collidepoint(pygame.mouse.get_pos()) and not modeBox6.collidepoint(pygame.mouse.get_pos()) and not remove_transparent_pixels(homeButtonScaled, (int(resizeScale * 650), int(resizeScale * 450))):
            pygame.mouse.set_cursor()
        if settingsDict["unlockedExtraModes"] == False:
            modes = [
                ('Easy', 225, modeBox1),
                ('Normal', 325, modeBox2),
                ('Hard', 425, modeBox3)
                ]
            for modeText, textYPos, modeBox in modes:
                modeBoxColour = WHITE
                pygame.draw.rect(window, BLACK, modeBox)
                if modeBox.collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    modeBoxColour = RED
                    if not soundPlayed:
                        pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                        soundPlayed = True
                else:
                    modeBoxColour = WHITE
                    soundPlayed = False
                pygame.draw.rect(window, modeBoxColour, modeBox, lineThickness)
                modeTextDisplay = gameFontCred.render(modeText, True, WHITE)
                window.blit(modeTextDisplay, (int(resizeScale * window_width) // 2 - modeTextDisplay.get_width() // 2, int(textYPos * resizeScale)))
        if settingsDict["unlockedExtraModes"] == True:
            modeBox1 = pygame.Rect(int(112.5 * resizeScale), int(175 * resizeScale), int(262.5 * resizeScale), int(75 * resizeScale))
            modeBox2 = pygame.Rect(int(112.5 * resizeScale), int(275 * resizeScale), int(262.5 * resizeScale), int(75 * resizeScale))
            modeBox3 = pygame.Rect(int(112.5 * resizeScale), int(375 * resizeScale), int(262.5 * resizeScale), int(75 * resizeScale))
            modeBox4 = pygame.Rect(int(412.5 * resizeScale), int(175 * resizeScale), int(262.5 * resizeScale), int(75 * resizeScale))
            modeBox5 = pygame.Rect(int(412.5 * resizeScale), int(275 * resizeScale), int(262.5 * resizeScale), int(75 * resizeScale))
            modeBox6 = pygame.Rect(int(412.5 * resizeScale), int(375 * resizeScale), int(262.5 * resizeScale), int(75 * resizeScale))
            modes = [
                ('Easy', 200, modeBox1),
                ('Normal', 300, modeBox2),
                ('Hard', 400, modeBox3),
                ('Penguin', 200, modeBox4),
                ('Ben', 300, modeBox5),
                ('Insane', 400, modeBox6)
            ]
            for modeText, textYPos, modeBox in modes:
                modeBoxColour = WHITE
                pygame.draw.rect(window, BLACK, modeBox)
                if modeBox.collidepoint(pygame.mouse.get_pos()):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    modeBoxColour = RED
                    if not soundPlayed:
                        pygame.mixer.Channel(3).play(hoverOverButtonSound, 0, 500)
                        soundPlayed = True
                else:
                    modeBoxColour = WHITE
                    soundPlayed = False
                pygame.draw.rect(window, modeBoxColour, modeBox, lineThickness)
                modeTextDisplay = gameFontCred.render(modeText, True, WHITE)
                window.blit(modeTextDisplay, (modeBox.x + modeBox.w // 2 - modeTextDisplay.get_width() // 2, int(textYPos * resizeScale)))
        pygame.display.update()


def show_rankings(file):
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if remove_transparent_pixels(homeButtonScaled, (int(resizeScale * 650), int(resizeScale * 450))):
                    render_game_start_page()
        window.fill(GREY)
        window.blit(blackGradientScreenScaled, (0,0))
        pygame.draw.rect(window, BLACK, bg)
        if resizeScale < 0.5:
            lineThickness = 1
        else:
            lineThickness = int(resizeScale * 2)
        pygame.draw.rect(window, WHITE, bg, lineThickness)
        leaderboardBg = pygame.Rect(int(100 * resizeScale), int(25 * resizeScale), int(600 * resizeScale), int(100 * resizeScale))
        pygame.draw.rect(window, BLACK, leaderboardBg)
        pygame.draw.rect(window, WHITE, leaderboardBg, lineThickness)
        titleText = gameFontEnd.render(file, True, WHITE)
        window.blit(homeButtonScaled, (int(resizeScale * 650), int(resizeScale * 450)))
        remove_transparent_pixels(homeButtonScaled, (int(resizeScale * 650), int(resizeScale * 450)))
        if not remove_transparent_pixels(homeButtonScaled, (int(resizeScale * 650), int(resizeScale * 450))):
            pygame.mouse.set_cursor()
        
        rank = 1
        suffix = ''
        rankX = 190
        window.blit(titleText, ((int(resizeScale * window_width) - titleText.get_width())/2, int(resizeScale * 55)))
        subtitleText = gameFontSubtitle.render('Rank   Name   Score', True, WHITE)
        window.blit(subtitleText, ((int(resizeScale * window_width)-subtitleText.get_width())/2, int(resizeScale * 150)))
        #Reading from a file
        #Next we will access that file and print the results.
        try:
            scores = open(f'./Files/high_scores_{file}.txt', 'r')
        except PermissionError:
            pass
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
                showRank = gameFont.render(str(rank) + suffix, True, WHITE)
                window.blit(showRank, (int(resizeScale * 96)+((int(resizeScale * window_width)-subtitleText.get_width())/2)-showRank.get_width(), int(resizeScale * rankX)))
                showName = gameFont.render(fields[1], True, WHITE)
                window.blit(showName, (int(resizeScale * 264)+((int(resizeScale * window_width)-subtitleText.get_width())/2)-showName.get_width(), int(resizeScale * rankX)))
                showScore = gameFont.render(fields[0], True, WHITE)
                window.blit(showScore, (int(resizeScale * 456)+((int(resizeScale * window_width)-subtitleText.get_width())/2)-showScore.get_width(), int(resizeScale * rankX)))
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
    global canRandomPattern
    global timerHasBeenSet
    global forcefieldNum
    global redBox1
    global redBox2
    global yellowBox1
    global yellowBox2
    global greenBox1
    global greenBox2
    global blueBox1
    global blueBox2

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == BOOST_EVENT: 
                boost = False
            if event.type == LIFE_LOSS_LIGHT_EVENT:
                redColour, redLightColour = ('#800000'), ('#FF0000')
                blueColour, blueLightColour = ('#001E80'), ('#003DFF')
                yellowColour, yellowLightColour = ('#778000'), ('#F0FF00')
                greenColour, greenLightColour = ('#008000'), ('#25FF00')
            if event.type == RETURN_NORMAL_EVENT:
                forcefieldActive = True
                forcefieldOpening = True
                forcefieldClosing = False
                canRandomPattern = True
                pengModeCanShowPattern = True
                canShowPattern = False
                patternStarted = False
            if event.type == CONTINUE_SHOWING_PATTERN_EVENT:
                if pengPatternCounter < len(pattern):
                    canRandomPattern = False
                    pengModeCanShowPattern = True
                    canShowPattern = True
                    timerHasBeenSet = False
            if event.type == FINISH_SHOWING_PATTERN_EVENT:
                forcefieldClosing = True
                forcefieldActive = False
                forcefieldOpening = False
            if event.type == LIFE_LOSS_CONTINUE_EVENT:
                redColour, redLightColour = ('#FF0000'), ('#800000')
                blueColour, blueLightColour = ('#003DFF'), ('#001E80')
                yellowColour, yellowLightColour = ('#F0FF00'), ('#778000')
                greenColour, greenLightColour = ('#25FF00'), ('#008000')
                pygame.time.set_timer(LIFE_LOSS_LIGHT_EVENT, 500, 1)
        
        window.fill(GREY)
        
        displayBox = pygame.Rect(int(0 * resizeScale), int(0 * resizeScale), int(window_width * resizeScale), int(window_height * resizeScale))
        pygame.draw.rect(window, displayBoxColour, displayBox) # to display the current colour pattern
        coverPrev = pygame.Rect(int(10 * resizeScale), int(10 * resizeScale), int((window_width-20) * resizeScale), int((window_height-20) * resizeScale))
        pygame.draw.rect(window, GREY, coverPrev)

        playAreaColour = ("#001833")
        playAreaBox = pygame.Rect(int(offsetX * resizeScale), int(offsetY * resizeScale), int(550 * resizeScale), int(550 * resizeScale))
        pygame.draw.rect(window, playAreaColour, playAreaBox)
        # draw elements
        # window.blit((gameFont.render('Score: 0', True, WHITE)), (50, 50))
        
        ########## Draw Borders of Game Area ##########
        redBox1 = pygame.Rect(int(offsetX * resizeScale), int(offsetY * resizeScale), int(colourLength * resizeScale), int(colourWidth * resizeScale))
        redBox2 = pygame.Rect(int(offsetX * resizeScale), int(offsetY * resizeScale), int(colourWidth * resizeScale), int(colourLength * resizeScale))
        yellowBox1 = pygame.Rect(int(offsetX * resizeScale), int((window_height - offsetY - colourLength) * resizeScale), int(colourWidth * resizeScale), int(colourLength * resizeScale))
        yellowBox2 = pygame.Rect(int(offsetX * resizeScale), int((window_height - offsetY - colourWidth) * resizeScale), int(colourLength * resizeScale), int(colourWidth * resizeScale))
        greenBox1 = pygame.Rect(int((window_width - offsetX - colourLength) * resizeScale), int(offsetY * resizeScale), int(colourLength * resizeScale), int(colourWidth * resizeScale))
        greenBox2 = pygame.Rect(int((window_width - offsetX - colourWidth) * resizeScale), int(offsetY * resizeScale), int(colourWidth * resizeScale), int(colourLength * resizeScale))
        blueBox1 = pygame.Rect(int((window_width - offsetX - colourLength) * resizeScale), int((window_height - offsetY - colourWidth) * resizeScale), int(colourLength * resizeScale), int(colourWidth * resizeScale))
        blueBox2 = pygame.Rect(int((window_width - offsetX - colourWidth) * resizeScale), int((window_height - offsetY - colourLength) * resizeScale), int(colourWidth * resizeScale), int(colourLength * resizeScale))
        pygame.draw.rect(window, redColour, redBox1)
        pygame.draw.rect(window, redColour, redBox2)
        pygame.draw.rect(window, yellowColour, yellowBox1)
        pygame.draw.rect(window, yellowColour, yellowBox2)
        pygame.draw.rect(window, greenColour, greenBox1)
        pygame.draw.rect(window, greenColour, greenBox2)
        pygame.draw.rect(window, blueColour, blueBox1)
        pygame.draw.rect(window, blueColour, blueBox2)
        ###############################################
        window.blit(platformScaled, (int(resizeScale * window_width)/2 - platformScaled.get_width()/2, int(resizeScale * window_height)/2))
        
        
        if imageCounter % 3 == 0: # 50ms per frame
            if forcefieldOpening == True:
                forcefieldNum = forcefieldNum + 1
                if forcefieldNum > 7:
                    forcefieldNum = 8
                    forcefieldOpening = False
            elif forcefieldClosing == True:
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
        if forcefieldNum == 11 and canRandomPattern == False and canShowPattern == False and patternStarted == False:
            canShowPattern = True
        window.blit(forcefieldSlide[forcefieldNum], (int(resizeScale * window_width)/2 - forcefieldSlide[forcefieldNum].get_width()/2, int(resizeScale * window_height)/2 - forcefieldSlide[forcefieldNum].get_height()/2 - int(resizeScale * 35)))
        
        pygame.time.Clock().tick(FPS)
        peng_mode_game_loop()
        imageCounter = imageCounter + 1


def apply_gravity():
    pengSpeed[1] = pengSpeed[1] + (resizeScale * gravity)


def update_penguin_position():
    global pengImage
    global pengImageLast
    global rocketFireAnimation
    global slideNum
    global fireSlideRed
    global pengRect
    pengPos[0] = pengPos[0] + pengSpeed[0]
    pengPos[1] = pengPos[1] + pengSpeed[1]
    # Update the position of the penguin on the screen
    window.blit(pengImage, pengPos)
    pengRect = pygame.Rect(pengPos[0], pengPos[1], pengImage.get_width(), pengImage.get_height())
    
    ############ ANIMATION ############
    if imageCounter % 45 == 0 and pengPos[1] + pengImage.get_height() >= int(resizeScale * window_height): # every 3/4 seconds if on the floor
        if pengImageLast == bobbingTopScaled:
            pengImage = bobbingTopScaled
            pengImageLast = bobbingBottomScaled
        elif pengImageLast == bobbingBottomScaled:
            pengImage = bobbingBottomScaled
            pengImageLast = bobbingTopScaled
    if imageCounter % 45 == 0 and pengPos[0] < platformScaled.get_width() + int(resizeScale * window_width)/2 - platformScaled.get_width()/2 and pengPos[0] > int(resizeScale * window_width)/2 - platformScaled.get_width()/2 - pengImage.get_width():
        if pengPos[1] > window_height/2 - pengImage.get_height() - 1: # every 3/4 seconds if on the floor
            if pengImageLast == bobbingTopScaled:
                pengImage = bobbingTopScaled
                pengImageLast = bobbingBottomScaled
            elif pengImageLast == bobbingBottomScaled:
                pengImage = bobbingBottomScaled
                pengImageLast = bobbingTopScaled
    ###################################
    
    fireSlide = fireSlideRed    
    if boost:
        fireSlide = fireSlideBlue
    else:
        fireSlide = fireSlideRed
    pressed = pygame.key.get_pressed()
    window.blit(rocketFireAnimation, (pengPos[0] + (pengImage.get_width()/2) - (rocketFireAnimation.get_width()/2), pengPos[1] + pengImage.get_height()))
    if (pressed[settingsDict["up"]]) and imageCounter % 5 == 0: # 12 fps if currently flying
        slideNum = slideNum + 1
        if slideNum > 6:
            slideNum = 0
        rocketFireAnimation = fireSlide[slideNum]
    elif (not pressed[settingsDict["up"]]): # when not up button being pressed
        rocketFireAnimation = nothingScaled
    for item, image, _ in all_items:
        window.blit(image, item)
    for i in range(min(life, 6)):
        window.blit(petrolLifeScaled, (int(resizeScale * 35), int(resizeScale * (35 + i * 85))))


def peng_mode_check_pos():
    global gravity
    # Limit the penguin's position to within the walls of the screen
    if pengPos[0] < int(resizeScale * offsetX): # if past the left side of the play area
        pengPos[0] = int(resizeScale * offsetX)
        pengSpeed[0] = 0
    elif pengPos[0] + pengImage.get_width() > int(resizeScale * window_width) - int(resizeScale * offsetX): # if past the right side of the play area
        pengPos[0] = int(resizeScale * window_width) - pengImage.get_width() - int(resizeScale * offsetX)
        pengSpeed[0] = 0
    if pengPos[1] < int(resizeScale * offsetY): # if past the top of the play area
        pengPos[1] = int(resizeScale * offsetY)
        pengSpeed[1] = 0
    elif pengPos[1] + pengImage.get_height() > int(resizeScale * window_height) - int(resizeScale * offsetY): # if past the bottom of the play area
        pengPos[1] = int(resizeScale * window_height) - pengImage.get_height() - int(resizeScale * offsetY)
        pengSpeed[1] = 0
        pengSpeed[0] = 0
    
    platform_x = int(resizeScale * window_width) // 2
    platform_y = int(resizeScale * window_height) // 2
    platform_left = platform_x - platformScaled.get_width() // 2
    platform_top = platform_y - platformScaled.get_height() // 2
    platform_bottom = platform_y + platformScaled.get_height() // 2
    platform_rect = platformScaled.get_rect(topleft=(platform_left, platform_top))

    if pengRect.colliderect(platform_rect):  # Check if the pengRect collides with the platform_rect
        if pengPos[1] < platform_y:  # Check if pengPos[1] is above the platform
            if not pygame.key.get_pressed()[settingsDict["up"]]: # if they arent moving up
                pengPos[1] = platform_top - pengImage.get_height() + 6
                pengSpeed[1] = 0
                gravity = 0
        elif pengPos[1] + pengRect.height > platform_bottom + 6: # Check if pengPos[1] is below the platform
            pengPos[1] = platform_bottom + 6
            pengSpeed[1] = 0
            gravity = 0
    else:
        gravity = 0.1


def peng_mode_apply_key():
    global pengImage
    global boost
    if boost:
        up = 0.25
    else:
        up = 0.15
    pressed = pygame.key.get_pressed()
    if (pressed[settingsDict["up"]]):
        pengSpeed[1] = pengSpeed[1] - (resizeScale * up)
        pengImage = lookingUpScaled # A way to not interfere with the colour_light() lighting up the player
    if (pressed[settingsDict["right"]]):
        pengSpeed[0] = pengSpeed[0] + (resizeScale * 0.05)
    if (pressed[settingsDict["left"]]):
        pengSpeed[0] = pengSpeed[0] - (resizeScale * 0.05)
    if (pressed[settingsDict["down"]]):
        pengSpeed[1] = pengSpeed[1] + (resizeScale * 0.0)
    if boost != True: # Make sure you cant start the boost while the boost is on
        if (pressed[settingsDict["boost"]]):
            boost = True
            pygame.time.set_timer(BOOST_EVENT, 5000, 1) # A 5 seconds timer (runs once)


def peng_mode_check_wall_pos(wallArea):
    global pengPos
    global pengSpeed
    pointToMoveToX = int(resizeScale * window_width)/2 - pengImage.get_width()/2
    pointToMoveToY = int(resizeScale * window_height)/2 - pengImage.get_height()
    
    if wallArea == "topLeft":
        # print("(" + str(offset+colourLength-pengImage.get_width()) + ", " + str(offset+colourLength-pengImage.get_height()) + ")")
        pengSpeed[1] = 0
        pengSpeed[0] = 0
        gradient = (pointToMoveToY - pengPos[1])/(pointToMoveToX - pengPos[0])
        while pengPos[0] < pointToMoveToX and pengPos[1] < pointToMoveToY:
            pengPos[0] = pengPos[0] + 1
            pengPos[1] = pengPos[1] + gradient
            window.blit(pengImage, pengPos)
            pygame.display.update()
    if wallArea == "topRight":
        # print("(" + str(window_width-offset-colourLength-pengImage.get_width()) + ", " + str(offset+colourLength-pengImage.get_height()) + ")")
        pengSpeed[1] = 0
        pengSpeed[0] = 0
        gradient = (pointToMoveToY - pengPos[1])/(pointToMoveToX - pengPos[0])
        while pengPos[0] > pointToMoveToX and pengPos[1] < pointToMoveToY:
            pengPos[0] = pengPos[0] - 1
            pengPos[1] = pengPos[1] - gradient
            window.blit(pengImage, pengPos)
            pygame.display.update()
    if wallArea == "bottomLeft":
        # print("(" + str(offset+colourLength-pengImage.get_width()) + ", " + str(window_height-offset-colourLength+pengImage.get_height()) + ")")
        pengSpeed[1] = 0
        pengSpeed[0] = 0
        gradient = (pointToMoveToY - pengPos[1])/(pointToMoveToX - pengPos[0])
        while pengPos[0] < pointToMoveToX and pengPos[1] > pointToMoveToY:
            pengPos[0] = pengPos[0] + 1
            pengPos[1] = pengPos[1] + gradient
            window.blit(pengImage, pengPos)
            pygame.display.update()
    if wallArea == "bottomRight":
        # print("(" + str(offset+colourLength-pengImage.get_width()) + ", " + str(window_height-offset-colourLength+pengImage.get_height()) + ")")
        pengSpeed[1] = 0
        pengSpeed[0] = 0
        gradient = (pointToMoveToY - pengPos[1])/(pointToMoveToX - pengPos[0])
        while pengPos[0] > pointToMoveToX and pengPos[1] > pointToMoveToY:
            pengPos[0] = pengPos[0] - 1
            pengPos[1] = pengPos[1] - gradient
            window.blit(pengImage, pengPos)
            pygame.display.update()


def penguin_mode_store_player_guess():
    # 1 = red
    # 2 = green
    # 3 = yellow
    # 4 = blue
    global playerPattern
    global score
    global pengRect
    global redColour
    global greenColour
    global yellowColour
    global blueColour
    global redLightColour
    global greenLightColour
    global yellowLightColour
    global blueLightColour
    global pengModeLifeStore
    
    pengRect = pygame.Rect(pengPos[0], pengPos[1], pengImage.get_width(), pengImage.get_height())
    
    if len(playerPattern) < len(pattern): # Check each item of the pattern
        if pygame.Rect.colliderect(pengRect, redBox1): # If the player touches a box
            redColour, redLightColour = redLightColour, redColour # change it into light mode
            colour_light('red_a')
            playerPattern.append(1) # Add the guess to the end of the player's guess' array
            peng_mode_check_wall_pos("topLeft")
            check_pattern(playerPattern) # Compare the guess with the answer
        elif pygame.Rect.colliderect(pengRect, redBox2):
            redColour, redLightColour = redLightColour, redColour
            colour_light('red_a')
            playerPattern.append(1)
            peng_mode_check_wall_pos("topLeft")
            check_pattern(playerPattern)
        elif pygame.Rect.colliderect(pengRect, greenBox1):
            greenColour, greenLightColour = greenLightColour, greenColour
            colour_light('green_e-lower')
            playerPattern.append(2)
            peng_mode_check_wall_pos("topRight")
            check_pattern(playerPattern)
        elif pygame.Rect.colliderect(pengRect, greenBox2):
            greenColour, greenLightColour = greenLightColour, greenColour
            colour_light('green_e-lower')
            playerPattern.append(2)
            peng_mode_check_wall_pos("topRight")
            check_pattern(playerPattern)
        elif pygame.Rect.colliderect(pengRect, yellowBox1):
            yellowColour, yellowLightColour = yellowLightColour, yellowColour
            colour_light('yellow_c-sharp')
            playerPattern.append(3)
            peng_mode_check_wall_pos("bottomLeft")
            check_pattern(playerPattern)
        elif pygame.Rect.colliderect(pengRect, yellowBox2):
            yellowColour, yellowLightColour = yellowLightColour, yellowColour
            colour_light('yellow_c-sharp')
            playerPattern.append(3)
            peng_mode_check_wall_pos("bottomLeft")
            check_pattern(playerPattern)
        elif pygame.Rect.colliderect(pengRect, blueBox1):
            blueColour, blueLightColour = blueLightColour, blueColour
            colour_light('blue_e-upper')
            playerPattern.append(4)
            peng_mode_check_wall_pos("bottomRight")
            check_pattern(playerPattern)
        elif pygame.Rect.colliderect(pengRect, blueBox2):
            blueColour, blueLightColour = blueLightColour, blueColour
            colour_light('blue_e-upper')
            playerPattern.append(4)
            peng_mode_check_wall_pos("bottomRight")
            check_pattern(playerPattern)
    
    pygame.display.update()
    if flagForRestart == True:
        if len(playerPattern) >= len(pattern):
            if pengModeLifeStore == life:
                pygame.time.set_timer(RETURN_NORMAL_EVENT, 1000, 1)
                playerPattern = []
                score = score + 1
                print(score)
            if pengModeLifeStore != life:
                pengModeLifeStore = life
                pygame.time.set_timer(RETURN_NORMAL_EVENT, 3000, 1)
                playerPattern = []

images = [bombScaled.convert_alpha(), cherryScaled.convert_alpha(), petrolScaled.convert_alpha()]

def peng_mode_game_loop():
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
    global boost
    global patternStarted
    global timerHasBeenSet
    global displayBoxColour
    global pengImage
    
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == COLOUR_LIGHT_EVENT:
            
            pygame.mixer.Channel(2).stop()
            redColour, redLightColour = ('#800000'), ('#FF0000')
            blueColour, blueLightColour = ('#001E80'), ('#003DFF')
            yellowColour, yellowLightColour = ('#778000'), ('#F0FF00')
            greenColour, greenLightColour = ('#008000'), ('#25FF00')
            displayBoxColour = GREY
            pengImage = lookingUpScaled
        if event.type == LIFE_LOSS_LIGHT_EVENT:
            redColour, redLightColour = ('#800000'), ('#FF0000')
            blueColour, blueLightColour = ('#001E80'), ('#003DFF')
            yellowColour, yellowLightColour = ('#778000'), ('#F0FF00')
            greenColour, greenLightColour = ('#008000'), ('#25FF00')
        if event.type == RETURN_NORMAL_EVENT:
            forcefieldActive = True
            forcefieldOpening = True
            forcefieldClosing = False
            canRandomPattern = True
            pengModeCanShowPattern = True
            canShowPattern = False
            patternStarted = False
        if event.type == CONTINUE_SHOWING_PATTERN_EVENT:
            print(pengPatternCounter)
            if pengPatternCounter < len(pattern):
                canRandomPattern = False
                pengModeCanShowPattern = True
                canShowPattern = True
                timerHasBeenSet = False
        if event.type == FINISH_SHOWING_PATTERN_EVENT:
            forcefieldClosing = True
            forcefieldActive = False
            forcefieldOpening = False
        if event.type == BOOST_EVENT: 
            boost = False
        if event.type == LIFE_LOSS_CONTINUE_EVENT:
            redColour, redLightColour = ('#FF0000'), ('#800000')
            blueColour, blueLightColour = ('#003DFF'), ('#001E80')
            yellowColour, yellowLightColour = ('#F0FF00'), ('#778000')
            greenColour, greenLightColour = ('#25FF00'), ('#008000')
            pygame.time.set_timer(LIFE_LOSS_LIGHT_EVENT, 500, 1)
    
    apply_gravity() # Apply gravitational force to the penguin's speed
    peng_mode_apply_key() # Check if the player presses any movement keys
    update_penguin_position() # Update the penguin's position
    peng_mode_check_pos() # Check the penguin's position and restrict it to inside the viewable area
    check_item_collision(all_items, pengRect) # check if the player touches any items
    check_item_lifetime(all_items) # remove any items that are onscreen for too long
    if pengModeCanShowPattern == True:
        forcefieldActive = True
        if canRandomPattern == True:
            random_pattern()
        if canShowPattern == True:
            show_pattern()
            playerPattern = []
        if canShowPattern == False and pengPatternCounter < len(pattern) and pengPatternCounter > 0 and timerHasBeenSet == False:
            pygame.time.set_timer(CONTINUE_SHOWING_PATTERN_EVENT, timeDelay+250, 1)
            timerHasBeenSet = True
    penguin_mode_store_player_guess()
    
    if imageCounter % 60 == 0:
        # Randomly choose the item type to spawn
        item_type = random.choice([1, 2, 3])
        if item_type == 1:
            spawn_peng_mode_items(all_items, images, item1_lifetime)
        elif item_type == 2:
            spawn_peng_mode_items(all_items, images, item2_lifetime)
        else:
            spawn_peng_mode_items(all_items, images, item3_lifetime)
        
        # spawn_peng_mode_items(all_items, images)
    
    pygame.display.update()

# Item lifetimes in milliseconds (change these values as needed)
item1_lifetime = 3000  # 3 seconds
item2_lifetime = 5000  # 5 seconds
item3_lifetime = 7000  # 7 seconds

def spawn_peng_mode_items(items, images, item_lifetime):
    image = random.choice(images)
    peng_spawn_area = emptyScaled.get_rect(topleft=(int(resizeScale * window_width)/2 - forcefieldSlide[forcefieldNum].get_width()/2, int(resizeScale * window_height)/2 - forcefieldSlide[forcefieldNum].get_height()/2 - int(resizeScale * 35)))
    if image == images[2] and life == 6:
        return
    else:
        while True:
            item = image.get_rect(center=(random.randint(int((offsetX + 50) * resizeScale), int((offsetX + 550 - 50) * resizeScale)), random.randint(int((offsetY + 50) * resizeScale), int((offsetY + 550 - 50) * resizeScale))))
            if not item.colliderect(peng_spawn_area):  # Check if the item overlaps with the safety net
                break
        item_timer = pygame.time.get_ticks() + item_lifetime
        items.append((item, image, item_timer))


def check_item_collision(items, character_rect):
    global score
    global life
    for item in items[:]:
        if item[0].colliderect(character_rect):
            if item[1] == images[0]:
                # play boom sound
                score = score - 3
                life = life - 1
                if life == 0:
                    render_save_score_screen()
            elif item[1] == images[1]:
                score = score + 2
            elif item[1] == images[2]:
                life = life + 1
            items.remove(item)


def check_item_lifetime(items):
    current_time = pygame.time.get_ticks()
    for item in items[:]:
        _, _, item_timer = item
        if current_time >= item_timer:
            items.remove(item)


render_game_start_page()