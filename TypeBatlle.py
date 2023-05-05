import pygame
import random

# Inicializar Pygame
pygame.init()

# Variables
global attacked_word_id
attacked_word_id = 0
attacked_word = None
global score 
score = 0
id = 0
missed_words_allowed = 3
missed_words_count = 0
global words_onscreen_count
words_onscreen_count = 1
word_spawn_delay = 120 #Ticks
global clock_tick_count
clock_tick_count = 0

# Configuración de la ventana
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("TypeBattle - by David Ramírez")

# Configuración de la fuentes
font = pygame.font.SysFont("monospace", 36)
font_stats = pygame.font.SysFont("monospace", 14)

# Configuración de fondo de pantalla
fondo = pygame.transform.scale(pygame.image.load("resources/images/background.jpg"), (window_width, window_height))

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
Red = (255, 0, 0)

# Lista de palabras
#word_list = ['opalo', 'original', 'orange', 'oiwi', 'oatermelon', 'oango', 'oear', 'oineapple']
word_list = ['algoritmo', 'biblioteca', 'computadora', 'depuración', 'estructura', 'función', 'hardware', 'interfaz', 'java', 'kernel', 'lenguaje', 'memoria', 'navegador', 'objeto', 'programa', 'query', 'repositorio', 'sintaxis', 'tecnología', 'usuario', 'variable', 'web', 'XML', 'yield', 'zip', 'aplicación', 'bit', 'código', 'debug', 'ensamblador', 'fragmento', 'GNU', 'hardware', 'internet', 'JavaScript', 'kernel', 'lenguaje', 'multitarea', 'núcleo', 'optimización', 'procesador', 'query', 'red', 'servidor', 'teclado', 'unicode', 'vector', 'whitespace', 'XHTML']

words = []

word = ""
for word in word_list:
    id += 1
    words.append({"id": id,"atacked": 0, "text": word, "x": 0, "y": 0, "surface": None, "rect": None })
   

# Configuración del reloj
clock = pygame.time.Clock()

# Función para generar una posición aleatoria que no esté en colisión con las palabras existentes
def generate_random_position(text):
    while True:
        word_surface  = font.render(text, True, white)
        word_rect = word_surface.get_rect()

        # Generar una posición aleatoria
        x = random.randint(10, window_width - word_rect.width - 10)
        y = -30
        return x, y

# Función para calcular las posiciones en pantalla
def calculate_positions():
    for word in words:
        pos = generate_random_position(word["text"])
        word_surface  = font.render(word["text"], True, white)
        word_rect = word_surface.get_rect()
        word_rect.topleft = (pos[0], pos[1])
        word["x"] = pos[0]
        word["y"] = pos[1]
        word["surface"] = word_surface
        word["rect"] = word_rect

# Función para dibujar la pantalla
def draw_screen():
    window.blit(fondo,(0,0))
    for w in range(words_onscreen_count):
        wordnumber = w
        text = font.render(words[wordnumber]["text"], True, white if words[wordnumber]["atacked"] == 0 else Red)
        window.blit(text, (words[wordnumber]["x"], words[wordnumber]["y"]))

# Función para comprobar la tecla presionada
def key_pressed_check(key):
    global attacked_word_id
    global score
    for word in words:
        if ((attacked_word_id > 0 and word["id"] == attacked_word_id) or attacked_word_id == 0) and len(word["text"]) > 0:
            if key == ord(word["text"][0]) and len(word["text"]) > 0:
                if len(word["text"]) >= 1:
                    word["text"] = word["text"][1:]
                    attacked_word_id=  word["id"]
                    word["atacked"] = 1
                if  len(word["text"]) == 0:
                    words.remove(word)
                    attacked_word_id = 0
                    score += 10
                    check_onscreen_words()
                    break


# Función para Comprobar si el jugador ha superado las palabras perdidas permitidas
def check_missed_words():
    if missed_words_count >= missed_words_allowed:
        textScore = font.render('You Lose!', True, Red)
        window.blit(textScore, (int((window_width  - textScore.get_width()) / 2),10))

# Función para ingrementar las palabras en pantalla
def check_onscreen_words():
    global clock_tick_count
    global words_onscreen_count
    if clock_tick_count == word_spawn_delay and words_onscreen_count < len(words):
        words_onscreen_count += 1
        clock_tick_count = 0
    if words_onscreen_count > len(words):
        words_onscreen_count = len(words)

calculate_positions()

# Bucle principal
while True:
    # Comprobar si el jugador ha cerrado la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            key_pressed_check(event.key)
    
    # Dibujar la pantalla
    draw_screen()
    
    # Mover las palabras hacia abajo
  
    for w in range(words_onscreen_count):
        word = words[w]
        word["y"] += 1
        if (word["x"]) < (window_width / 2) - (word["rect"].width /2):
            word["x"] += 0.3  
        else:
            word["x"] -= 0.3  

        if word["y"] == window_width-200:
            missed_words_count += 1
            attacked_word_id = 0
            attacked_word = None
            words.remove(word)

    check_onscreen_words()

    check_missed_words()

         
    # Mostrar palabras por destruir
    textScore = font_stats.render('Enemigos: ' + words.__len__().__str__(), True, white)
    window.blit(textScore, (int(window_width  - textScore.get_width()),1))

    # Imprimir el Score en pantalla
    textScore = font_stats.render('Score: ' + score.__str__(), True, white)
    window.blit(textScore, (1, 1))

    # Imprimir las palabras falladas
    textMissed = font_stats.render('Missed: ' + missed_words_count.__str__(), True, white)
    window.blit(textMissed, (1, 30))
        
    # Actualizar el conteo de Ticks
    clock_tick_count += 1
    # Actualizar la pantalla
    pygame.display.update()

    # Configuración del reloj
    clock.tick(60)
