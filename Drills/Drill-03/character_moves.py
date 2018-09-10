from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_rect(start_x,start_y):
    x,y=start_x,start_y

    while x<800-50:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+5
        delay(0.01)

    while y<600-50:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+5
        delay(0.01)

    while x>50:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-5
        delay(0.01)

    while y>start_y:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-5
        delay(0.01)

    while x<start_x:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+5
        delay(0.01)

def move_circle():
    degree=360

    while degree>0:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+200*math.cos(math.radians(270+degree)),290+200*math.sin(math.radians(270+degree)))
        degree=degree-5
        delay(0.02)    




start_x=400
start_y=90

x=0



while True:
    move_rect(start_x,start_y)
    move_circle()
    
    
close_canvas()
