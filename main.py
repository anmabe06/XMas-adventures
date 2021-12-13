from pygame import image
from global_variables import *
import pygame
from User_character import Character
from Obstacles import Helicopter, Building, Present
import time
import random

#T_ODO: Change player jump
#T_ODO: Add score and lifes text
#T_ODO: Add hitboxes to obstacles
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


def isQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


def isDeadFromCollision():
    sentinel = False
    if len(obstacles_in_scene[0]) > 0:
        for helicopter in obstacles_in_scene[0]:
            # print("Helicopter: ", helicopter.rect.x, helicopter.rect.y, " | User: ", user.rect.x, user.rect.y)
            if user.rect.colliderect(helicopter.rect):
                sentinel = True
    
    if len(obstacles_in_scene[2]) > 0:
        for building in obstacles_in_scene[2]:
            #print("Building: ", building.rect.x, building.rect.y, " | User: ", user.rect.x, user.rect.y)
            if user.rect.colliderect(building.rect):
                sentinel = True
    
    if user.hasColided == True and sentinel == True:
        pass
    elif user.hasColided == True and sentinel == False:
        user.hasColided = False
        return sentinel
    elif user.hasColided == False and sentinel == True:
        user.hasColided = True
        return sentinel


def hasObtainedPoints():
    if len(obstacles_in_scene[1]) > 0:
        for present in obstacles_in_scene[1]:
            if user.rect.colliderect(present.rect):
                user.score += 1
                present.showImage = False
    
    return True


def isDeadFromFloorBang():
    if user.y >= screen_height-user.height:
        return True
    
    return False


def islifeLost():
    global lifeLost_value
    isDeadFromFloorBang_value = isDeadFromFloorBang()
    isDeadFromCollision_value = isDeadFromCollision()
    
    if isDeadFromFloorBang_value:
        if user.lifes > 0:
            user.respawnAnimation
            user.lifes -= 1
            lifeLost_value = True
            #TO REMOVE AFTER ANIMATION COMPLETED
            time.sleep(1)
            user.x, user.y = user.initial_x, user.initial_y
            user.rect.x, user.rect.y = user.initial_x, user.initial_y
            #######
        print("isDeadFromFloorBang")

    elif isDeadFromCollision_value:
        user.lifes -= 1
        lifeLost_value = True
        user.blinkAnimation
        print("isDeadFromCollision")

    return isDeadFromFloorBang_value and isDeadFromCollision_value


def create_obstacles():
    helicopter_height = str(random.randint(0,3))
    building_height = str(random.randint(0,3))
    showPresent = True if random.randint(0,10) == 3 else False

    if helicopter_height == "3" and building_height == "3":
        if random.randint(0,1) == 0:
            helicopter_height = "1"
        else:
            building_height = "1"

    elif helicopter_height == "3" and building_height == "2":
        building_height = "1"

    elif helicopter_height == "2" and building_height == "3":
        helicopter_height = "1"

    present_y_position = (heightConverter[helicopter_height] + (screen_height - heightConverter[building_height])) / 2 - 100

    #sentinel_helicopter=obstacles_in_scene[0]
    #sentinel_present=obstacles_in_scene[1] if showPresent
    #sentinel_building=obstacles_in_scene[2]

    #sentinel_helicopter = str(sentinel_helicopter)
    #sentinel_present = str(sentinel_present)
    #sentinel_building = str(sentinel_building)

    obstacles_in_scene[0].append(Helicopter(helicopter_height, pygame.Rect(screen_width, 0, 100, heightConverter[helicopter_height])))
    obstacles_in_scene[2].append(Building(building_height, pygame.Rect(screen_width, screen_height - heightConverter[building_height], 100, heightConverter[building_height])))
    #if showPresent:
    obstacles_in_scene[1].append(Present(present_y_position, pygame.Rect(screen_width, present_y_position,  100, 100)))


