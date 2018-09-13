from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

left = True
right = False

direction = right
x = 0
frame = 0

while True:
    clear_canvas()
    grass.draw(400, 30)

    if direction == right:
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
        x += 10
        if x == 800:
            direction = left
    else:
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        x -= 10
        if x == 0:
            direction = right

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()



close_canvas()

