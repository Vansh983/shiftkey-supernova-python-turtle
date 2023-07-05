
import turtle

pen = turtle.Turtle()
turtle.getscreen().bgcolor("yellow")

pen.shape("turtle")
pen.speed(100)
pen.color("red", "green")

# for i in range(5):
#     pen.forward(50)
#     pen.left(216)

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
        turtle.end_fill()
        
star(pen, 360)

turtle.mainloop()

