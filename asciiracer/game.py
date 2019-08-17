import curses
import numpy as np
from . import environment
from .environment import draw_background, draw_tracks, draw_statusbar, \
                    draw_debris, draw_horizon, draw_car, draw_money
from . import hud
from .hud import draw_hud
from .mechanics import update_state
from .config import GAME_SIZE, FPS, BASE_SPEED
from .misc import limit_fps


class AsciiRacer(object):
    def __init__(self):
        self.SCENE = [  # draw_tracks,
                      draw_hud, draw_horizon, draw_tracks,
                      # draw_debris,
                      draw_car, draw_money, draw_background]
        self.reset_state()
        self.initialize_screen()
        curses.noecho()
        curses.cbreak()

    def reset_state(self):
        self.state = {'frames': 0,
                      'time': 0.0,  # seconds
                      'speed': BASE_SPEED,  # coord per frame
                      'car': None,
                      'car_x': 0,  # range -1:1
                      'car_steer_tuple': None,
                      'car_speed_tuple': None,
                      'debris': [],  # debris objects drawn in scene
                      'money': [],  # money objects drawn in scene
                      'score': 0,
                      'pdb': False}  # for testing

    # @limit_fps(fps=FPS)
    def draw_scene(self, screen):
        for draw_element in reversed(self.SCENE):
            draw_element(screen, self.state)
        screen.refresh()

    def initialize_screen(self):
        self.screen = curses.initscr()
        self.screen.keypad(True)
        self.screen.resize(*GAME_SIZE)
        self.screen.nodelay(True)
        environment.init(self.screen)
        hud.init(self.screen)

    def step(self, key):
        '''step takes the ord() of a character'''
        self.draw_scene(self.screen)
        if key == ord('q'):
            self.close()
        elif key == ord('p'):
            self.state['pdb'] = True
        else:
            update_state(key, self.state)
        self.state['frames'] += 1
        self.state['time'] += 1/FPS
        return self.state['score'], self.to_matrix(self.screen)

    def close(self):
        self.screen.clear()
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

    @staticmethod
    def to_matrix(screen):
        size = screen.getmaxyx()
        matrix = np.zeros(size, dtype=np.uint8)
        for y in range(size[0]):
            for x in range(size[1]):
                ch = int(screen.inch(y, x))
                if ch is not None:
                    matrix[y, x] = ch
        return matrix
