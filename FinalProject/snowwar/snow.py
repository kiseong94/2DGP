from pico2d import *



class Snow:
    def __init__(self, x, y, vx, vy):
        self.image = load_image('snow.png')
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.destroy = False


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.destroy == False:
            self.x += self.vx
            self.y += self.vy
            self.vy -= 0.5
            self.collision()

    def collision(self):
        if self.y < 260:
            self.vx, self.vy = 0, 0
            self.destroy = True

