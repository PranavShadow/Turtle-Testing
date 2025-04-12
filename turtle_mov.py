import turtle

# --- Setup Screen ---
screen = turtle.Screen()
screen.title("All User Inputs Demo")
screen.bgcolor("black")
screen.setup(800, 600)

# --- Create a Turtle ---
player = turtle.Turtle()
player.shape("turtle")
player.color("lime")
player.penup()
player.goto(0, 0)

# --- Movement Step Size (set via input) ---
step = screen.numinput("Speed Setup", "Enter movement step size:", 20)

# --- Movement Functions ---
def move_up():
    player.sety(player.ycor() + step)

def move_down():
    player.sety(player.ycor() - step)

def move_left():
    player.setx(player.xcor() - step)

def move_right():
    player.setx(player.xcor() + step)

# --- Key Release Feedback ---
def say_stopped():
    print("Key released!")

# --- Mouse Click Handler ---
def teleport(x, y):
    player.goto(x, y)
    print(f"Teleported to ({x}, {y})")

# --- Text Input ---
name = screen.textinput("Welcome!", "What is your name?")
print(f"Hello, {name}! Use arrow keys to move your turtle.")

# --- Listen for Input ---
screen.listen()

# Key Presses
screen.onkeypress(move_up, "Up")      # Up Arrow
screen.onkey(move_down, "Down")       # Down Arrow
screen.onkeypress(move_left, "Left")  # Left Arrow
screen.onkey(move_right, "Right")     # Right Arrow

# Key Release
screen.onkeyrelease(say_stopped, "Up")

# Mouse Click (both onclick and onscreenclick are valid)
screen.onscreenclick(teleport)

# Mainloop to keep window open
screen.mainloop()
