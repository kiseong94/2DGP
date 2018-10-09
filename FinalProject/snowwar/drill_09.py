from pico2d import *
import random

open_canvas(1800,900)


# Game object class here

def handle_events():
    global running
    global main_character

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_d:
               main_character.key_manager(1)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                main_character.key_manager(0)

# initialization code
class Main_Character:
    def __init__(self):
        self.image = load_image('main.png')
        self.x = self.image.w//2
        self.y = self.image.h//2 + 230
        self.state = 0
        self.frame = 0

    def move_right(self):
        self.x = self.x + 3


    def draw(self):
        if self.state == 0:
            self.image.clip_draw(60 * (self.frame//2), 60 * self.state, 60, 60, self.x, self.y, 60, 60)
        else:
            self.image.clip_draw(60*(self.frame%8), 60*self.state, 60, 60, self.x, self.y, 60, 60)
        self.frame = (self.frame+1) % 16

    def action(self):
        if self.state == 1:
            self.move_right()

    def key_manager(self, state):
        self.state = state

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






# game main loop code
main_character = Main_Character()
back_ground = Back_Ground()
running = True

while running:
    handle_events()
    clear_canvas()
    back_ground.draw()
    main_character.draw()
    main_character.action()
    update_canvas()
    delay(0.05)

# finalization code