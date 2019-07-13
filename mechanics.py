from config import SPEED_INCREMENT, SPEED_DECREMENT, BASE_SPEED, \
                   STEERING_STEP, MAX_NUM_CARS


def update_state(key, state):
    # respond to keys
    if key == ord('w'):
        state['speed'] += SPEED_INCREMENT
        state['speed'] = min(99, state['speed'])
    elif key == ord('s'):
        state['speed'] -= SPEED_DECREMENT
        state['speed'] = max(BASE_SPEED, state['speed'])
    elif key in {ord('d'), ord('a')}:
        direction = 1 if key == ord('d') else -1
        steer_tuple = state['car_steer_tuple']
        if steer_tuple is None or steer_tuple[1] != direction:
            state['car_steer_tuple'] = (state['time'], direction)
        # state['car_x'] = max(-1, state['car_x'])
    elif key == -1:
        pass

    if state['car_steer_tuple'] is not None:
        t0, direction = state['car_steer_tuple']
        state['car_x'] += direction*STEERING_STEP
        state['car_x'] = min(1, state['car_x'])
        state['car_x'] = max(-1, state['car_x'])
        if state['time'] - t0 > 0.5:
            state['car_steer_tuple'] = None

    # update other cars
    if len(state['cars']) < MAX_NUM_CARS:
        pass
        # TODO: game['cars'] ....
