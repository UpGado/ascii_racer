import time
from time import sleep


def limit_fps(fps):
    delay = 1/fps

    def run_fps_capped(func):
        def run(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            sleep_time = delay-elapsed_time
            if sleep_time >= 0:
                sleep(sleep_time)
        return run
    return run_fps_capped


def linear_interpolate(x1, y1, x2, y2, x3):
    y3 = y1 + (x3-x1)*(y2-y1)/(x2-x1)
    return y3


def make_in_range(x, x_min, x_max):
    x = min(x, x_max)
    x = max(x_min, x)
    return x


def rectangle_overlap(r1_y1, r1_y2, r1_x1, r1_x2,
                      r2_y1, r2_y2, r2_x1, r2_x2):
    if r2_x2 < r1_x1 or r2_x1 > r1_x2:
        return False
    elif r2_y2 < r1_y1 or r2_y1 > r1_y2:
        return False
    else:
        return True
