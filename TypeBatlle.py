import pygame
import random

# Inicializar Pygame
pygame.init()

# Variables
attacked_word = ''

# Configuración de la ventana
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("ZType")

# Configuración de la fuente
font = pygame.font.SysFont("monospace", 36)

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Lista de palabras
word_list = ['apple', 'banana', 'orange', 'kiwi', 'watermelon', 'mango', 'pear', 'pineapple']

words = []
for i in range(1):
    word = ""
    for word in word_list:
        words.append({"text": word, "x": random.randint(0, window_width-200), "y": random.randint(-500, 0)})

# Configuración del reloj
clock = pygame.time.Clock()

# Función para dibujar la pantalla
def draw_screen():
    window.fill(black)
    for word in words:
        text = font.render(word["text"], True, white)
        window.blit(text, (word["x"], word["y"]))

# Bucle principal
while True:
    # Comprobar si el jugador ha cerrado la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Dibujar la pantalla
    draw_screen()
    
    # Mover las palabras hacia abajo
    for word in words:
        word["y"] += 1

    # Comprobar si el jugador ha presionado una tecla
    keys = pygame.key.get_pressed()

   
    for word in words:
        if (len(attacked_word) > 0 and word["text"] == attacked_word) or len(attacked_word) == 0:
            if keys[ord(word["text"][0])] and len(word["text"]) > 0 :
                if len(word["text"]) > 1:
                    word["text"] = word["text"][1:]
                    attacked_word =  word["text"]
                else:
                    words.remove(word)
                    attacked_word =  ''
                
            

        

    # Actualizar la pantalla
    pygame.display.update()

    # Configuración del reloj
    clock.tick(60)
