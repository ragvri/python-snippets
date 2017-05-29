import random
import pygame
from blob import Blob

STARTINGH_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


# to inherit pass class into the child class
# when we inherit from a method we inherit all its methods and attributes
# BlueBlob is child of Blob or subclass of Blob
class BlueBlob(Blob):
    # in BlueBob, we want all the objects to be blue. So we create another init method. But we need to pass super(),
    # this allows us to run the init of the super class.
    # When we use super, we don't pass self
    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(color, x_boundary, y_boundary)
        self.color = BLUE

    # adding new methods to child class
    def move_fast(self):
        self.x += random.randrange(-7, 7)
        self.y += random.randrange(-7, 7)


def draw_environment(blobs_list):
    game_display.fill(WHITE)
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


def main():
    blue_blobs = dict(enumerate([BlueBlob(BLUE, WIDTH, HEIGHT) for i in range(STARTINGH_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([BlueBlob(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment([blue_blobs, red_blobs])
        clock.tick(60)  # 60 frames per second max


if __name__ == main():
    main()
