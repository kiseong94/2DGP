from pico2d import *
import main_state
import snow
import math

IDLE, MOVE, AIM, THROW, HIT, DEAD, SIT, MAKE_WALL, RELOAD = range(9)

MOVE_FRONT, TIME_UP, COL = range(3)


next_state_table = {
    MOVE: {MOVE_FRONT: MOVE, COL: DEAD},
    DEAD: {MOVE_FRONT: DEAD, COL: DEAD},
    HIT: {},

}


# initialization code
class Enemy:



    def enter_IDLE(self):
        pass

    def exit_IDLE(self):
        pass

    def do_IDLE(self):
        pass

    def draw_IDLE(self):
        pass



    def enter_MOVE(self):
        self.frame = 0

    def exit_MOVE(self):
        pass

    def do_MOVE(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.velocity


    def draw_MOVE(self):
        self.image.clip_draw(60 * self.frame, 60 * 0, 60, 60, self.x - main_state.base_x, self.y, 60, 60)




    def enter_RELOAD(self):
        pass

    def exit_RELOAD(self):
        pass

    def do_RELOAD(self):
        self.frame = (self.frame + 1) % 16

    def draw_RELOAD(self):
        pass



    def enter_SIT(self):
        pass

    def exit_SIT(self):
        pass

    def do_SIT(self):
        pass

    def draw_SIT(self):
        pass


    def enter_MAKE_WALL(self):
        pass

    def exit_MAKE_WALL(self):
        pass

    def do_MAKE_WALL(self):
        pass

    def draw_MAKE_WALL(self):
        pass


    def enter_AIM(self):
        pass


    def exit_AIM(self):
        pass

    def do_AIM(self):
        pass

    def draw_AIM(self):
        pass


    def enter_THROW(self):
        pass

    def exit_THROW(self):
        pass


    def do_THROW(self):
        pass

    def draw_THROW(self):
        pass


    def enter_HIT(self):
        pass

    def exit_HIT(self):
        pass

    def do_HIT(self):
        pass

    def draw_HIT(self):
        pass


    def enter_DEAD(self):
        self.frame = 0

    def exit_DEAD(self):
        pass

    def do_DEAD(self):
        if self.frame < 16:
            self.frame += 1

    def draw_DEAD(self):
        self.image.clip_draw(60 * (self.frame//2), 60 * 1, 60, 60, self.x - main_state.base_x, self.y, 60, 60)

    enter_state = {MOVE: enter_MOVE, DEAD: enter_DEAD}
    exit_state = {MOVE: exit_MOVE, DEAD: exit_DEAD}
    do_state = {MOVE: do_MOVE, DEAD: do_DEAD}
    draw_state = {MOVE: draw_MOVE, DEAD: draw_DEAD}


    def add_event(self, event):
        self.event_que.insert(0, event)


    def change_state(self, state):
        if self.cur_state != state:
            self.exit_state[self.cur_state](self)
            self.enter_state[state](self)
            self.cur_state = state

    def update(self):
        self.do_state[self.cur_state](self)
        self.action()

        for s in main_state.snows:
            if s.collision_object(self.x - 10, self.y + 25, self.x + 10, self.y - 25):
                self.add_event(COL)

        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])

    def draw(self):
        self.draw_state[self.cur_state](self)
        #draw_rectangle(self.x - 10 - main_state.base_x, self.y + 25, self.x + 10 - main_state.base_x, self.y - 25)

    def action(self):
        if self.cur_state != DEAD:
            self.add_event(MOVE_FRONT)




class Enemy_basic(Enemy):
    def __init__(self):
        self.image = load_image('enemy_image.png')
        self.velocity = -2
        self.cur_state = MOVE
        self.event_que = []
        self.x, self.y = 1800 + main_state.base_x, 30 + 260
        self.frame = 0
        self.reload_time = 0
        self.throw_power = 0
        self.timer = 0
        self.throw_degree = 0
