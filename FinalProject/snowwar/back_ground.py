from pico2d import *
import random

class Back_Ground:
    def __init__(self):
        self.ground_image = load_image('ground.png')
        self.mountain_image = load_image('mountain.png')
        self.forest_image = load_image('forest.png')
        self.tree_image = load_image('trees.png')
        self.edge = 800

    def draw(self):
        self.mountain_image.draw(self.mountain_image.w, 200 + self.mountain_image.h, 1600, 400)
        self.forest_image.draw(800, 340, 1600, 160)
        self.tree_image.draw(800, 340 + self.tree_image.h//2, 1600, 320)
        self.ground_image.draw(400,230,800,60)
        self.ground_image.draw(400 + self.edge, 230, 800, 60)