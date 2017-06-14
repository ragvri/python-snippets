"""
checking modularity. Can the class we created be used elsewhere
"""
import random


class Blob:
    def __init__(self, color, x_boundary, y_boundary, size_range=(4, 8), mov_range=(-1, 2)):
        # when object created first the init method is run
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.size = random.randrange(size_range[0], size_range[1])
        self.mov_range = mov_range
        self.move_x = 0
        self.move_y = 0

    def move(self):
        self.move_x = random.randrange(self.mov_range[0], self.mov_range[1])
        self.move_y = random.randrange(self.mov_range[0], self.mov_range[1])  # movements in pixel form
        self.x += self.move_x
        self.y += self.move_y
