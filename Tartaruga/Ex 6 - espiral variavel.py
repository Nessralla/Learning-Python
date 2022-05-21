#espiral - Desenha uma espiral quadrangular colorida variável
import turtle

t = turtle.Pen()
colors = ["red","yellow","blue","green","purple","orange"]
turtle.bgcolor("black")

sides = 6

for x in range(200):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)


turtle.Screen().exitonclick()
