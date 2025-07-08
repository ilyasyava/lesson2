from turtle import *
import math
import turtle

t = Turtle()
t.speed(0)
t.color("red")

def f1(n):
    x = 16*math.sin(n)**3
    y = 13*math.cos(n)-5 * math.cos(2*n) - \
            2*math.cos(3*n) - math.cos(4*n)
    return x, y

t.pu()
for i in range(1, 15):
    t.goto(0, 0)
    t.pd()
    for n in range(0, 65, 2):
        x, y = f1(n/10)
        t.goto(x*i, y*i)
    t.pu()

exitonclick()
