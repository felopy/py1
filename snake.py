import pygame as pg
from random import randrange

# Constants
WINDOW = 1000
TILE_SIZE = 40
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

# Function to get a random position
def get_random_position():
    return [randrange(*RANGE), randrange(*RANGE)]

# Function to handle user input
def handle_input(dirs, snake_dir):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_s and dirs[pg.K_s]:
                snake_dir = (0, TILE_SIZE)
                dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
            if event.key == pg.K_a and dirs[pg.K_a]:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
            if event.key == pg.K_d and dirs[pg.K_d]:
                snake_dir = (TILE_SIZE, 0)
                dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}
    return dirs, snake_dir

# Function to update the game state
def update_game_state(snake, segments, length, snake_dir, time, time_step, food):
    snake.move_ip(snake_dir)
    segments.append(snake.copy())
    segments = segments[-length:]
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1

    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        return True, segments, length  # Player has lost
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1

    return False, segments, length

# Function to draw the game screen
def draw_screen(screen, snake, segments, food):
    screen.fill('black')
    pg.draw.rect(screen, 'red', food)
    [pg.draw.rect(screen, 'green', segment) for segment in segments]
    pg.display.flip()

# Main game loop
def main():
    pg.init()
    snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
    snake.center = get_random_position()
    length = 1
    segments = [snake.copy()]
    snake_dir = (0, 0)
    time, time_step = 0, 100  # Adjust time_step for a more reasonable frame rate
    food = snake.copy()
    food.center = get_random_position()
    screen = pg.display.set_mode([WINDOW] * 2)
    clock = pg.time.Clock()
    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
    
    game_over = False  # Variable to control when the game is over

    while not game_over:
        game_over, segments, length = update_game_state(snake, segments, length, snake_dir, time, time_step, food)
        if game_over:
            break  # Exit the loop if the game is over
        
        dirs, snake_dir = handle_input(dirs, snake_dir)
        draw_screen(screen, snake, segments, food)
        clock.tick(10)  # Adjust the frame rate to a reasonable value (e.g., 10)

if __name__ == "__main__":
    main()

