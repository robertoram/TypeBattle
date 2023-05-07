import pygame

# Screen settings
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Fonts
FONT_NAME = pygame.font.match_font('monospace')

# Game settings
TITLE = "TypeBattle"
WORD_LIST = ['algoritmo', 'biblioteca', 'computadora', 'depuración', 'estructura'] #, 'función', 'hardware', 'interfaz', 'java', 'kernel', 'lenguaje', 'memoria', 'navegador', 'objeto', 'programa', 'query', 'repositorio', 'sintaxis', 'tecnología', 'usuario', 'variable', 'web', 'XML', 'yield', 'zip', 'aplicación', 'bit', 'código', 'debug', 'ensamblador', 'fragmento', 'GNU', 'hardware', 'internet', 'JavaScript', 'kernel', 'lenguaje', 'multitarea', 'núcleo', 'optimización', 'procesador', 'query', 'red', 'servidor', 'teclado', 'unicode', 'vector', 'whitespace', 'XHTML']
LETTER_SPEED = 20
NEW_WORD_DELAY = 3000
WORD_ATTACK_DELAY = 3000
SCORE_INCREMENT = 10

# Game events
QUIT_EVENT = pygame.USEREVENT + 1
TITLE_EVENT = pygame.USEREVENT + 2

# Fonts
FONT_TYPE = "Arial"
FONT_SIZE = 32

