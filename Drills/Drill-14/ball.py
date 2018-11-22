import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None
    background = None

    def __init__(self, bg):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        if Ball.background == None:
            Ball.background = bg
        self.x, self.y, self.fall_speed = random.randint(100, 1700), random.randint(100, 1000), 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        window_x, window_y = self.x - self.background.window_left, self.y - self.background.window_bottom
        self.image.draw(window_x, window_y)
        #draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

