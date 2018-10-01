from pico2d import *
import random
size=10
points = [(random.randint(-500,500),random.randint(-500,500)) for i in range(size)]


open_canvas(1200, 800)
character = load_image('animation_sheet.png')


def draw_line(p1, p2):


   for i in range(0, 100 + 1, 2):
       t = i/100
       x = (1-t)*p1[0]+t*p2[0]
       y = (1-t)*p1[1]+t*p2[1]

while True:
    draw_line(points[n-1], points[n])
    n = (n+1) % size

