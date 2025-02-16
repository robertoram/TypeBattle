import pygame
import random

# Inicializar Pygame
pygame.init()

# Variables
attacked_word_id = 0
attacked_word = None
score = 0
id = 0
missed_words_allowed = 3
missed_words_count = 0
words_onscreen_count = 3


# Configuración de la ventana
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("TypeBattle - by David Ramírez")

# Configuración de la fuente
font = pygame.font.SysFont("monospace", 36)

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
Red = (255, 0, 0)

# Función para generar una posición aleatoria que no esté en colisión con las palabras existentes
def generate_random_position(words):
    while True:
        # Generar una posición aleatoria
        x = random.randint(100, window_width - 100)
        y = random.randint(-500, 0)
        rect = pygame.Rect(x, y, 100, 100)
        
        # Comprobar si hay colisión con alguna palabra existente
        collision = False
        word_count = words_onscreen_count if len(words) >= words_onscreen_count else len(words)
        for w in range(word_count):
            wordcollission = words[w]
            #for wordcollission in words:
            if wordcollission["rect"] != None:
                if rect.colliderect(wordcollission["rect"]):
                    collision = True
                    break
        
        # Si no hay colisión, devolver la posición
        if not collision:
            return x, y

# Lista de palabras
#word_list = ['opalo', 'original', 'orange', 'kiwi', 'watermelon', 'mango', 'pear', 'pineapple']
word_list = ['algoritmo', 'biblioteca', 'computadora', 'depuración', 'estructura', 'función', 'hardware', 'interfaz', 'java', 'kernel', 'lenguaje', 'memoria', 'navegador', 'objeto', 'programa', 'query', 'repositorio', 'sintaxis', 'tecnología', 'usuario', 'variable', 'web', 'XML', 'yield', 'zip', 'aplicación', 'bit', 'código', 'debug', 'ensamblador', 'fragmento', 'GNU', 'hardware', 'internet', 'JavaScript', 'kernel', 'lenguaje', 'multitarea', 'núcleo', 'optimización', 'procesador', 'query', 'red', 'servidor', 'teclado', 'unicode', 'vector', 'whitespace', 'XHTML']

words = []

word = ""
for word in word_list:
    id += 1
    # pos = generate_random_position(words)
    # word_surface  = font.render(word, True, white)
    # word_rect = word_surface.get_rect()
    # word_rect.topleft = (pos[0], pos[1])
    words.append({"id": id,"atacked": 0, "text": word, "x": 0, "y": 0, "surface": None, "rect": None })
   

# Configuración del reloj
clock = pygame.time.Clock()

# Función para dibujar la pantalla
def draw_screen():
    window.fill(black)
    word_count = words_onscreen_count if len(words) >= words_onscreen_count else len(words)
    for w in range(word_count):
        if words[w]["rect"] == None:
            pos = generate_random_position(words)
            word_surface  = font.render(words[w]["text"], True, white)
            word_rect = word_surface.get_rect()
            word_rect.topleft = (pos[0], pos[1])
            words[w]["x"] = pos[0]
            words[w]["y"] = pos[1]
            words[w]["surgace"] = word_surface
            words[w]["rect"] = word_rect
        word =  words[w]
        text = font.render(word["text"], True, white if word["atacked"] == 0 else Red)
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
    #for word in words:
    word_count = words_onscreen_count if len(words) >= words_onscreen_count else len(words)
    for w in range(word_count):
        word = words[w]
        word["y"] += 1
        if word["y"] == window_width-200:
            missed_words_count += 1
            attacked_word_id = 0
            attacked_word = None
            words.remove(word)

    # Comprobar si el jugador ha superado las palabras perdidas permitidas

    if missed_words_count >= missed_words_allowed:
        textScore = font.render('You Lose!', True, Red)
        window.blit(textScore, (int((window_width  - textScore.get_width()) / 2),10))

    # Comprobar si el jugador ha presionado una tecla
    keys = pygame.key.get_pressed()

   
    for word in words:
        if (attacked_word_id > 0 and word["id"] == attacked_word_id) or attacked_word_id == 0:
            if keys[ord(word["text"][0])] and len(word["text"]) > 0:
                if len(word["text"]) > 1:
                    word["text"] = word["text"][1:]
                    attacked_word_id=  word["id"]
                    word["atacked"] = 1
                else:
                    words.remove(word)
                    attacked_word_id = 0
                    attacked_word = None
                    score += 10
                    break
         
    # Mostrar palabras por destruir
    textScore = font.render('Enemigos: ' + words.__len__().__str__(), True, white)
    window.blit(textScore, (int(window_width  - textScore.get_width()),1))

    # Imprimir el Score en pantalla
    textScore = font.render('Score: ' + score.__str__(), True, white)
    window.blit(textScore, (1, 1))

    # Imprimir las palabras falladas
    textMissed = font.render('Missed: ' + missed_words_count.__str__(), True, white)
    window.blit(textMissed, (1, 30))
        

    # Actualizar la pantalla
    pygame.display.update()

    # Configuración del reloj
    clock.tick(60)
