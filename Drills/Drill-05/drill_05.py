from pico2d import *
import math

open_canvas()

character = load_image('animation_sheet.png')

path = {(203,535),(132,243),(535,470), (477, 203), (715, 136), (316, 225), (510, 92), (692, 518), (682, 336), (712, 349) }
path_index=0

start_x, start_y = 203,535


def point_to_point(start_x, start_y, target_x, target_y):
    frame = 0
    cnt = 0
    x, y = start_x, start_y
    vx, vy = (target_x - start_x)/20, (target_y - start_y)/20

    while cnt < 20:
        clear_canvas()
        frame = (frame + 1) % 8
        x += vx
        y += vy
        if vx > 0:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        cnt+=1
        delay(0.05)



while True:
    for target_x,target_y in path:
        point_to_point(start_x, start_y, target_x, target_y)
        start_x, start_y= target_x, target_y

close_canvas()
