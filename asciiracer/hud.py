from .ascii_factory import num2str


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


def draw_hud(screen, state):
    draw_speedmeter(screen, state)
