from pico2d import *

IDLE, MOVE, ATTACK, HIT, DEAD, SIT, MAKE_WALL, RELOAD = range(8)

A_DOWN, A_UP, S_DOWN, S_UP, W_DOWN, W_UP, D_DOWN, D_UP, R_DOWN, LEFT_BUTTON_DOWN, LEFT_BUTTON_UP = range(11)


key_event_table = {
    (SDL_KEYDOWN, SDLK_a): A_DOWN, (SDL_KEYUP, SDLK_a): A_UP,
    (SDL_KEYDOWN, SDLK_s): S_DOWN, (SDL_KEYUP, SDLK_s): S_UP,
    (SDL_KEYDOWN, SDLK_w): W_DOWN, (SDL_KEYUP, SDLK_w): W_UP,
    (SDL_KEYDOWN, SDLK_d): D_DOWN, (SDL_KEYUP, SDLK_d): D_UP,
    (SDL_KEYDOWN, SDLK_r): R_DOWN,
}



next_state_table = {
    IDLE: {A_DOWN: MOVE, D_DOWN: MOVE, A_UP: IDLE, D_UP: IDLE, S_DOWN: SIT, S_UP: IDLE, W_DOWN: MAKE_WALL, W_UP: IDLE, R_DOWN: RELOAD},
    MOVE: {A_DOWN: MOVE, D_DOWN: MOVE, A_UP: IDLE, D_UP: IDLE, S_DOWN: SIT, S_UP: MOVE, W_DOWN: MAKE_WALL, W_UP: MOVE, R_DOWN: RELOAD},
    RELOAD: {A_DOWN: MOVE, D_DOWN: MOVE, A_UP: RELOAD, D_UP: RELOAD, S_DOWN: SIT, S_UP: RELOAD, W_DOWN: MAKE_WALL, W_UP: RELOAD, R_DOWN: RELOAD},
    SIT: {A_DOWN: MOVE, D_DOWN: MOVE, A_UP: SIT, D_UP: SIT, S_DOWN: SIT, S_UP: IDLE, W_DOWN: MAKE_WALL, W_UP: SIT, R_DOWN: RELOAD},
    MAKE_WALL: {A_DOWN: MOVE, D_DOWN: MOVE, A_UP: MAKE_WALL, D_UP: MAKE_WALL, S_DOWN: SIT, S_UP: MAKE_WALL, W_DOWN: MAKE_WALL, W_UP: IDLE, R_DOWN: RELOAD},
    ATTACK: {},
    HIT: {},



}


# initialization code
class Main_Character:
    def __init__(self):
        self.event_que = []
        self.image = load_image('main.png')
        self.x, self.y = 0, 60 + 230
        self.cur_state = IDLE
        self.frame = 0
        self.velocity = 0
        self.reload_time = 6


    def enter_IDLE(self):
        self.frame = 0

    def exit_IDLE(self):
        pass

    def do_IDLE(self):
        self.frame = (self.frame + 1) % 8

    def draw_IDLE(self):
        self.image.clip_draw(60 * self.frame, 60 * 0, 60, 60, self.x, self.y, 60, 60)



    def enter_MOVE(self):
        self.frame = 0

    def exit_MOVE(self):
        pass

    def do_MOVE(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.velocity

    def draw_MOVE(self):
        if self.velocity > 0:
            self.image.clip_draw(60 * self.frame, 60 * 1, 60, 60, self.x, self.y, 60, 60)
        else:
            self.image.clip_draw(60 * self.frame, 60 * 2, 60, 60, self.x, self.y, 60, 60)



    def enter_RELOAD(self):
        self.frame = 0

    def exit_RELOAD(self):
        pass

    def do_RELOAD(self):
        self.frame = (self.frame + 1) % 8

    def draw_RELOAD(self):
        self.image.clip_draw(60 * self.frame, 60 * 3, 60, 60, self.x, self.y, 60, 60)



    def enter_SIT(self):
        self.frame = 0

    def exit_SIT(self):
        pass

    def do_SIT(self):
        self.frame = (self.frame + 1) % 8

    def draw_SIT(self):
        self.image.clip_draw(60 * self.frame, 60 * 4, 60, 60, self.x, self.y, 60, 60)


    def enter_MAKE_WALL(self):
        self.frame = 0

    def exit_MAKE_WALL(self):
        pass

    def do_MAKE_WALL(self):
        self.frame = (self.frame + 1) % 8

    def draw_MAKE_WALL(self):
        self.image.clip_draw(60 * self.frame, 60 * 5, 60, 60, self.x, self.y, 60, 60)


    def enter_ATTACK(self):
        pass

    def exit_ATTACK(self):
        pass

    def do_ATTACK(self):
        pass

    def draw_ATTACK(self):
        pass


    def enter_HIT(self):
        pass

    def exit_HIT(self):
        pass

    def do_HIT(self):
        pass

    def draw_HIT(self):
        pass

    enter_state = {IDLE: enter_IDLE, MOVE: enter_MOVE, RELOAD: enter_RELOAD, SIT: enter_SIT, MAKE_WALL: enter_MAKE_WALL}
    exit_state = {IDLE: exit_IDLE, MOVE: exit_MOVE, RELOAD: exit_RELOAD, SIT: exit_SIT, MAKE_WALL: exit_MAKE_WALL}
    do_state = {IDLE: do_IDLE, MOVE: do_MOVE, RELOAD: do_RELOAD, SIT: do_SIT, MAKE_WALL: do_MAKE_WALL}
    draw_state = {IDLE: draw_IDLE, MOVE: draw_MOVE, RELOAD: draw_RELOAD, SIT: draw_SIT, MAKE_WALL: draw_MAKE_WALL}


    def add_event(self, event):
        self.event_que.insert(0, event)


    def change_state(self, state):
        self.exit_state[self.cur_state](self)
        self.enter_state[state](self)
        self.cur_state = state

    def update(self):
        self.do_state[self.cur_state](self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])

    def draw(self):
        self.draw_state[self.cur_state](self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == D_DOWN:
                self.velocity += 3
            elif key_event == D_UP:
                self.velocity -= 3
            elif key_event == A_DOWN:
                self.velocity -= 2
            elif key_event == A_UP:
                self.velocity += 2
            self.add_event(key_event)


