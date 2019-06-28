import time
from time import sleep


def limit_fps(fps):
    delay = 1/fps

    def run_fps_capped(func):
        def run(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            elapsed_time = time.time() - start_time
            sleep(delay-elapsed_time)
        return run
    return run_fps_capped
