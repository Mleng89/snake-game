import cube


class Snake:
    def __init__(self, color, position):
        self.color = color
        self.head = cube[position]

    def move(self):
        ...

    def reset(self, position):
        self.head = cube(position)
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
