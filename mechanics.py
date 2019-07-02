def update_state(key, state):
    if key == ord('w'):
        state['speed'] += 10
        state['speed'] = min(99, state['speed'])
    elif key == ord('s'):
        state['speed'] -= 10
        state['speed'] = max(1, state['speed'])
    elif key == -1:
        pass
