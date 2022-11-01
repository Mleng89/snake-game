import pygame as pg
from cube import Cube
from snake import Snake

pg.init()
WIDTH, HEIGHT = 900, 900
ROWS = 30  # Can make this smaller to make game harder
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snek")

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def draw_Grid(width, rows, surface):
    # drawing lines vertical and horizontal
    size_between = width // rows
    x, y = 0, 0
    for length in range(ROWS):
        x = x + size_between
        y = y + size_between

        pg.draw.line(surface, WHITE, (x, 0), (x, WIDTH))
        pg.draw.line(surface, WHITE, (0, y), (WIDTH, y))


def reset_Grid(surface):
    WINDOW.fill(BLACK)
    draw_Grid(WIDTH, ROWS, surface)
    pg.display.update()


def random_food(rows, items):
    ...


def message_box(subject, content):
    ...


def main():
    clock = pg.time.Clock()
    sss = Snake((0, 255, 0), (10, 10))

    while True:
        pg.time.delay(50)  # Delay app -- does not run too fast (lower number = faster)
        clock.tick(60)  # Lower number makes it slower
        reset_Grid(WINDOW)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()


if __name__ == "__main__":
    main()
