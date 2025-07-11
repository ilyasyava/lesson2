# '''
# Добавить несколько черепах
#     - или сразу
#     * или в течении игры по одной через определенное количество кликов
#     - на каждой забиндить клик через одну и туже функцию cath
# '''
import turtle
import random

from turtle import Turtle, Screen
from random import choice

COLORS = ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'cyan', 'black']


def catch(x, y):
    print("Черепаха поймана!", x, y)


def add_turtle():
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(choice(COLORS))
    new_turtle.goto(0, 0)
    new_turtle.onclick(catch)

    new_turtle.setheading(random.randint(0, 360))
    return new_turtle


def on_screen_click(x, y):
    global click_count
    click_count += 1
    print("Клики:", click_count)

    if click_count % 4 == 0:
        new_t = add_turtle()
        all_turtles.append(new_t)


def move_turtles():
    for t in all_turtles:
        t.forward(3)
    screen.ontimer(move_turtles, 50)


def main():
    global click_count, all_turtles, screen
    click_count = 0
    all_turtles = []

    screen = turtle.Screen()
    screen.title("Игра с черепахами")
    screen.setup(width=600, height=600)

    first_turtle = add_turtle()
    all_turtles.append(first_turtle)

    screen.onscreenclick(on_screen_click)

    move_turtles()

    screen.mainloop()


main()