import pygame
import random

class Obstacle:
    def __init__(self, screen_width, screen_height, grid_size):
        self.position = (0, 0)
        self.color = (0, 0, 255)
        self.width = grid_size
        self.height = grid_size * 2
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_size = grid_size
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, self.screen_width // self.grid_size - 1) * self.grid_size,
                         random.randint(0, self.screen_height // self.grid_size - 2) * self.grid_size)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (self.width, self.height))
        pygame.draw.rect(surface, self.color, r)
