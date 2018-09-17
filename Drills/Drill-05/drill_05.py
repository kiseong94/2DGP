from pico2d import *
import math

open_canvas()

character = load_image('animation_sheet.png')


def point_to_point(start_x, start_y, target_x, target_y):
    x, y = start_x, start_y
    vx, vy = (target_x - start_x)/20, (target_y - start_y)/20
    while x != target_x:
        clear_canvas()
        x += vx
        y += vy
        character.clip_draw(0 * 100, 100, 100, 100, x, y)
        update_canvas()
        delay(0.05)


point_to_point(100,100,200,200)



close_canvas()
