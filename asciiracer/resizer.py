import os

class Resizer(object):

    def __init__(self):
        self.current_size = tuple(int(i) for i in os.popen('stty size', 'r').read().split())

    @property
    def game_size(self):
        return self.current_size
