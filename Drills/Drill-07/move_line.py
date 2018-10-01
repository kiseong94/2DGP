from pico2d import *
import random
size=10
n=1
prev_x=0

points = [(random.randint(0,1280),random.randint(0,1024)) for i in range(size)]


open_canvas(1280, 1024)
kpu_ground = load_image('KPU_GROUND.PNG')
character = load_image('animation_sheet.png')


def draw_character(p1, p2 ):
    frame = 0
    global prev_x
    for i in range(0, 100 + 1, 2):

       clear_canvas()
       kpu_ground.draw(1280 // 2, 1024 // 2)
       t = i/100
       x = (1-t)*p1[0]+t*p2[0]
       y = (1-t)*p1[1]+t*p2[1]

       if(prev_x>x):
           character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
       else:
           character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
       update_canvas()
       frame = (frame + 1) % 8
       prev_x = x
       delay(0.06)


while True:
    draw_character(points[n-1], points[n])

    n = (n+1) % size



