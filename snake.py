import pygame

class Snake:
    def __init__(self, screen_width, screen_height, grid_size):
        self.length = 1
        self.positions = [((screen_width // 2), (screen_height // 2))]
        self.direction = None
        self.color = (0, 255, 0)
        self.head_color = (0, 200, 0)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.grid_size = grid_size

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        if self.direction:
            cur = self.get_head_position()
            x, y = self.direction
            new = (((cur[0] + (x * self.grid_size)) % self.screen_width),
                   (cur[1] + (y * self.grid_size)) % self.screen_height)
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((self.screen_width // 2), (self.screen_height // 2))]
        self.direction = None

    def draw(self, surface):
        for i, p in enumerate(self.positions):
            r = pygame.Rect((p[0], p[1]), (self.grid_size, self.grid_size))
            if i == 0:
                pygame.draw.rect(surface, self.head_color, r)
            else:
                pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (255, 255, 255), r, 1)

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.turn((0, -1))
        elif keys[pygame.K_DOWN]:
            self.turn((0, 1))
        elif keys[pygame.K_LEFT]:
            self.turn((-1, 0))
        elif keys[pygame.K_RIGHT]:
            self.turn((1, 0))
