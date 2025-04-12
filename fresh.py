import turtle as t

screen = t.Screen()
screen.title("Fresh Game")
screen.setup(800, 800)
screen.bgcolor("black")
screen.delay(15)

pol = t.Turtle()
pol.pensize(3)
pol.shape("square")
pol.speed(2)

# ✅ Start at the center
pol.penup()
pol.goto(-50, 250)
pol.pendown()
pol.color("white")

# Drawing pattern with center at screen center
for i in range(1, 50):
    if i < 10:
        pol.color("red")
        
    elif i < 30:
        pol.color("green")
        screen.clear()
    else:
        pol.color("yellow")

    pol.fd(100)
    pol.lt(20)
    pol.bk(200)  # This makes it rotate with a center behind it

screen.mainloop()
