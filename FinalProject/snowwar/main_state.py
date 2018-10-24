import random
import json
import os

from pico2d import *

import game_framework
import main_character
import back_ground
import enemy

name = "MainState"

player = None
background = None
font = None
base_x = 0
cnt = 100
snows = []
enemies = []


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
    global cnt
    if cnt == 0:
        enemies.insert(0, enemy.Enemy_basic())
        cnt = 100
    else:
        cnt -= 1

    player.update()
    for s in snows:
        s.update()
        if s.check_destroyed():
            snows.remove(s)
    for e in enemies:
        e.update()


def draw():
    clear_canvas()
    background.draw()
    player.draw()
    for s in snows:
        s.draw()

    for e in enemies:
        e.draw()
    update_canvas()






