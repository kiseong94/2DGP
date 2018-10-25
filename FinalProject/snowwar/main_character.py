from pico2d import *
import main_state
import snow
import math

IDLE, MOVE, AIM, THROW, HIT, DEAD, SIT, MAKE_WALL, RELOAD = range(9)

A_DOWN, A_UP, S_DOWN, S_UP, W_DOWN, W_UP, D_DOWN, D_UP, R_DOWN, LEFT_BUTTON_DOWN, LEFT_BUTTON_UP, TIME_UP = range(12)


key_event_table = {
    (SDL_KEYDOWN, SDLK_a): A_DOWN, (SDL_KEYUP, SDLK_a): A_UP,
    (SDL_KEYDOWN, SDLK_s): S_DOWN, (SDL_KEYUP, SDLK_s): S_UP,
    (SDL_KEYDOWN, SDLK_w): W_DOWN, (SDL_KEYUP, SDLK_w): W_UP,
    (SDL_KEYDOWN, SDLK_d): D_DOWN, (SDL_KEYUP, SDLK_d): D_UP,
    (SDL_KEYDOWN, SDLK_r): R_DOWN
}
mouse_event_table = {
    (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT): LEFT_BUTTON_DOWN,
    (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT): LEFT_BUTTON_UP,
}



next_state_table = {
    IDLE: {A_DOWN: MOVE, D_DOWN: MOVE, A_UP: IDLE, D_UP: IDLE, S_DOWN: SIT, S_UP: IDLE, W_DOWN: MAKE_WALL,
           W_UP: IDLE, R_DOWN: RELOAD, LEFT_BUTTON_DOWN: AIM, LEFT_BUTTON_UP: IDLE, TIME_UP: IDLE},
    MOVE: {A_DOWN: MOVE, D_DOWN: MOVE, A_UP: IDLE, D_UP: IDLE, S_DOWN: SIT, S_UP: MOVE, W_DOWN: MAKE_WALL,
           W_UP: MOVE, R_DOWN: RELOAD, LEFT_BUTTON_DOWN: AIM, LEFT_BUTTON_UP: MOVE, TIME_UP: IDLE},
    RELOAD: {A_DOWN: MOVE, D_DOWN: MOVE, A_UP: RELOAD, D_UP: RELOAD, S_DOWN: SIT, S_UP: RELOAD, W_DOWN: MAKE_WALL,
             W_UP: RELOAD, R_DOWN: RELOAD, LEFT_BUTTON_DOWN: AIM, LEFT_BUTTON_UP: RELOAD, TIME_UP: IDLE},
    SIT: {A_DOWN: MOVE, D_DOWN: MOVE, A_UP: SIT, D_UP: SIT, S_DOWN: SIT, S_UP: IDLE, W_DOWN: MAKE_WALL,
          W_UP: SIT, R_DOWN: RELOAD, LEFT_BUTTON_DOWN: AIM, LEFT_BUTTON_UP: SIT, TIME_UP: IDLE},
    MAKE_WALL: {A_DOWN: MOVE, D_DOWN: MOVE, A_UP: MAKE_WALL, D_UP: MAKE_WALL, S_DOWN: SIT, S_UP: MAKE_WALL,
                W_DOWN: MAKE_WALL, W_UP: IDLE, R_DOWN: RELOAD, LEFT_BUTTON_DOWN: AIM, LEFT_BUTTON_UP: MAKE_WALL, },
    AIM: {A_DOWN: AIM, D_DOWN: AIM, A_UP: AIM, D_UP: AIM, S_DOWN: AIM, S_UP: AIM, TIME_UP: IDLE,
          W_DOWN: AIM, W_UP: AIM, R_DOWN: AIM, LEFT_BUTTON_DOWN: AIM, LEFT_BUTTON_UP: THROW, TIME_UP: IDLE},
    THROW: {A_DOWN: THROW, D_DOWN: THROW, A_UP: THROW, D_UP: THROW, S_DOWN: THROW, S_UP: THROW,
            W_DOWN: THROW, W_UP: THROW, R_DOWN: THROW, LEFT_BUTTON_DOWN: THROW, LEFT_BUTTON_UP: THROW, TIME_UP: IDLE},
    HIT: {},

}


