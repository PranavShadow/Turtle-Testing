import turtle as t
import time

# Setup screen
screen = t.Screen()
screen.title("Smooth Ball Animation")
screen.bgcolor("black")
screen.setup(800, 600)

# Turn off auto-updates
screen.tracer(0)

# Create the ball
ball = t.Turtle()
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.goto(-300, 0)

# Ball movement speed
speed = 5

# Animate the ball
while ball.xcor() < 300:
    x = ball.xcor()
    ball.setx(x + speed)

    screen.update()  # Manually update screen
    time.sleep(0.01)  # Small delay for visible animation

screen.mainloop()
screen.bye()
screen.exitonclick()