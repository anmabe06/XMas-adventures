import pygame
from User_character import Character
from Obstacles import Top_obstacle, Bottom_obstacle, Coin

pygame.init()

pygame.display.set_caption("XMAS ADVENTURES")
screen_width, screen_height = 1100, 700
screen = pygame.display.set_mode((screen_width, screen_height))

user = Character("anmabe", "melchor")

user_character = user_image = pygame.image.load(user.character_image)
player = pygame.Rect(user.x, user.y, user.width, user.height)
background_image = pygame.image.load('assets/images/background.jpg')

run = True
clock = pygame.time.Clock()

fps = 60
speed = 5
gravity = 5

def move():
    dummie = pygame.key.get_pressed()
    if dummie[pygame.K_UP] and user.y - speed > 0:  # Left
        user.y -= speed
    elif user.y + gravity <= screen_height - user.height:
        user.y += gravity
    

def load_window():
    screen.blit(background_image, (0,0))
    screen.blit(user_character, (user.x, user.y))
    pygame.display.update()

while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    move()
    load_window()

    # Aquí es donde programaremos lo que debe ocurrir en cada frame

# Tras salir del bucle, cerramos el juego y acabamos el programa
pygame.quit()