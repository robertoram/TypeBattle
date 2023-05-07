import pygame
from game.config import *
from game.scenes import *
from game.scenes.menu_scene import MenuScene
from game.scenes.game_scene import GameScene
from game.scenes.game_over_scene import GameOverScene
# Inicialización de Pygame
pygame.init()

# Configuración de la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Creación de las escenas
menu_scene = MenuScene(screen)
game_scene = GameScene(screen)
game_over_scene = GameOverScene(screen)

# Configuración de la escena actual
current_scene = menu_scene

# Bucle principal del juego
while True:
    # Manejo de eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == QUIT_EVENT:
            pygame.quit()
            quit()
        elif event.type == TITLE_EVENT:
            # Handle title event
            pass


    # Actualización de la escena actual
    current_scene.update()

    # Cambio de escena si es necesario
    if current_scene.done:
        if current_scene.next_scene == "game":
            current_scene = game_scene
        elif current_scene.next_scene == "game_over":
            current_scene = game_over_scene
        else:
            break

    # Dibujado de la escena actual
    current_scene.draw()

    # Actualización de la pantalla
    pygame.display.update()

# Cierre de Pygame
pygame.quit()