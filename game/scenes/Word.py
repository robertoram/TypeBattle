import pygame
from game.config import *

class Word(pygame.sprite.Sprite):
    def __init__(self, word_data):
        super().__init__()
        self.id = word_data["id"]
        self.text = word_data["text"]
        self.x = word_data["x"]
        self.y = word_data["y"]
        self.speed = word_data["speed"] if "speed" in word_data else LETTER_SPEED
        self.attacked = word_data["attacked"] if "attacked" in word_data else 0
        self.font = pygame.font.Font(None, 40)
        self.image = self.font.render(self.text, True, WHITE)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self, delta_time):
        self.y += self.speed * delta_time
        self.rect.center = (self.x, self.y)

    def attack(self):
        self.attacked = 1
        self.image = self.font.render(self.text, True, (255, 0, 0))

    def render_word(self):
            self.text = self.font.render(self.word, True, WHITE)
            self.image.blit(self.text, (0, 0))