import random
from config import HORIZON, TRACK_SLOPE, DEBRIS_SPEED_MULTIPLIER, \
                   MAX_NUM_DEBRIS
from misc import linear_interpolate


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
                      f"Num cars: {len(state['cars'])}"])
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


def spawn_debris(state):
    debris1 = [u'/\\',
               u'\\/']
    debris2 = ['*']
    debris3 = ['#']
    debris_list = [debris1, debris2, debris3]

    debris = random.choice(debris_list)

    y0 = horizon_y
    top_track_offset = int(horizon_y*TRACK_SLOPE) - 2
    if random.choice([True, False]):
        # left side
        x0 = random.randint(0, left_track[0]+top_track_offset)
    else:
        # right side
        x0 = random.randint(right_track[0]-top_track_offset, width-1)
    t0 = state['time']
    return debris, y0, x0, t0


def draw_debris(screen, state):
    DEBRIS_SPEED = state['speed']*DEBRIS_SPEED_MULTIPLIER

    for _ in range(MAX_NUM_DEBRIS - len(state['debris'])):
        state['debris'].append(spawn_debris(state))

    for debris_tuple in state['debris']:
        debris, y0, x0, t0 = debris_tuple
        step = 1 if x0 > width / 2 else -1
        y = y0 + int(DEBRIS_SPEED*(state['time']-t0))
        x = x0 + int((y-horizon_y)/step)
        if in_range(y+len(debris), x):
            for i, line in enumerate(debris):
                screen.addstr(y+i, x, line)
        else:
            state['debris'].remove(debris_tuple)


def draw_horizon(screen, state):
    for x in range(width):
        screen.addstr(horizon_y, x, '-')


def draw_car(screen, state):
    car = ['      _______________     ',
          r'     /               \    ',
          r'  ▉▉|      RrrrR      |▉▉  ',
          r'  ▉▉|  CA  R     R    |▉▉  ',
          r'  ▉▉ \_______________/ ▉▉   ']

    car_width = len(car[0])
    offset = 2 # offset from track
    x0 = left_track[0]+car_width/2+offset
    x1 = right_track[0]-car_width/2-offset
    car_center_x = linear_interpolate(-1, x0, 1, x1, state['car_x'])
    start_x = int(car_center_x - car_width / 2)
    for y, line in enumerate(reversed(car)):
        screen.addstr(height-1-y, start_x, line)
