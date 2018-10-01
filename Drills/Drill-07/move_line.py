from pico2d import *
import random
size=10
n=1
points = [(random.randint(-500,500),random.randint(-500,500)) for i in range(size)]


open_canvas(1280, 1024)
kpu_ground = load_image('KPU_GROUND.PNG')
character = load_image('animation_sheet.png')


def draw_line(p1, p2):


   for i in range(0, 100 + 1, 2):
       t = i/100
       x = (1-t)*p1[0]+t*p2[0]
       y = (1-t)*p1[1]+t*p2[1]

while True:
    clear_canvas()
    kpu_ground.draw(1280//2, 1024//2)
    draw_line(points[n-1], points[n])
    update_canvas()
    n = (n+1) % size

    delay(0.02)


