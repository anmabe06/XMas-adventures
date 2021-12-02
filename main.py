import pygame
from user_character import Character
from obstacles import Top_obstacle, Bottom_obstacle, Coin

pygame.init()

pygame.display.set_caption("XMAS ADVENTURES")
screen_width, screen_height = 1100, 700
screen = pygame.display.set_mode((screen_width, screen_height))

user = Character()

#user_image = pygame.image.load(user.image)
user_image = pygame.image.load('assets/images/gaspar.png')
background_image = pygame.image.load('assets/images/background.jpg')

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #Screen assets
    screen.fill((155,155,155))
    #screen.blit(user_image, (0, screen_height - user.height))
    screen.blit(background_image, (0,0))
    screen.blit(user_image, (0, 550))
    pygame.display.update()

    # Aquí es donde programaremos lo que debe ocurrir en cada frame

# Tras salir del bucle, cerramos el juego y acabamos el programa
pygame.quit()