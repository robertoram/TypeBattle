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
WORD_LIST = ["python", "pygame", "keyboard", "window", "score", "game"]
LETTER_SPEED = 5
NEW_WORD_DELAY = 1000
WORD_ATTACK_DELAY = 3000
SCORE_INCREMENT = 10

# Game events
QUIT_EVENT = pygame.USEREVENT + 1
TITLE_EVENT = pygame.USEREVENT + 2

# Fonts
FONT_TYPE = "Arial"
FONT_SIZE = 32