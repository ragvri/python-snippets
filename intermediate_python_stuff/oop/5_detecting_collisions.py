import random
import pygame
from blob import Blob
import numpy as np

STARTINGH_BLUE_BLOBS = 20
STARTING_RED_BLOBS = 20
STARTING_GREEN_BLOBS = 20
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


class BlueBlob(Blob):
    def __init__(self, x_boundary, y_boundary):
        super().__init__(BLUE, x_boundary, y_boundary)

    def move_fast(self):
        self.x += random.randrange(-7, 7)
        self.y += random.randrange(-7, 7)

    def __add__(self, other_blob):
        if other_blob.color == (255, 0, 0):
            self.size -= other_blob.size
            other_blob.size -= self.size
        elif other_blob.color == (0, 255, 0):
            self.size += other_blob.size
            other_blob.size = 0
        elif other_blob.color == (0, 0, 255):
            pass
        else:
            raise Exception("Try to combine required color ")


class GreenBlob(Blob):
    def __init__(self, x_boundary, y_boundary):
        super().__init__(GREEN, x_boundary, y_boundary)


class RedBlob(Blob):
    def __init__(self, x_boundary, y_boundary):
        super().__init__(RED, x_boundary, y_boundary)


def is_touching(b1, b2):
    return np.linalg.norm(np.array([b1.x, b1.y]) - np.array([b2.x, b2.y])) < b1.size + b2.size


def handle_collisions(blob_list):
    blues, reds, greens = blob_list
    for blue_id, blue_blob in blues.copy().items():  # we won't never want to modify thing that we are iterating
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                if blue_blob == other_blob:
                    pass
                elif is_touching(blue_blob, other_blob):
                    blue_blob + other_blob
                    if other_blob.size <= 0:
                        del other_blobs[other_blob_id]
                    if blue_blob.size <= 0:
                        del blues[blue_id]
    return blues, reds, greens


def draw_environment(blobs_list):
    game_display.fill(WHITE)
    blues, reds, greens = handle_collisions(blobs_list)
    for blobs_dict in blobs_list:
        for blob_id in blobs_dict:
            blob = blobs_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            if blob.x < 0:
                blob.x = 0
            elif blob.x > blob.x_boundary:
                blob.y = blob.x_boundary
            if blob.y < 0:
                blob.y = 0
            elif blob.y > blob.y_boundary:
                blob.y = blob.y_boundary

    pygame.display.update()
    return blues, reds, greens


def main():
    blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for i in range(STARTINGH_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        blue_blobs, red_blobs, green_blobs = draw_environment([blue_blobs, red_blobs, green_blobs])
        clock.tick(60)  # 60 frames per second max


if __name__ == main():
    main()
