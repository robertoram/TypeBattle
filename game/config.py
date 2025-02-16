import pygame
import os

# Screen settings
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
# Fonts
FONT_NAME = pygame.font.match_font('monospace')

# Game settings
TITLE = "TypeBattle"
WORD_LIST =  [
    'bed',
    'generator',
    'base',
    'emerald',
    'diamond',
    'upgrade',
    'bridge',
    'wool',
    'clay',
    'iron',
    'gold',
    'armor',
    'sword',
    'axe',
    'pickaxe',
    'shears',
    'bow',
    'arrow',
    'tnt',
    'fireball',
    'gapple',
    'potion',
    'team',
    'trapped',
    'obsidian',
    'defender',
    'attacker',
    'rush',
    'void',
    'bridge',
    'egg',
    'ender',
    'pearl',
    'bedbug',
    'sharpness',
    'protection',
    'haste',
    'invisibility',
    'bridge',
    'builder',
    'miner',
    'fatigue',
    'jumper',
    'healer',
    'demolitionist',
    'archer',
    'iron',
    'golem',
    'emerald',
    'forge',
    'diamond',
    'forge',
    'mana',
    'spell',
    'shop',
    'upgrade',
    'NPC',
    'villager',
    'shopkeeper',
    'bedwars'
]


LETTER_SPEED = 15
LETTER_SPEED_INGREMENT = 1
NEW_WORD_DELAY = 1000
WORD_ATTACK_DELAY = 250
SCORE_INCREMENT = 10
PROJECTILE_SPEED = 100

# Game events
QUIT_EVENT = pygame.USEREVENT + 1
TITLE_EVENT = pygame.USEREVENT + 2

# Fonts
FONT_TYPE = "monospace"
FONT_SIZE = 32

#SOUNDS

SOUND_SUCCESS_PATH = os.path.join(os.path.dirname(__file__), 'assets', 'sounds', 'success_bell.wav')
SOUND_ERROR_PATH = os.path.join(os.path.dirname(__file__), 'assets', 'sounds', 'error_bell.wav')
#IMAGES
BG_PATH = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'background_scroll.jpg')
