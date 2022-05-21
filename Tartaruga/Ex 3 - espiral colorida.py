#espiral - Desenha uma espiral quadrangular colorida
import turtle

t = turtle.Pen()
colors = ["#7FFFD4","yellow","blue","green"]

for x in range(500):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)


turtle.Screen().exitonclick()
