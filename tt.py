
# from pygame.locals import *
# # # print(K_UP)

# # try:
# #     tt = int(input())
# #     print(tt)
# #     tts = chr(tt)
# #     print(tts)
# # except ValueError:
# #     if tt == 1073741906 or tt == 11:#...
# #         print("up arrow")
# #         #the text = Up Arrow
# #     pass


# settingsDict = {
#     "up": K_UP,
#     "down": K_b,
#     "left": K_c,
#     "right": K_d,
#     "boost": K_UP
# }
# print(settingsDict["boost"])
# y = str(chr(settingsDict["boost"]))
# print("\n")

import pygame
import random
import os

pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

def spawn_random_item(items, images):
    image = random.choice(images)
    item = image.get_rect(center=(random.randint(100, 700), random.randint(100, 500)))
    items.append((item, image))

def check_collision(items, character_rect):
    for item in items[:]:
        if item[0].colliderect(character_rect):
            items.remove(item)

all_items = []
images = [pygame.image.load("./Assets/penguin_mode/bomb.png").convert_alpha(),
          pygame.image.load("./Assets/penguin_mode/cherry.png").convert_alpha(),
          pygame.image.load("./Assets/penguin_mode/petrol.png").convert_alpha()]

spawn_delay = 1  # Milliseconds between spawns
last_spawn_time = pygame.time.get_ticks()

# Player character
character_width, character_height = 50, 50
character_rect = pygame.Rect(screen_width // 2, screen_height // 2, character_width, character_height)

while True:
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time >= spawn_delay:
        spawn_random_item(all_items, images)
        last_spawn_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        character_rect.x += 5
    if keys[pygame.K_UP]:
        character_rect.y -= 5
    if keys[pygame.K_DOWN]:
        character_rect.y += 5

    check_collision(all_items, character_rect)


    # Other game logic and drawing code here
    screen.fill((255, 255, 255))  # Fill the screen with white

    # Draw the player character
    pygame.draw.rect(screen, (0, 0, 255), character_rect)

    for item, image in all_items:
        screen.blit(image, item)

    pygame.display.flip()
    clock.tick(60)
