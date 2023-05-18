import pygame
import random
from game.config import *


class Scores:
    def __init__(self, data):
        super().__init__()
        self.score = data["score"]
        self.pressed_letters = data["pressed_letters"]
        self.correct_letters = data["correct_letters"]
        self.time_seconds = data["time_seconds"]


