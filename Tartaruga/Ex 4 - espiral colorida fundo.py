#espiral - Desenha uma espiral quadrangular colorida e escolhe o fundo
import turtle

t = turtle.Pen()
colors = ["#7FFFD4","yellow","blue","green"]
turtle.bgcolor("black")

for x in range(200):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)


turtle.Screen().exitonclick()
