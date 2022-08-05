import json

from .ascii_factory import num2str
from .multiplayer.client import Client


def init(screen):
    global width, height
    height, width = screen.getmaxyx()


def draw_speedmeter(screen, state):
    margin_y, margin_x = 4, 4
    hud = ['▛▀▀▀▀▀▀▀▀▀▀▀▀▀▜',
           '▍             ▐',
           '▍             ▐',
           '▍             ▐',
           '▍             ▐',
           '▙▃▃▃▃▃▃▃▃▃▃▃▃▃▟',
           '▍     MPH     ▐',
           '▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀']
    hud_width = len(hud[0])
    speed = num2str(state['speed'])
    for l, (hud_line, speed_line) in enumerate(zip(hud[1:-1], speed)):
        hud[l+1] = hud_line[0] + speed_line + hud_line[-1]
    x0 = width - margin_x - hud_width
    y0 = margin_y
    for y, line in enumerate(hud):
        screen.addstr(y0+y, x0, line)


def draw_score_table(screen, state, client: Client):
    """
    Only available in multiplayer.
    :return:
    """
    y0 = 4
    x0 = width - 30
    screen.addstr(y0, x0, "SCORE TABLE:")
    for player_id, player_score in client.score_table.items():
        y0 += 1
        if int(player_id) == client.id:
            player_id = "You"
        score_row = f'{player_id}: {player_score}'
        screen.addstr(y0, x0, score_row)
    client.send_score_update_message(state["score"])


def draw_hud(screen, state):
    draw_speedmeter(screen, state)
