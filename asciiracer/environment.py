import random
from collections import namedtuple
from .config import HORIZON, TRACK_SLOPE, DEBRIS_SPEED_MULTIPLIER, \
                   MAX_NUM_DEBRIS
from .misc import linear_interpolate

Sprite = namedtuple('Sprite', ['attrs', 'current_coords'])


def init(screen):
    global width, height, horizon_y, left_track, right_track
    height, width = screen.getmaxyx()
    horizon_y = int(HORIZON*height)
    left_track = (int(3*width/16), '▞', TRACK_SLOPE)
    right_track = (int(13*width/16), '▚', -TRACK_SLOPE)


def in_range(y, x):
    return 0 <= y and y <= height - 1 and \
           0 <= x and x <= width - 1


def draw_background(screen, state):
    global width, height
    background = ' '
    for y in range(height):
        for x in range(width-1):
            screen.addstr(y, x, background)


def draw_statusbar(screen, state):
    status = '|'.join([f"Time: {state['time']:.2f} seconds",
                      f"Score: {state['score']}"])
    screen.addstr(0, 0, status)


def draw_tracks(screen, state):
    global left_track, right_track, height, horizon_y
    for (x0, character, slope) in [left_track, right_track]:
        for y in range(horizon_y, height):
            x = x0+int(slope*(height-1-y))
            if y <= horizon_y + 5:
                c = character
                character = '$'
            screen.addstr(y, x, character)
            if y <= horizon_y + 5:
                character = c


def spawn_debris(state, x_ranges):
    debris_list = [[u'/\\',
                    u'\\/'],
                   ['*'],
                   ['#']]
    return spawn_sprite(state, x_ranges, debris_list, DEBRIS_SPEED_MULTIPLIER)


def spawn_money(state, x_ranges):
    def martini_glass(ch):
        return [r'╲___╱',
                   f" ╲{ch}╱ ",
                   r'  ╿   ',
                   r'  ┴  ']
    money_list = [(martini_glass('V'), 10),
                  (martini_glass('$'), 1),
                  (martini_glass('G'), 5),
                  (martini_glass('B'), -20),
                  (martini_glass('B'), -20),
                  (martini_glass('B'), -20)]
    return spawn_sprite(state, x_ranges, money_list, 1)


def spawn_sprite(state, x_ranges, sprites, speed_multiplier):
    sprite_design = random.choice(sprites)

    y0 = horizon_y
    x_range = random.choice(x_ranges)
    x0 = random.randint(*x_range)
    t0 = state['time']
    new_sprite = Sprite((sprite_design, y0, x0, t0, speed_multiplier),
                        None)
    return new_sprite

def draw_debris(screen, state):
    top_track_offset = int(horizon_y*TRACK_SLOPE) - 2
    x_ranges = [(0, left_track[0]+top_track_offset),
                (right_track[0]-top_track_offset, width-1)]
    draw_sprite(screen, state, 'debris', MAX_NUM_DEBRIS, x_ranges, spawn_debris)


def draw_money(screen, state):
    top_track_offset = int(horizon_y*TRACK_SLOPE) + 2
    x_ranges = [(left_track[0]+top_track_offset,
                right_track[0]-top_track_offset)]
    draw_sprite(screen, state, 'money', 1, x_ranges, spawn_money)


def draw_sprite(screen, state, key, max_num, x_ranges, spawn_func):
    num_missing_sprites = max_num - len(state[key])
    if num_missing_sprites > 0:
        for _ in range(num_missing_sprites):
            state[key].append(spawn_func(state, x_ranges))
    draw_parallax(state[key], screen, state)


def draw_parallax(sprites, screen, state):
    for s, sprite_tuple in enumerate(sprites):
        sprite, y0, x0, t0, speed_multiplier = sprite_tuple.attrs
        if type(sprite) is tuple:
            sprite_design = sprite[0]
        else:
            sprite_design = sprite
        speed = state['speed']*speed_multiplier
        step = parallax_slope(x0)
        y = y0 + int(speed*(state['time']-t0))
        x = x0 + int((y0-y)*step)
        if in_range(y+len(sprite_design), x):
            for i, line in enumerate(sprite_design):
                screen.addstr(y+i, x, line)
            sprites[s] = Sprite((sprite, y0, x0, t0, speed_multiplier),
                                ((y, y+i), (x, x+len(line))))
        else:
            sprites.remove(sprite_tuple)


def draw_horizon(screen, state):
    for x in range(width):
        screen.addstr(horizon_y, x, '-')


def draw_car(screen, state):
    car = ['      ____________     ',
          r'     /            \    ',
          r'  ▉▉|      RrrrR   |▉▉  ',
          r'  ▉▉|  CA  R     R |▉▉  ',
          r'  ▉▉ \____________/ ▉▉   ']

    car_width = len(car[0])
    offset = 2  # offset from track
    x0 = left_track[0]+car_width/2+offset
    x1 = right_track[0]-car_width/2-offset
    car_center_x = linear_interpolate(-1, x0, 1, x1, state['car_x'])
    start_x = int(car_center_x - car_width / 2)
    for offset, line in enumerate(reversed(car)):
        y = height-1-offset
        x = start_x + len(line)
        screen.addstr(y, start_x, line)
    y_coords = (height-1-offset, height-1)
    x_coords = (start_x, x)
    state['car'] = Sprite(None, (y_coords, x_coords))


def parallax_slope(x0):
    # using top end of tracks as reference
    top_track_offset = int(horizon_y*TRACK_SLOPE)
    x_range = (left_track[0]+top_track_offset, right_track[0]-top_track_offset)
    return linear_interpolate(x_range[0], TRACK_SLOPE, x_range[1], -TRACK_SLOPE, x0)
