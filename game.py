import curses
import environment
from environment import draw_background, draw_tracks, draw_time, \
                    draw_debris, draw_horizon, draw_car
from config import GAME_SIZE, FPS
from misc import limit_fps


SCENE = [draw_time, draw_horizon, draw_car,
         draw_debris, draw_tracks, draw_background]
state = {'time': 0,  # frame
         'speed': 1,  # coord per frame
         'debris': []}


@limit_fps(fps=FPS)
def draw_scene(screen):
    for draw_element in reversed(SCENE):
        draw_element(screen, state)
    screen.refresh()


def main(screen):
    screen.resize(*GAME_SIZE)
    environment.init(screen)
    while True:
        draw_scene(screen)
        state['time'] += 1
    screen.clear()
    screen.getkey()


curses.wrapper(main)
