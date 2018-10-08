from pico2d import *
import random

open_canvas()


# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 600
        self.vy = random.randint(-10, -5)
        self.falling = True

        if random.randint(0, 1):
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

        self.r = self.image.h // 2

    def update(self):
        if self.falling:
            self.y += self.vy

    def draw(self):
        self.image.draw(self.x, self.y)

    def collision(self):
        if self.y <= 50+self.r:
            self.y = 50+self.r
            self.falling = False



team = [Boy() for i in range(11)]
balls = [Ball() for i in range(20)]
grass = Grass()
running = True

# game main loop code

while running:
    handle_events()
    clear_canvas()
    grass.draw()

    for boy in team:
        boy.update()
        boy.draw()

    for ball in balls:
        ball.update()
        ball.collision()
        ball.draw()

    update_canvas()
    delay(0.05)

# finalization code