# All digits are 6 characters wide and 4 high
nums = {
    0:     ['██████',
            '█    █',
            '█    █',
            '██████'],

    1:     ['   █  ',
            '   █  ',
            '   █  ',
            '   ▉  '],

    2:     ['██████',
            '     █',
            '██████',
            '█▄▄▄▄▄'],

    3:     ['██████',
            '     █',
            '▀▀▀▀▀█',
            '▄▄▄▄▄█'],

    4:     ['█    █',
            '█    █',
            '█▄▄▄▄█',
            '     █'],

    5:     ['██████',
            '█     ',
            '▀▀▀▀▀█',
            '▄▄▄▄▄█'],

    6:     ['█▀▀▀▀█',
            '█     ',
            '█▀▀▀▀█',
            '█▄▄▄▄█'],

    7:     ['██████',
            '   ▗█▛',
            '  ▟█▛ ',
            '▄██▛  '],

    8:     ['█▀▀▀▀█',
            '█    █',
            '█▀▀▀▀█',
            '█▄▄▄▄█'],

    9:     ['█▀▀▀▀█',
            '█▄▄▄▄█',
            '     █',
            '     █'],
}


def num2str(num):
    assert(0 <= num and num <= 99)
    r_digit = num % 10
    l_digit = (num - r_digit)/10
    l_digit, r_digit = [nums[_] for _ in [l_digit, r_digit]]
    string = []
    for l_line, r_line in zip(l_digit, r_digit):
        string.append(' '.join([l_line, r_line]))
    return string
