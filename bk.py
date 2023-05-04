import sys
import pygame
import random

# Inicializar pygame
pygame.init()

# Definir el tamaño de la ventana
window_width = 800
window_height = 600

# Crear la ventana
screen = pygame.display.set_mode((window_width, window_height))

# Cargar la imagen del jugador
player_image = pygame.image.load("player.png")

# Definir la posición inicial del jugador
player_x = 400
player_y = 500


# Lista de palabras enemigas
enemy_words = ["asteroid", "comet", "meteor", "rocket", "spaceship", "alien", "planet", "nebula"]

# Definir la fuente y el tamaño del texto
font = pygame.font.Font(None, 36)

# Variables para la posición del jugador
player_x = window_width // 2
player_y = window_height - 100

# Variable para el tiempo de espera entre la aparición de palabras enemigas
enemy_delay = 0
enemy_y = 0
enemy_text = font.render("", True, (255, 255, 255))
enemy_x = 0
enemy_y = 0
enemy_speed = 0
score=0
# Bucle principal del juego
while True:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 5
            elif event.key == pygame.K_RIGHT:
                player_x += 5
    


    # Llenar la pantalla con un color sólido (negro)
    screen.fill((0, 0, 0))

    # Dibujar la imagen del jugador en la pantalla
    screen.blit(player_image, (player_x, player_y))

    # Actualizar el tiempo de espera entre la aparición de palabras enemigas
    enemy_delay -= 1

    # Si el tiempo de espera ha terminado, elegir una nueva palabra enemiga y reiniciar el tiempo de espera
    if enemy_delay <= 0 and enemy_y >= window_height-100:
        enemy_word = random.choice(enemy_words)
        enemy_text = font.render(enemy_word, True, (255, 255, 255))
        enemy_x = random.randint(0, window_width - enemy_text.get_width())
        enemy_y = 0
        enemy_delay = 500 # tiempo de espera en número de iteraciones del bucle principal

    # Dibujar la palabra enemiga en la pantalla
    screen.blit(enemy_text, (enemy_x, enemy_y))

    # Actualizar la posición vertical de la palabra enemiga
    enemy_speed -= 1
    if enemy_speed <= 0:
        enemy_y += 1
        enemy_speed = 10

    # Actualizar la pantalla
    pygame.display.flip()
