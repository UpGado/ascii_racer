import random


def init(screen):
    global width, height, horizon, left_track, right_track, slope
    height, width = screen.getmaxyx()
    horizon = int(height/2)
    slope = 0.7  # x = x0 - slope*y
    left_track = (int(3*width/8), '▞', -slope)
    right_track = (int(5*width/8), '▚', slope)


def in_range(y, x):
    return 0 <= y and y <= height - 1 and \
           0 <= x and x <= width - 1


def draw_background(screen, state):
    global width, height
    background = ' '
    for y in range(height):
        for x in range(width-1):
            screen.addstr(y, x, background)


def draw_time(screen, state):
    screen.addstr(0, 0, str(state['time']))


def draw_tracks(screen, state):
    global left_track, right_track, height, horizon
    for (x0, character, step) in [left_track, right_track]:
        for y in range(horizon, height):
            screen.addstr(y, x0+int(step*y), character)


def spawn_debris(state):
    debris1 = [u'/\\',
               u'\\/']
    debris2 = ['*']
    debris3 = ['#']
    debris_list = [debris1, debris2, debris3]

    debris = random.choice(debris_list)

    y0 = horizon
    if random.choice([True, False]):
        # left side
        x0 = random.randint(0, left_track[0])
    else:
        x0 = random.randint(right_track[0], width-1)
    t0 = state['time']
    return debris, y0, x0, t0


def draw_debris(screen, state):
    NUM_DEBRIS = 20
    DEBRIS_SPEED = state['speed']/30

    for _ in range(NUM_DEBRIS - len(state['debris'])):
        state['debris'].append(spawn_debris(state))

    for debris_tuple in state['debris']:
        debris, y0, x0, t0 = debris_tuple
        step = 1 if x0 > width / 2 else -1
        y = y0 + int(DEBRIS_SPEED*(state['time']-t0))
        x = x0 + int(y/step)
        if in_range(y+len(debris), x):
            for i, line in enumerate(debris):
                screen.addstr(y+i, x, line)
        else:
            state['debris'].remove(debris_tuple)


def draw_horizon(screen, state):
    for x in range(width):
        screen.addstr(horizon, x, '-')


def draw_car(screen, state):
    car = ['     ____________________________________     ',
          u'    /                a                   \\    ',
          u'    |      CCCCC    A A     R R R        |    ',
          u'    |      C       AaaaA    R    r       |    ',
          u'  ▉▉|      C      A     A   RrrrR        |▉▉  ',
          u'  ▉▉|      CCCCC A       A  R     R      |▉▉  ',
          u'  ▉▉ \\__________________________________/ ▉▉   ']
    car_width = len(car[0])
    start_x = int(width/2) - int(car_width/2)
    for y, line in enumerate(reversed(car)):
        screen.addstr(height-1-y, start_x, line)