def move():
    global sentinelSpeed

    dummie = pygame.key.get_pressed()
    if dummie[pygame.K_UP] and user.jumping_animation_duration_timer == 0:
        user.y -= user.jump_speed
        user.rect.y -= user.jump_speed
        if user.y < 10:
            user.y = 10
            user.rect.y = 10
        user.jumping_animation_duration_timer = user.jumping_animation_duration
        #sentinelSpeed = user.speed
    
    elif user.jumping_animation_duration_timer > 0:
        
        if user.jumping_animation_duration_timer >= user.jumping_animation_duration_halved:
            user.y -= user.speed / fps / 4*3
            user.rect.y -= user.speed / fps / 4*3
            if user.y < 10:
                user.y = 10
                user.rect.y = 10
        else:
            #Code to make a slow fall animation
            user.y += user.speed / fps / 4
            user.rect.y = user.speed / fps / 4
            pass
        
        user.jumping_animation_duration_timer -= 1
    
    else:
        user.y += gravity
        user.rect.y += gravity

    user.rect.y = user.y
    #print(user.rect.y, user.y)


def move_scene():
    #Move obstacles
    if len(obstacles_in_scene[0]) > 0:
        for helicopter in obstacles_in_scene[0]:
            helicopter.rect.x -= obstacle_speed
            helicopter.x -= obstacle_speed
    
    if len(obstacles_in_scene[1]) > 0:
        for present in obstacles_in_scene[1]:
            present.rect.x -= obstacle_speed
            present.x -= obstacle_speed
    
    if len(obstacles_in_scene[2]) > 0:
        for building in obstacles_in_scene[2]:
            building.rect.x -= obstacle_speed
            building.x -= obstacle_speed


def load_window():
    global lifeLost_value
    screen.blit(background_image, (0,0))
    screen.blit(user_character, (user.x, user.y))
    screen.blit(lifes_font, (screen_width - 200, 20))
    screen.blit(score_font, (screen_width - 200, 90))
    if lifeLost_value:
        screen.blit(pygame.image.load("assets/images/end_screen.png"), (0,0))
        lifeLost_value = False
    #screen.blit(pygame.image.load("assets/images/end_screen.png"), (0,0))
    
    if len(obstacles_in_scene[0]) > 0:
        for helicopter in obstacles_in_scene[0]:
            screen.blit(helicopter.helicopter_obstacle, (helicopter.x, helicopter.y))
    
    if len(obstacles_in_scene[1]) > 0:
        for present in obstacles_in_scene[1]:
            if present.showImage:
                screen.blit(present.present_obstacle, (present.x, present.y))
    
    if len(obstacles_in_scene[2]) > 0:
        for building in obstacles_in_scene[2]:
            screen.blit(building.building_obstacle, (building.x, building.y))

    pygame.display.update()


def showEndScreen():
    lifes_font = font.render('Lifes: 0', True, (255,255,255))
    screen.blit(lifes_font, (screen_width - 200, 20))
    screen.blit(pygame.image.load("assets/images/end_screen.png"), (0,0))
    screen.blit(game_over_font, (screen_width/2-400,screen_height/2-100))
    
    pygame.display.update()
    while True:
        isQuit()


def game():
    global current_obstacle_frame_separation
    global obstacle_frame_separation
    global lifes_font, score_font
    #time.sleep(2)

    while user.lifes > 0:
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
        hasObtainedPoints()
        
        if islifelost_var and user.lifes != 0:
            time.sleep(1)

        isQuit()
    
    showEndScreen()


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None, 50)
    font2 = pygame.font.SysFont(None, 200)
    game_over_font = font2.render('GAME OVER', True, (255,0,0))

    #Window adjustments
    pygame.display.set_caption("XMAS ADVENTURES")
    screen = pygame.display.set_mode((screen_width, screen_height))

    #Set scene
    user = Character("anmabe", "melchor")
    user.rect = pygame.Rect(user.x, user.y, user.width, user.height)
    user_character = pygame.image.load(user.character_image)
    background_image = pygame.image.load('assets/images/background.jpg')

    clock = pygame.time.Clock()

    #Background music
    #pygame.mixer.music.load('foo.mp3')
    #pygame.mixer.music.play(-1)

    game()