from global_variables import *
import pygame
from User_character import Character
from Obstacles import Helicopter, Building, Present
import time
import random

#T_ODO: Change player jump
#T_ODO: Add score and lifes text
#TODO: Add hitboxes to obstacles
#TODO: Make presents' code
#TODO: Add background music
#TODO: Add hop sound effect on movement
#TODO: Make respawn animation
#TODO: Make helicopter animation
#TODO: Add lost screen to quit game or redirect to main menu
#TODO: Main menu:
#       - Game name
#       - Background animation
#       - Change character (selector)
#       - Set name

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
    if user.y >= screen_height-user.height:
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

    #sentinel_helicopter=obstacles_in_scene[0]
    #sentinel_present=obstacles_in_scene[1] if showPresent
    #sentinel_building=obstacles_in_scene[2]

    #sentinel_helicopter = str(sentinel_helicopter)
    #sentinel_present = str(sentinel_present)
    #sentinel_building = str(sentinel_building)

    obstacles_in_scene[0].append(Helicopter(helicopter_height))
    obstacles_in_scene[2].append(Building(building_height))


def move():
    global sentinelSpeed

    dummie = pygame.key.get_pressed()
    if dummie[pygame.K_UP] and user.jumping_animation_duration_timer == 0:
        user.y -= user.jump_speed
        user.jumping_animation_duration_timer = user.jumping_animation_duration
        #sentinelSpeed = user.speed
    
    elif user.jumping_animation_duration_timer > 0:
        
        if user.jumping_animation_duration_timer >= user.jumping_animation_duration_halved:
            user.y -= user.speed / fps / 4*3
        else:
            #Code to make a slow fall animation
            user.y += user.speed / fps / 4
            pass
        
        user.jumping_animation_duration_timer -= 1
    
    else:
        user.y += gravity


def move_scene():
    #Move obstacles
    if len(obstacles_in_scene[0]) > 0:
        for helicopter in obstacles_in_scene[0]:
            helicopter.x -= obstacle_speed
    
    if len(obstacles_in_scene[1]) > 0:
        for present in obstacles_in_scene[1]:
            #screen.blit(present, (present.x, present.y))
            pass
    
    if len(obstacles_in_scene[2]) > 0:
        for building in obstacles_in_scene[2]:
            building.x -= obstacle_speed


def load_window():
    screen.blit(background_image, (0,0))
    screen.blit(user_character, (user.x, user.y))
    screen.blit(lifes_font, (screen_width - 200, 20))
    screen.blit(score_font, (screen_width - 200, 90))
    
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
    global lifes_font, score_font
    #time.sleep(2)

    while not isTerminal():
        clock.tick(fps)
        lifes_font = font.render(f'Lifes: {user.lifes}', True, (255,255,255))
        score_font = font.render(f'Score: {user.score}', True, (255,255,255))
        
        if current_obstacle_frame_separation == obstacle_frame_separation:
            create_obstacles()
            current_obstacle_frame_separation = 0
        
        current_obstacle_frame_separation += 1
        move()
        move_scene()
        islifelost_var = islifeLost()
        load_window()
        
        if islifelost_var and user.lifes != 0:
            time.sleep(1)

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None, 50)

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