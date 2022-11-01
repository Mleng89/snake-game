from cube import Cube
import pygame as pg

c = Cube


class Snake:
    body = []
    print(".body....>", body)
    turns = {}

    def __init__(self, color, position):
        self.color = color
        self.head = c(position)
        self.body.append(self.head)
        self.direction_X = 0
        self.direction_Y = 1

    def move(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            keys = pg.key.get_pressed()

            for key in keys:
                if keys[pg.K_LEFT]:
                    # x negative
                    self.direction_X = -1
                    self.direction_Y = 0
                    self.turns[self.head.position[:]] = [
                        self.direction_X,
                        self.direction_Y,
                    ]
                elif keys[pg.K_RIGHT]:
                    # x positive
                    self.direction_X = 1
                    self.direction_Y = 0
                    self.turns[self.head.position[:]] = [
                        self.direction_X,
                        self.direction_Y,
                    ]

                elif keys[pg.K_UP]:
                    # y negative
                    self.direction_X = 0
                    self.direction_Y = -1
                    self.turns[self.head.position[:]] = [
                        self.direction_X,
                        self.direction_Y,
                    ]

                elif keys[pg.K_DOWN]:
                    # y positive
                    self.direction_X = 0
                    self.direction_Y = 1
                    self.turns[self.head.position[:]] = [
                        self.direction_X,
                        self.direction_Y,
                    ]

        for idx, cube in enumerate(self.body):
            print(".....", self.body)
            p = cube.position[:]
            if p in self.turns:
                turn = self.turns[p]
                cube.move(turn[0], turn[1])
                if idx == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                cube.move(cube.direction_X, cube.direction_Y)

    def reset(self, position):
        self.head = c(position)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.direction_X = 0
        self.direction_Y = 1

    def addCube(self):
        tail = self.body[-1]
        x, y = tail.d

    def draw(self, surface):
        ...
