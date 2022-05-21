# espiral circular

import turtle

t = turtle.Pen()
t.pencolor("red")
for x in range(100):
    t.circle(x)
    t.left(91)


turtle.Screen().exitonclick()