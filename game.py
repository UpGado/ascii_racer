import curses
import environment
from environment import draw_background, draw_tracks, draw_statusbar, \
                    draw_debris, draw_horizon, draw_car
import hud
from hud import draw_hud
from mechanics import update_state
from config import GAME_SIZE, FPS, BASE_SPEED
from misc import limit_fps


SCENE = [draw_statusbar, draw_hud, draw_horizon, draw_tracks,
         draw_debris, draw_car, draw_background]
state = {'frames': 0,
         'time': 0.0,  # seconds
         'speed': BASE_SPEED,  # coord per frame
         'car_x': 0,  # range -1:1
         'debris': [],
         'cars': []}


@limit_fps(fps=FPS)
def draw_scene(screen):
    for draw_element in reversed(SCENE):
        draw_element(screen, state)
    screen.refresh()


def main(screen):
    screen.resize(*GAME_SIZE)
    screen.nodelay(True)
    environment.init(screen)
    hud.init(screen)
    while True:
        key = screen.getch()
        if key == ord('q'):
            break
        else:
            update_state(key, state)
        draw_scene(screen)
        state['frames'] += 1
        state['time'] += 1/FPS
    screen.clear()
    screen.getkey()


curses.wrapper(main)
