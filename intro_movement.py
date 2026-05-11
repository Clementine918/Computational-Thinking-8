import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("cardinal2",0,-200)
s2 = create_sprite("lucabella", 0, 200)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y+5)
        
def move_up2():
    x = s2.xcor()
    y = s2.ycor()
    s2.goto(x, y+5)

def move_down():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y-5)

def move_down2():
    x = s2.xcor()
    y = s2.ycor()
    s2.goto(x, y-5)
    
def move_left():
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x-5, y)

def move_left2():
    x = s2.xcor()
    y = s2.ycor() 
    s2.goto(x-5, y)
    
def move_right(): 
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x+5, y)

def move_right2(): 
    x = s2.xcor()
    y = s2.ycor() 
    s2.goto(x+5, y)

def draw():
    s1.pendown()

def draw2():
    s2.pendown()

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(draw2, "v")

window.onkeypress(move_up2, "Up")
window.onkeypress(move_down2, "Down")
window.onkeypress(move_left2, "Left")
window.onkeypress(move_right2, "Right")
window.onkeypress(draw, "c")

# Section 3: define other controls
def hide():
    s1.hideturtle()
    s2.hideturtle()
def show():
    s1.showturtle()
    s2.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")


# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()