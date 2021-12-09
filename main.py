from global_variables import *
import pygame
from User_character import Character
from Obstacles import Helicopter, Building, Present
import time
import random

#TODO: Make obtacle logic
#TODO: Make background music track

def isTerminal():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    
    if user.lifes <= 0:
        return True
    
    return False


def islifeLost():
    #Colision with object
    #Colision with floor or ceeling
    if user.y < 13.0 or user.y == screen_height-user.height:
        user.lifes -= 1
        if user.lifes == 0:
            return True
        time.sleep(1)
        user.x, user.y = user.initial_x, user.initial_y
        return True
    
    return False


def create_obstacles():
    helicopter_height = str(random.randint(0,3))
    building_height = str(random.randint(0,3))
    #showPresent = True if random.randint(0,5) == 3 else False

    if helicopter_height == "3" and building_height == "3":
        if random.randint(0,1) == 0:
            helicopter_height = "2"
        else:
            building_height = "2"

    sentinel_helicopter=obstacles_in_scene[0]
    #sentinel_present=obstacles_in_scene[1] if showPresent
    sentinel_building=obstacles_in_scene[2]

    sentinel_helicopter = str(sentinel_helicopter)
    #sentinel_present = str(sentinel_present)
    sentinel_building = str(sentinel_building)

    obstacles_in_scene[0].append(Helicopter(helicopter_height))
    obstacles_in_scene[1].append(Building(helicopter_height))


        

def move():
    dummie = pygame.key.get_pressed()
    if dummie[pygame.K_UP] and user.y - speed*2 > 0:
        user.y -= speed * 2
    elif user.y + speed <= screen_height - user.height:
        if user.y > 13.0 or not dummie[pygame.K_UP]:
            user.y += speed


def move_scene():
    #Move obstacles
    if len(obstacles_in_scene[0]) > 0:
        for helicopter in obstacles_in_scene[0]:
            helicopter.x += obstacle_speed
    
    if len(obstacles_in_scene[1]) > 0:
        for present in obstacles_in_scene[1]:
            #screen.blit(present, (present.x, present.y))
            pass
    
    if len(obstacles_in_scene[2]) > 0:
        for building in obstacles_in_scene[2]:
            building.x += obstacle_speed


def load_window():
    screen.blit(background_image, (0,0))
    screen.blit(user_character, (user.x, user.y))
    
    if len(obstacles_in_scene[0]) > 0:
        for helicopter in obstacles_in_scene[0]:
            screen.blit(helicopter.helicopter_obstacle, (helicopter.x, helicopter.y))
    
    if len(obstacles_in_scene[1]) > 0:
        for present in obstacles_in_scene[1]:
            #screen.blit(present, (present.x, present.y))
            pass
    
    if len(obstacles_in_scene[2]) > 0:
        for building in obstacles_in_scene[2]:
            screen.blit(building.building_obstacle, (building.x, building.y))

    pygame.display.update()


def game():
    global current_obstacle_frame_separation
    global obstacle_frame_separation
    #time.sleep(2)
    while not isTerminal():
        clock.tick(fps)
        
        if current_obstacle_frame_separation == obstacle_frame_separation:
            create_obstacles()
            current_obstacle_frame_separation = 0
        
        current_obstacle_frame_separation += 1
        move()
        #move_scene()
        islifelost_var = islifeLost()
        load_window()
        
        if islifelost_var and user.lifes != 0:
            time.sleep(1)
        
        print(len(obstacles_in_scene))

    pygame.quit()


if __name__ == "__main__":
    pygame.init()

    #Window adjustments
    pygame.display.set_caption("XMAS ADVENTURES")
    screen = pygame.display.set_mode((screen_width, screen_height))

    #Set scene
    user = Character("anmabe", "melchor")
    user_character = pygame.image.load(user.character_image)
    player = pygame.Rect(user.x, user.y, user.width, user.height)
    background_image = pygame.image.load('assets/images/background.jpg')

    clock = pygame.time.Clock()

    #Background music
    #pygame.mixer.music.load('foo.mp3')
    #pygame.mixer.music.play(-1)

    game()