import curses


def handle_key(key, state):
    if key == ord('w') and state['speed'] < 99:
        state['speed'] += 1
    elif key == ord('s') and state['speed'] > 1:
        state['speed'] -= 1
    pass
