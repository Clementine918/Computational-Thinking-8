from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -250
y1 = 250
x2 = -250
y2 = 130
x3 = -250
y3 = -15
x4 = -250
y4 = -200
x5 = 250
y5 = 250

set_background("underwater3")
s5 = create_sprite("emma.gif",0,0)
s5.color ("white")

s5.write("Ladies and Gentleman!")
time.sleep(2)
s5.clear()
s5.write("Are you ready for some racing?!!")
time.sleep(2)
s5.clear()
# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice

s5.write("First up we have your reigning champion... The Fish!")
t1 = create_sprite("fish1",x1,y1)
time.sleep(4)
s5.clear()

s5.write("Next up we have the one and only... Whale!")
t2 = create_sprite("whale1",x2,y2)
time.sleep(3)
s5.clear()

s5.write("He has competed for years but has yet to win a medal")
time.sleep(4)
s5.clear()

s5.write("Now we have the rookie...")
time.sleep(4)
s5.clear()
s5.write("You may recognize him from some of his movies...")
time.sleep(4)
s5.clear()

t3 = create_sprite("shark1",x3,y3)
s5.write("The Shark from Nemo!!")
time.sleep(4)
s5.clear()

s5.write("And last but not least we have...")
time.sleep(3)
s5.clear()

s5.write("Competing for the first time in this sport....")
time.sleep(4)
s5.clear()

s5.write("The GOAT...")
time.sleep(4)
s5.clear()
t4 = create_sprite("lebron(1)",x4,y4)
s5.write("LeBron James!!")
time.sleep(4)
s5.clear()

s5.goto(x5,y5)
window.update()

s5.write("On your marks...")
time.sleep(3)
s5.clear()

s5.write("Get set...")
time.sleep(3)
s5.clear()

s5.write("Go...")
time.sleep(2)
s5.clear()

# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower

# Sprite 2 will be slower because the numbers you can get are lower
# Sprite 3 will be the fastest because the lowest number you can get is pretty high and the biggest number you can get is higher then the rest.

for i in range(40):
    x1 += random.randint(5,15)
    x2 += random.randint(0,9)
    x3 += random.randint(8,18)
    x4 += random.randint(0,18)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4


if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("The fish wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("The whale wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    s5.write("The shark wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    s5.write("Lebron wins!")



turtle.exitonclick()