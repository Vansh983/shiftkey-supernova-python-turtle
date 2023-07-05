
import turtle
import math

pen = turtle.Turtle()
pen.color("red", "yellow")
pen.speed(1000)

pen.shape("turtle")

pen.begin_fill()

for i in range(2200):
    pen.forward(math.sqrt(i))
    pen.left(i%180)

pen.end_fill()

turtle.mainloop()

