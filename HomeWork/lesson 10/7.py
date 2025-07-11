# """
# **
# задание для самых  любопытных ))
#
# сделать анимацию снежинок елки с выводом в консоль
# образец и описание в файле example\elka_animate.py
# """
from random import Random
import time
import os

random = Random()


def new_sky_line(columns):
    return ''.join(random.choice('  ..  ''  ""  **') for _ in range(columns))


def sky(rows, columns):
    all_sky = [new_sky_line(columns) for _ in range(rows)]
    wind = 0


    def inner_sky_down_right():
        nonlocal all_sky, wind
        all_sky.pop(-1)
        all_sky.insert(0, new_sky_line(columns))
        wind = int(wind / 2 + random.randint(-1, 2))
        all_sky = [line[wind:] + line[:wind] for line in all_sky]
        return '\n'.join(all_sky)
    return inner_sky_down_right



def add_tree(all_sky: list, tree_height):
    for i in range(tree_height):
        all_sky[i] = (
            all_sky[i][: tree_height - i - 1]
            + "▲" * (i * 2 + 1)
            + all_sky[i][tree_height + i + 1 :]
        )
    return all_sky


def print_rastr(rastr_list):
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in rastr_list:
        print(line)

sky_gen = sky(30, 80)

while True:
    raw_sky = sky_gen().split('\n')
    sky_with_tree = add_tree(raw_sky, 30)
    print_rastr(sky_with_tree)
    time.sleep(0.1)