# initialization code
class Main_Character:
    def __init__(self):
        self.event_que = []
        self.image = load_image('main.png')
        self.arrow_image = load_image('arrow.png')
        self.throw_image = load_image('throw_parts.png')
        self.x, self.y = 200, 30 + 260
        self.cur_state = IDLE
        self.frame = 0
        self.velocity = 0
        self.reload_time = 60
        self.throw_power = 0
        self.aim_base_x, self.aim_base_y = 0, 0
        self.aim_draw_x, self.aim_draw_y = 0, 0
        self.timer = 0
        self.throw_degree = 0
        self.snow_stack = 0



    def enter_IDLE(self):
        self.frame = 0

    def exit_IDLE(self):
        pass

    def do_IDLE(self):
        self.frame = (self.frame + 1) % 16

    def draw_IDLE(self):
        self.image.clip_draw(60 * (self.frame//2), 60 * 0, 60, 60, 200, self.y, 60, 60)



    def enter_MOVE(self):
        self.frame = 0

    def exit_MOVE(self):
        pass

    def do_MOVE(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.velocity
        main_state.base_x += self.velocity
        main_state.background.move_ground(self.velocity)
        main_state.background.move_forest(self.velocity)
        main_state.background.move_mountain(self.velocity)


    def draw_MOVE(self):
        if self.velocity > 0:
            self.image.clip_draw(60 * self.frame, 60 * 1, 60, 60, 200, self.y, 60, 60)
        else:
            self.image.clip_draw(60 * self.frame, 60 * 2, 60, 60, 200, self.y, 60, 60)



    def enter_RELOAD(self):
        self.frame = 0
        self.timer = 0

    def exit_RELOAD(self):
        pass

    def do_RELOAD(self):
        self.frame = (self.frame + 1) % 16
        if self.timer == self.reload_time:
            self.snow_stack += 1
            self.add_event(TIME_UP)
        else:
            self.timer += 1

    def draw_RELOAD(self):
        self.image.clip_draw(60 * (self.frame//2), 60 * 3, 60, 60, 200, self.y, 60, 60)



    def enter_SIT(self):
        self.frame = 0

    def exit_SIT(self):
        pass

    def do_SIT(self):
        self.frame = (self.frame + 1) % 16

    def draw_SIT(self):
        self.image.clip_draw(60 * (self.frame//2), 60 * 4, 60, 60, 200, self.y, 60, 60)


    def enter_MAKE_WALL(self):
        self.frame = 0

    def exit_MAKE_WALL(self):
        pass

    def do_MAKE_WALL(self):
        self.frame = (self.frame + 1) % 16

    def draw_MAKE_WALL(self):
        self.image.clip_draw(60 * (self.frame//2), 60 * 5, 60, 60, 200, self.y, 60, 60)


    def enter_AIM(self):
        self.aim_draw_x, self.aim_draw_y = self.aim_base_x, self.aim_base_y
        self.frame = 0
        self.throw_power = 0


    def exit_AIM(self):
        pass

    def do_AIM(self):
        if self.aim_base_y <= self.aim_draw_y:
            self.aim_draw_y = self.aim_base_y - 1
        if self.aim_base_x <= self.aim_draw_x:
            self.aim_draw_x = self.aim_base_x - 1
        self.throw_power = math.sqrt((self.aim_draw_x - self.aim_base_x)**2+(self.aim_base_y - self.aim_draw_y)**2)
        self.throw_degree = math.atan((self.aim_draw_x - self.aim_base_x)/(self.aim_base_y - self.aim_draw_y))

    def draw_AIM(self):
        self.throw_image.clip_composite_draw(40 * 1, 0, 40, 45, clamp(-1.2, self.throw_degree, 0), 'n', 200, self.y + 10, 40, 45)
        self.image.clip_draw(60 * 0, 60 * 6, 60, 60, 200, self.y, 60, 60)
        self.throw_image.clip_composite_draw(40 * 0, 0, 40, 45, clamp(-2, self.throw_degree, -0.2), 'n', 200 - 5, self.y + 10, 40, 45)
        self.throw_image.clip_composite_draw(40 * 2, 0, 40, 45, clamp(-2, self.throw_degree, -0.6) - 30, 'n', 200 - 1, self.y + 15, 40, 45)
        self.arrow_image.rotate_draw(self.throw_degree, 200, 350, 10+self.throw_power/12, 30 + self.throw_power/2)


    def enter_THROW(self):
        self.frame = 0
        self.timer = 8

    def exit_THROW(self):
        self.snow_stack = 0
        main_state.snows.insert(0, snow.Snow(200, self.y + 10, (self.aim_base_x-self.aim_draw_x)/15 + 5, (self.aim_base_y-self.aim_draw_y)/15))

    def do_THROW(self):
        self.timer -= 1
        self.frame += 1
        if self.timer <= 0:
            self.add_event(TIME_UP)

    def draw_THROW(self):
        self.image.clip_draw(60 * (self.frame//2), 60 * 7, 60, 60, 200, self.y, 60, 60)


    def enter_HIT(self):
        pass

    def exit_HIT(self):
        pass

    def do_HIT(self):
        pass

    def draw_HIT(self):
        pass

    enter_state = {IDLE: enter_IDLE, MOVE: enter_MOVE, RELOAD: enter_RELOAD, SIT: enter_SIT,
                   MAKE_WALL: enter_MAKE_WALL, AIM: enter_AIM, THROW: enter_THROW}
    exit_state = {IDLE: exit_IDLE, MOVE: exit_MOVE, RELOAD: exit_RELOAD, SIT: exit_SIT,
                  MAKE_WALL: exit_MAKE_WALL, AIM: exit_AIM, THROW: exit_THROW}
    do_state = {IDLE: do_IDLE, MOVE: do_MOVE, RELOAD: do_RELOAD, SIT: do_SIT,
                MAKE_WALL: do_MAKE_WALL, AIM: do_AIM, THROW: do_THROW}
    draw_state = {IDLE: draw_IDLE, MOVE: draw_MOVE, RELOAD: draw_RELOAD, SIT: draw_SIT,
                  MAKE_WALL: draw_MAKE_WALL, AIM: draw_AIM, THROW: draw_THROW}


    def add_event(self, event):
        self.event_que.insert(0, event)


    def change_state(self, state):
        if self.cur_state != state:
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
        elif (event.type, event.button) in mouse_event_table:
            key_event = mouse_event_table[(event.type, event.button)]
            if key_event == LEFT_BUTTON_DOWN:
                if self.snow_stack == 0:
                    key_event = R_DOWN
                else:
                    self.aim_base_x, self.aim_base_y = event.x, 900 - event.y -1
            self.add_event(key_event)

        elif event.type == SDL_MOUSEMOTION and self.cur_state == AIM:
            self.aim_draw_x, self.aim_draw_y = event.x, 900 - event.y -1




