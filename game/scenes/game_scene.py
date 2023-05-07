import pygame
import random
from game.config import *
from game.utils import *
from game.scenes.Word import *


class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.word_sprites = pygame.sprite.Group()
        print(WORD_LIST)
        self.word_list = WORD_LIST
        self.next_word_time = pygame.time.get_ticks() + NEW_WORD_DELAY
        self.attacked_word_time = 0
        self.score = 0
        self.font = pygame.font.Font(FONT_NAME, 28)
        self.game_over = False
        self.done = False
      

    def new_word(self):
        self.word_list = WORD_LIST
        if len(self.word_list) > 0:
            word_text = random.choice(self.word_list)
            word = {"id": pygame.time.get_ticks(), "text": word_text, "x": random.randint(50, WIDTH - 50), "y": 0,
                    "speed": LETTER_SPEED, "attacked": 0}
            self.word_list.remove(word_text)
            self.word_sprites.add(Word(word))

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    key = event.unicode.lower()
                    if event.mod & pygame.KMOD_SHIFT:
                        key = event.unicode.upper()
                    # for accent_key in ACCENT_KEYS:
                    #     if event.key == accent_key:
                    #         key = ACCENT_KEYS[accent_key][key]
                    #         break
                    for word in self.word_sprites:
                        if ((self.attacked_word_time > 0 and word.id == self.attacked_word_time) or self.attacked_word_time == 0) and len(word.text) > 0:
                            if key == word.text[0]:
                                if len(word.text) >= 1:
                                    word.text = word.text[1:]
                                    self.attacked_word_time = word.id
                                    word.attacked = 1
                                if  len(word.text) == 0:
                                    self.word_sprites.remove(word)
                                    self.attacked_word_time = 0
                                    self.score += SCORE_INCREMENT
                                    self.new_word()

    def update(self,delta_time):
        current_time = pygame.time.get_ticks()
       
        if current_time > self.next_word_time:
            self.new_word()
            self.next_word_time = current_time + NEW_WORD_DELAY
        for word in self.word_sprites:
            word.update(delta_time)
            if word.rect.right < 0:
                self.word_sprites.remove(word)
                self.new_word()
            if word.attacked == 1:
                attacked_word_time = current_time + WORD_ATTACK_DELAY
        if self.attacked_word_time > 0 and current_time > self.attacked_word_time:
            for word in self.word_sprites:
                if word.id == self.attacked_word_time:
                    self.word_sprites.remove(word)
                    self.attacked_word_time = 0
                    self.new_word()
                    break
        if len(self.word_sprites) == 0:
            self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_text("Score: " + str(self.score), 28, WHITE, 10, 10)
        self.word_sprites.draw(self.screen)
        pygame.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(FONT_NAME, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_surface, (x, y))
