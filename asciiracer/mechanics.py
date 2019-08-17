from .config import SPEED_INCREMENT, SPEED_DECREMENT, BASE_SPEED, \
                   STEERING_STEP, MAX_SPEED, \
                   STEERING_STICKY_TIME, SPEED_STICKY_TIME
from .misc import make_in_range, rectangle_overlap


def update_state(key, state):
    steer_tuple = state['car_steer_tuple']
    speed_tuple = state['car_speed_tuple']
    # respond to keys
    if key in {ord('w'), ord('s')}:
        direction = 1 if key == ord('w') else -1
        if speed_tuple is None or speed_tuple[1] != direction:
            state['car_speed_tuple'] = (state['time'], direction)
    elif key in {ord('d'), ord('a')}:
        direction = 1 if key == ord('d') else -1
        if steer_tuple is None or steer_tuple[1] != direction:
            state['car_steer_tuple'] = (state['time'], direction)
    elif key == -1:
        # no key pressed
        pass

    if steer_tuple is not None:
        update_steering(state, steer_tuple)

    if speed_tuple is not None:
        update_speed(state, speed_tuple)

    collect_money(state)


def collect_money(state):
    c_ys, c_xs = state['car'].current_coords
    for money_object in state['money']:
        ys, xs = money_object.current_coords
        if rectangle_overlap(*c_ys, *c_xs, *ys, *xs):
            (_, score), *args = money_object.attrs
            state['score'] += score
            state['money'].remove(money_object)


def update_steering(state, steer_tuple):
    t0, direction = steer_tuple
    elapsed_time = state['time'] - t0
    if elapsed_time > STEERING_STICKY_TIME:
        state['car_steer_tuple'] = None
    else:
        new_car_x = state['car_x'] + direction*STEERING_STEP
        state['car_x'] = make_in_range(new_car_x, -1, 1)


def update_speed(state, speed_tuple):
    t0, direction = speed_tuple
    if state['time'] - t0 > SPEED_STICKY_TIME:
        state['car_speed_tuple'] = None
    else:
        change = SPEED_INCREMENT if direction == 1 \
                                    else SPEED_DECREMENT
        new_car_speed = state['speed'] + change
        state['speed'] = make_in_range(new_car_speed,
                                       BASE_SPEED, MAX_SPEED)
