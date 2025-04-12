import turtle
from PIL import ImageGrab

# --- Setup screen ---
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Color Collision Game")
screen.bgpic("level1.png")  # ← Your background map!

player = turtle.Turtle()
player.shape("turtle")
player.color("cyan")
player.penup()
player.goto(-380, 0)

step = 10

# --- Movement + Collision ---
def get_pixel_color(x, y):
    # Get screen coordinates (convert turtle to canvas pixels)
    canvas = screen.getcanvas()
    x_root = canvas.winfo_rootx() + x + 400  # offset from center
    y_root = canvas.winfo_rooty() + 300 - y  # inverted y-axis
    img = ImageGrab.grab(bbox=(x_root, y_root, x_root+1, y_root+1))
    return img.getpixel((0, 0))

def check_collision():
    x, y = player.xcor(), player.ycor()
    color = get_pixel_color(x, y)

    if color == (255, 0, 0):  # Red = Danger
        screen.textinput("Game Over", "You hit a danger zone!")
        screen.bye()
    elif color == (0, 255, 0):  # Green = Goal
        screen.textinput("Congrats!", "You reached the goal!")
        screen.bye()
    # else: safe path, do nothing

def move_up(): player.sety(player.ycor() + step); check_collision()
def move_down(): player.sety(player.ycor() - step); check_collision()
def move_left(): player.setx(player.xcor() - step); check_collision()
def move_right(): player.setx(player.xcor() + step); check_collision()

# --- Keybindings ---
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

screen.mainloop()
