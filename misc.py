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
            else:
                raise RuntimeError('cannot keep up with target FPS')
        return run
    return run_fps_capped


def linear_interpolate(x1, y1, x2, y2, x3):
    y3 = y1 + (x3-x1)*(y2-y1)/(x2-x1)
    return y3
