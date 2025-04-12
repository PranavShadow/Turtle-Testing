import turtle as t

screen = t.Screen()
screen.bgcolor("black")
screen.title("Tracer Demo")
screen.setup(800, 800)

pen = t.Turtle()
pen.color("cyan")
pen.speed(2000)
pen.pensize(1)


screen.tracer(0)

# Draw a spirograph-style pattern
for i in range(183):
    pen.forward(100)
    pen.right(45)
    pen.forward(20)
    pen.left(90)
    pen.forward(20)
    pen.right(45)
    pen.setheading(i * 2)  # Slowly rotating
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()

# 🧠 Manually update once it's all drawn
# screen.update()
screen.mainloop()
