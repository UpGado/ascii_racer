def draw_background(screen, state):
    background = ' '
    height, width = screen.getmaxyx()
    for y in range(height-1):
        for x in range(width-1):
            screen.addstr(y, x, background)


def draw_time(screen, state):
    screen.addstr(0, 0, str(state['time']))


def draw_tracks(screen, state):
    height, width = screen.getmaxyx()
    horizon = int(height/2)
    slope = 1.3
    left_track = [int(3*width/8), '▞', slope]
    right_track = [int(5*width/8), '▚', -slope]

    for (x0, character, step) in [left_track, right_track]:
        for y in range(horizon, height-1):
            screen.addstr(y, x0-int(y/step), character)
