import turtle

# --- Setup screen ---
screen = turtle.Screen()
screen.title("Safe Path Game")
screen.bgcolor("black")
screen.setup(800, 600)

# --- Player ---
player = turtle.Turtle()
player.shape("turtle")
player.color("cyan")
player.penup()
player.goto(-350, 0)

# --- Goal Area (Green) ---
goal = turtle.Turtle()
goal.shape("square")
goal.shapesize(stretch_wid=5, stretch_len=2)
goal.color("green")
goal.penup()
goal.goto(350, 0)

# --- Danger Zone (Red) ---
danger = turtle.Turtle()
danger.shape("square")
danger.shapesize(stretch_wid=10, stretch_len=3)
danger.color("red")
danger.penup()
danger.goto(0, 0)

# --- Helper Functions ---
step = 20

def is_in_zone(turt, zone, w, h):
    """Check if turtle is inside a rectangular area"""
    x1, y1 = zone.xcor() - w, zone.ycor() - h
    x2, y2 = zone.xcor() + w, zone.ycor() + h
    x, y = turt.xcor(), turt.ycor()
    return x1 <= x <= x2 and y1 <= y <= y2

def reset_game():
    player.goto(-350, 0)

def game_over():
    screen.textinput("Game Over", "Oops! You stepped in the danger zone!")
    ask_restart()

def game_won():
    screen.textinput("Congratulations!", "You reached the goal! 🎉")
    ask_restart()

def ask_restart():
    choice = screen.textinput("Play Again?", "Type 'yes' to restart, or anything else to quit:")
    if choice and choice.lower() == "yes":
        reset_game()
    else:
        screen.bye()

# --- Movement Functions ---
def move_up():
    player.sety(player.ycor() + step)
    check_state()

def move_down():
    player.sety(player.ycor() - step)
    check_state()

def move_left():
    player.setx(player.xcor() - step)
    check_state()

def move_right():
    player.setx(player.xcor() + step)
    check_state()

def check_state():
    if is_in_zone(player, danger, 60, 100):
        game_over()
    elif is_in_zone(player, goal, 40, 50):
        game_won()

# --- Key Bindings ---
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# --- Game Loop ---
screen.mainloop()
