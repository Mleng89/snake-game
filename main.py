import pygame as pg
from cube import Cube
from snake import Snake

pg.init()
WIDTH, HEIGHT = 900, 900
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snek")
# COLORS
BLACK = (0, 0, 0)


def draw_Grid(width, rows, surface):
    ...


def reset_Grid(surface):
    ...


def random_food(rows, items):
    ...


def message_box(subject, content):
    ...


def main():
    clock = pg.time.Clock()
    while True:
        clock.tick(60)
        WINDOW.fill(BLACK)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
    pg.display.flip()


if __name__ == "__main__":
    main()
