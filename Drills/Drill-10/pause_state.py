import game_framework
import main_state
from pico2d import *


name = "PauseState"
image = None
t = None


def enter():
    global image, t
    t = 0
    image = load_image('pause_image.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()



def draw():
    clear_canvas()
    main_state.draw()
    if t < 1:
        image.draw(400, 300)
    update_canvas()







def update():
    global t
    t = (t+0.05) % 2


def pause():
    pass


def resume():
    pass






