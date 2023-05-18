import pygame
from game.config import *
from game.utils import *



class GameOverScene:
    def __init__(self, screen, scores):
        self.screen = screen
        self.score = scores.score
        self.time_seconds = scores.time_seconds
        self.accuracy = scores.correct_letters / scores.pressed_letters * 100
        self.title_font = pygame.font.SysFont(FONT_TYPE, 60)
        self.font = pygame.font.SysFont(FONT_TYPE, 30)
        self.done = False
        self.next_scene = None

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_scene = 'menu_scene'
                    self.done = True

    def update(self,delta_time):
        self.process_input()
    
    def convert_time(self, time_seconds):
        horas = time_seconds // 3600
        minutos = (time_seconds % 3600) // 60
        segundos = time_seconds % 60
        
        tiempo_formateado = "{:02d}:{:02d}:{:02d}".format(int(horas), int(minutos), int(segundos))
        
        return tiempo_formateado

    def draw(self):
        self.screen.fill(BLACK)
        title_text = self.title_font.render("GAME OVER", True, WHITE)
        score_text = self.font.render("Your score: {} ({}wpm)".format(self.score, int(self.score / SCORE_INCREMENT / self.time_seconds * 60)), True, WHITE)
        accuracy_text = self.font.render("Your accuracy: {}%".format("{:.1f}".format(self.accuracy)), True, WHITE)
        time_text = self.font.render("Your time: {}".format(self.convert_time(self.time_seconds)), True, WHITE)
        prompt_text = self.font.render("Press space to return to main menu", True, WHITE)
       
        title_text_rect = title_text.get_rect(center=(WIDTH / 2, HEIGHT / 6))
        score_text_rect = score_text.get_rect(center=(WIDTH / 2, HEIGHT / 6 * 2))
        accuracy_text_rect = accuracy_text.get_rect(center=(WIDTH / 2, HEIGHT / 6 * 3))
        time_text_rect = accuracy_text.get_rect(center=(WIDTH / 2, HEIGHT / 6 * 4))
        prompt_text_rect = prompt_text.get_rect(center=(WIDTH / 2, HEIGHT / 6 * 5))
        self.screen.blit(title_text, title_text_rect)
        self.screen.blit(score_text, score_text_rect)
        self.screen.blit(accuracy_text, accuracy_text_rect)
        self.screen.blit(time_text, time_text_rect)
        self.screen.blit(prompt_text, prompt_text_rect)

