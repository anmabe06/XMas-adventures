import pygame
from User_character import Character
from Obstacles import Helicopter, Building, Present
import random

#TODO: Make obtacle logic
#TODO: Change assets
#TODO: Make background music track

def isTerminal():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    #Colision
    return False


def create_obstacles():
    global obstacles_in_scene

        

def move():
    dummie = pygame.key.get_pressed()
    if dummie[pygame.K_UP] and user.y - speed*2 > 0:
        user.y -= speed * 2
    elif user.y + speed <= screen_height - user.height:
        if user.y > 13.0 or not dummie[pygame.K_UP]:
            user.y += speed


def load_window():
    screen.blit(background_image, (0,0))
    screen.blit(user_character, (user.x, user.y))
    pygame.display.update()


def game():
    while not isTerminal():
        clock.tick(fps)
        create_obstacles()
        move()
        load_window()

    pygame.quit()


if __name__ == "__main__":
    pygame.init()

    #Window adjustments
    pygame.display.set_caption("XMAS ADVENTURES")
    screen_width, screen_height = 1100, 700
    screen = pygame.display.set_mode((screen_width, screen_height))

    #Set scene
    user = Character("anmabe", "melchor")
    user_character = user_image = pygame.image.load(user.character_image)
    player = pygame.Rect(user.x, user.y, user.width, user.height)
    background_image = pygame.image.load('assets/images/background.jpg')

    clock = pygame.time.Clock()

    #Background music
    #pygame.mixer.music.load('foo.mp3')
    #pygame.mixer.music.play(-1)

    fps = 60
    speed = 5
    starting_obstacle_separation = 600
    obstacles_in_scene = []

    game()