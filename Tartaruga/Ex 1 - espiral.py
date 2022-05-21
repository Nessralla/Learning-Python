#espiral - Desenha uma espiral quadrangular
import turtle

t = turtle.Pen()


for x in range(500):
    t.forward(x)
    t.left(91)


turtle.Screen().exitonclick()
