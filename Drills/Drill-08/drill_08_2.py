from pico2d import *
import random


points = [(100, 100),(300,350),(200,500),(100,200)]
n=0
size=4

frame = 0
prev_x = 0

KPU_WIDTH, KPU_HEIGHT = 1280, 900
open_canvas(KPU_WIDTH, KPU_HEIGHT)
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')


def draw_curve_4_points(p1, p2, p3, p4):
    global frame
    global prev_x

    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        if x > prev_x:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        frame=(frame+1)%8
        prev_x=x
        update_canvas()
        delay(0.02)



while True:
    draw_curve_4_points(points[n-1],points[n],points[(n+1)%size],points[(n+2)%size])
    n=(n+1)%size


turtle.done()