import turtle as t

# Create a screen and set dark mode
screen = t.Screen()
screen.bgcolor("black")
screen.title("Dark Theme Turtle Window")
screen.setup(1000, 508)

# Set background image (adjust the path as necessary)
screen.bgpic("screen.gif")

# Create a turtle
chotu = t.Turtle()
chotu.color("white")
chotu.pensize(3)
chotu.speed(3)
chotu.shape("square")

# Turtle movements
chotu.fd(100)
chotu.lt(90)
chotu.fd(100)
chotu.rt(90)
chotu.bk(100)
chotu.rt(90)
chotu.fd(100)

# Keep the window open
screen.mainloop()
