import random
import json
import os

from pico2d import *

import game_framework
import main_character
import back_ground
import snow

name = "MainState"

player = None
background = None
font = None
base_x = 0
snows = []


def enter():
    global player
    global background
    player = main_character.Main_Character()
    background = back_ground.Back_Ground()


def exit():
    global player
    global background
    del player
    del background



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
    for s in snows:
        s.update()

def draw():
    clear_canvas()
    background.draw()
    player.draw()
    for s in snows:
        s.draw()
    update_canvas()






