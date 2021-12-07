# INICIO: importamos pygame y lo activamos
import pygame
pygame.init()


# ------------CONSTANTES------------
# Creamos la ventana
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship!")

# Cargamos las imágenes que vamos a usar y las ajustamos 
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
SPACESHIP_IMAGE = pygame.image.load('assets/images/melchor.png')
SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
SPACE = pygame.transform.scale(pygame.image.load(
    'assets/images/background.jpg'), (WIDTH, HEIGHT))

# Otras constantes que nos conviene tener almacenadas
FPS = 60
VEL = 5
INITIAL_X, INITIAL_Y = WIDTH//2, HEIGHT//2


# ------------FUNCIONES------------
# Función para mover la nave sin que salga de la pantalla
def handle_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x - VEL > 0:  # Left
        player.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and player.x + VEL + player.width < WIDTH:  # Right
        player.x += VEL
    if keys_pressed[pygame.K_UP] and player.y - VEL > 0:  # Up
        player.y -= VEL
    if keys_pressed[pygame.K_DOWN] and player.y + VEL + player.height < HEIGHT:  # Down
        player.y += VEL

# Función para dibujar todos nuestros elementos en la pantalla
def draw_window(player):
    WIN.blit(SPACE, (0,0)) # Primero el fondo para que todo lo demás vaya encima
    WIN.blit(SPACESHIP, (player.x, player.y)) # Después dibujamos nuesta nave 
    pygame.display.update() # Finalmente actualizamos la pantalla


# ------------BUCLE PRINCIPAL------------
run = True
clock = pygame.time.Clock()
player = pygame.Rect(INITIAL_X, INITIAL_Y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

while run:
    clock.tick(FPS) # esperamos al tick para no ir más rápido que los FPS establecidos

    for event in pygame.event.get():
        # recorremos todos los eventos, en este caso solo nos interesa el evento de cerrar ventana
        if event.type == pygame.QUIT:
            run = False
    
    keys_pressed = pygame.key.get_pressed()
    handle_movement(keys_pressed, player) # Actualizamos la posición en función de las teclas presionadas
    draw_window(player) # Dibujamos nuestros elementos en la pantalla


# FIN: desactivamos pygame
pygame.quit()

    