from .misc import get_terminal_size

#
# Definitions:
# - [X]_STICKY_TIME: amount of time a key press of action [X]
#                    sticks in the game
GAME_SIZE = get_terminal_size()
FPS = 60

# Car movement
SPEED_INCREMENT = 1
SPEED_DECREMENT = -1
BASE_SPEED = 5
MAX_SPEED = 99
SPEED_STICKY_TIME = 0.2
STEERING_STICKY_TIME = 0.5
STEERING_STEP = 0.06

# Environment
HORIZON = 0.5  # how far from top?
TRACK_SLOPE = 0.7  # x = x0 - slope*y
DEBRIS_SPEED_MULTIPLIER = 1.0
MAX_NUM_DEBRIS = 20

# Cars
MAX_NUM_CARS = 4

# Multiplayer
SERVER_HOST = 'localhost'
SERVER_PORT = 8087
IS_MULTIPLAYER_ENABLED = False
