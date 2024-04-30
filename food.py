import pygame
import random

class Food:
    def __init__(self, screen_width, screen_height, grid_size):
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_size = grid_size
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, self.screen_width // self.grid_size - 1) * self.grid_size,
                         random.randint(0, self.screen_height // self.grid_size - 1) * self.grid_size)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (self.grid_size, self.grid_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (255, 255, 255), r, 1)
