import random
import json
import os

from pico2d import *

import game_framework

import main_character



name = "MainState"

player = None
font = None



def enter():
    global player
    player = main_character.Main_Character()


def exit():
    global player
    del player



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            player.handle_event(event)



def update():
    player.update()

def draw():
    clear_canvas()
    player.draw()
    update_canvas()






