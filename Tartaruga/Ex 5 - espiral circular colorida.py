#espiral - Desenha uma espiral circular colorida
import turtle

t = turtle.Pen()
colors = ["red","yellow","blue","green"]
turtle.bgcolor("black")

for x in range(200):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)


turtle.Screen().exitonclick()
