import pygame
from game.config import *
from game.utils import *



class GameOverScene:
    def __init__(self, screen, scores):
        self.screen = screen
        self.score = scores.score
        self.accuracy = scores.correct_letters / scores.pressed_letters * 100
        self.title_font = pygame.font.SysFont(FONT_TYPE, 60)
        self.font = pygame.font.SysFont(FONT_TYPE, 30)
        self.done = False
        self.next_scene = None

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.QUIT:
                return QUIT_EVENT
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.next_scene = 'menu_scene'
                self.done = True

    def update(self,delta_time):
        pass

    def draw(self):
        self.screen.fill(BLACK)
        title_text = self.title_font.render("GAME OVER", True, WHITE)
        score_text = self.font.render("Your score: {}".format(self.score), True, WHITE)
        accuracy_text = self.font.render("Your accuracy: {}%".format("{:.1f}".format(self.accuracy)), True, WHITE)
        prompt_text = self.font.render("Press space to return to main menu", True, WHITE)
        title_text_rect = title_text.get_rect(center=(WIDTH / 2, HEIGHT / 5))
        score_text_rect = score_text.get_rect(center=(WIDTH / 2, HEIGHT / 5 * 2))
        accuracy_text_rect = accuracy_text.get_rect(center=(WIDTH / 2, HEIGHT / 5 * 3))
        prompt_text_rect = prompt_text.get_rect(center=(WIDTH / 2, HEIGHT / 5 * 4))
        self.screen.blit(title_text, title_text_rect)
        self.screen.blit(score_text, score_text_rect)
        self.screen.blit(accuracy_text, accuracy_text_rect)
        self.screen.blit(prompt_text, prompt_text_rect)

