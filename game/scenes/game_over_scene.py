import pygame
from game.config import *
from game.utils import *


class GameOverScene:
    def __init__(self, score):
        self.score = score
        self.title_font = pygame.font.SysFont(FONT_TYPE, 60)
        self.font = pygame.font.SysFont(FONT_TYPE, 30)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.QUIT:
                return QUIT_EVENT
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return TITLE_EVENT

    def update(self,delta_time):
        pass

    def render(self, screen):
        screen.fill(BLACK)
        title_text = self.title_font.render("GAME OVER", True, WHITE)
        score_text = self.font.render("Your score: {}".format(self.score), True, WHITE)
        prompt_text = self.font.render("Press space to return to main menu", True, WHITE)
        title_text_rect = title_text.get_rect(center=(WIDTH / 2, 200))
        score_text_rect = score_text.get_rect(center=(WIDTH / 2, 300))
        prompt_text_rect = prompt_text.get_rect(center=(WIDTH / 2, 400))
        screen.blit(title_text, title_text_rect)
        screen.blit(score_text, score_text_rect)
        screen.blit(prompt_text, prompt_text_rect)

