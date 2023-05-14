import pygame
import random
import os
from game.config import *
from game.utils import *
from game.sprites.word import *
from game.utils.scores import Scores


class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.word_sprites = pygame.sprite.Group()
        self.word_list = WORD_LIST
        self.next_word_time = pygame.time.get_ticks() + NEW_WORD_DELAY
        self.attacked_word_time = 0
        self.attacked_word_id = 0
        self.score = 0
        self.missed = 0
        self.font = pygame.font.Font(FONT_NAME, 28)
        self.game_over = False
        self.done = False
        self.word_list = WORD_LIST.copy()
        self.total_pressed_letters = 0
        self.correct_pressed_letters = 0
        self.scores = None
        
        self.background = pygame.transform.scale(pygame.image.load(BG_PATH), (WIDTH, HEIGHT))
        self.sucess_sound = pygame.mixer.Sound(SOUND_SUCCESS_PATH)
      
       

    def new_word(self):
       
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
                if event.key == pygame.K_ESCAPE:
                    self.next_scene = 'menu_scene'
                    #self.word_sprites.remove(any)
                    self.done = True
                if event.unicode.isalpha():
                    self.total_pressed_letters += 1
                    key = event.unicode.lower()
                    if event.mod & pygame.KMOD_SHIFT:
                        key = event.unicode.upper()
                    
                    for word in self.word_sprites:
                        if ((self.attacked_word_id > 0 and word.id == self.attacked_word_id) or self.attacked_word_id == 0) and len(word.text) > 0:
                            if key == word.text[0]:
                                if len(word.text) >= 1 and len(word.text) > 0:
                                    word.text = word.text[1:]
                                    self.attacked_word_id = word.id
                                    word.attack()
                                    self.correct_pressed_letters += 1
                                   
                                if  len(word.text) == 0:
                                    self.word_sprites.remove(word)
                                    self.attacked_word_id = 0
                                    self.score += SCORE_INCREMENT
                                    pygame.mixer.Sound.play(self.sucess_sound)
                                    self.new_word()
                                    break
    def reset_scene(self):
        self.score = 0
        self.missed = 0
        self.total_pressed_letters = 0
        self.correct_pressed_letters = 0
        self.scores = None
        self.done = False
        self.attacked_word_id = 0
        self.word_list = WORD_LIST.copy()
        self.word_sprites = pygame.sprite.Group()




    def update(self,delta_time):
        self.process_input()
        current_time = pygame.time.get_ticks()

        if len(self.word_sprites) == 0 and (self.total_pressed_letters > 0 or self.missed > 0):
                self.scores = Scores({"score": self.score, "pressed_letters": self.total_pressed_letters , "correct_letters": self.correct_pressed_letters})
               
                self.next_scene = 'game_over'
                self.done = 1

        if current_time > self.next_word_time:
            self.new_word()
            self.next_word_time = current_time + NEW_WORD_DELAY
            
        for word in self.word_sprites:
            word.update(delta_time)
            if word.projectile:
                word.projectile.draw(self.screen)
            if word.rect.y >= HEIGHT:
                self.attacked_word_id = 0
                self.word_sprites.remove(word)
                self.missed += 1
                #self.new_word()
            #if word.attacked == 1:
            #    self.attacked_word_time = current_time + WORD_ATTACK_DELAY
        if self.attacked_word_id > 0 and current_time > self.attacked_word_time:
            for word in self.word_sprites:
                if word.id == self.attacked_word_id and len(word.text) == 0:
                    self.word_sprites.remove(word)
                    self.attacked_word_id = 0
                    self.new_word()
                    break
        
            

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.draw_text("Score: " + str(self.score), 28, WHITE, 10, 10)
        self.draw_text("Missed: " + str(self.missed), 28, WHITE, 10, 35)
        self.word_sprites.draw(self.screen)
            
        pygame.display.flip()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(FONT_NAME, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        
        text_rect.topleft = (x, y)
        self.screen.blit(text_surface, (x, y))
