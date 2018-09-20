from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
left, right = -1, 1
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
direction = left

def handle_events():
    global running, move
    global x, y
    global cursor_x, cursor_y, vx, vy, t, direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cursor_x, cursor_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            move = True
            target_x, target_y = event.x, KPU_HEIGHT - 1 - event.y
            vx = (target_x - x)/20
            vy = (target_y - y)/20
            t = 0
            if vx < 0:
                direction = left
            else:
                direction = right
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def Move_To_Target():
    global x, y, move, t
    x = x + vx
    y = y + vy
    t += 1
    if direction == left:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    if t == 20:
        move = False


def Stand_Still():
    if direction == left:
        character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
move = False


cursor_x, cursor_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if move:
        Move_To_Target()
    else:
        Stand_Still()
    cursor.draw(cursor_x + cursor.w / 2, cursor_y - cursor.h / 2)
    frame = (frame + 1) % 8
    update_canvas()
    delay(0.06)
    handle_events()

close_canvas()




