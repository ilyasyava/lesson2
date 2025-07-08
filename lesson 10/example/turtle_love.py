import turtle
import math
from random import randint

def xt(t):
    return 16 * math.sin(t) ** 3
def yt(t):
    return 13 * math.cos(t)     - \
            5 * math.cos(2 * t) - \
            2 * math.cos(3 * t) - \
                math.cos(4 * t)

turtle.color("pink")
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)
turtle.hideturtle()
turtle.Screen().tracer(2) # чтобы рисовало побыстрее

t = turtle.Turtle()
t.hideturtle()
t.speed(500)
for i in range(1000):
    t.goto((xt(i) * 20, yt(i) * 20))
    t.pencolor((255 - i) % 255, i % 255, (255 + i) // 2 % 255)
    t.home()
    turtle.clear()
    turtle.write("love love", False, align="center",font = ( "Verdana", randint(20,70), "normal" ))
    

turtle.update()
turtle.mainloop()
turtle.done()