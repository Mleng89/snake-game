class Cube(object):
    def __init__(self, start, direction_X=1, direction_Y=0, color=(255, 0, 0)):
        self.start = start
        self.direction_X = direction_X
        self.direction_Y = direction_Y
        self.color = color

    def move(self, direction_X, direction_Y):
        self.direction_X = direction_X
        self.direction_Y = direction_Y
        self.position = (
            self.position[0] + self.direction_X,
            self.position[1] + self.direction_Y,
        )

    def draw(self, surface, eyes=False):
        ...
