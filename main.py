import pygame
from snake import Snake
from food import Food
from obstacle import Obstacle
import random

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 20
WHITE = (255, 255, 255)

# Game states
WAITING = 0
RUNNING = 1

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Snake(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
    food = Food(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
    obstacles = []

    game_state = WAITING

    # Load background image
    background = pygame.image.load("grass_background.jpg")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and game_state == WAITING:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    game_state = RUNNING
                    pygame.time.wait(300)  # Pause for 300 milliseconds before starting the game
                    # Randomize obstacle positions on new try
                    obstacles = [Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE) for _ in range(5)]

        if game_state == RUNNING:
            snake.handle_keys()
            snake.move()

            if snake.get_head_position() == food.position:
                snake.length += 1
                food.randomize_position()

            for obstacle in obstacles:
                if snake.get_head_position()[0] in range(obstacle.position[0], obstacle.position[0] + obstacle.width) and \
                    snake.get_head_position()[1] in range(obstacle.position[1], obstacle.position[1] + obstacle.height):
                    snake.reset()
                    obstacles = [Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE) for _ in range(5)]  # Reset obstacles

            surface.blit(background, (0, 0))  # Draw background
            snake.draw(surface)
            food.draw(surface)
            for obstacle in obstacles:
                obstacle.draw(surface)
            screen.blit(surface, (0, 0))
            pygame.display.update()
            clock.tick(10)
        else:
            surface.blit(background, (0, 0))  # Draw background
            font = pygame.font.Font(None, 36)
            text = font.render("Press any arrow key to start", True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            surface.blit(text, text_rect)
            screen.blit(surface, (0, 0))
            pygame.display.update()

if __name__ == "__main__":
    main()
