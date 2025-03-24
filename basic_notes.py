import turtle as t


# Create turtle
chotu = t.Turtle()
t.bgcolor("black")

'''
Turtle has following Functions:
forward - fd
backward - bk
left - lt
right - rt
home 
clear
pen up - up
pen down - down
'''

'''
Turtle Shapes
arrow , blank , circle , classic , square , triangle , turtle
'''

chotu.color("red")
chotu.shapesize(5,5)
chotu.fd(50)
chotu.lt(50)
chotu.rt(100)
chotu.bk(50)
chotu.home()
chotu.clear()

# Keep the window open
t.done()
