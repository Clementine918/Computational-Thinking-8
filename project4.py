from utils import *


# The goal of my game is to get $10,000 by making tacos and buying taco trucks which give you automatic money every second



# Section 1 - setup
# TODO - set a background using set_background()
set_background("tacotruck2")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
money = 0
taco_trucks = 1
taco_truck_price = 15
automatic_money = 0

# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -200,200)
m1.hideturtle()



# Section 2 - controls
# code to make and sell tacos when space key is pressed
def make_taco():
    #this makes it so when you press the space button it makes a taco in a random place on the screen and sells the taco to a customer earning you $1
    global money
    money += 1
    x = random.randint (-300,300)
    y = random.randint (-180,0)
    t1 = create_sprite ("taco", x, y)
    time.sleep(0.1)
    t1.hideturtle()
window.onkeypress(make_taco, "space")

# TODO - make a second control
def buy_truck ():
    global money, taco_trucks, taco_truck_price, automatic_money
    if money >= taco_truck_price:
        #this makes it so when you press the "t" key and you have enough money you get a taco truck. Taco trucks give you $5 automatically every second. Taco trucks cost $15 to buy the first time and the price goes up by $5 each time you by one.
        money -= taco_truck_price
        taco_trucks += 1
        taco_truck_price += 5
        automatic_money += 5
        x = random.randint (-300,300)
        y = random.randint (-180,0)
        ntt1 = create_sprite ("new_taco_truck", x, y)
        ntt1.write("+1 taco truck")
        time.sleep(0.5)
        ntt1.clear()
        ntt1.hideturtle()
window.onkeypress(buy_truck, "t")




# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    m1.clear()
    m1.write(f"Money: {money}      Taco Trucks: {taco_trucks}      Taco Truck Price: {taco_truck_price}      Money per Second: {automatic_money}")
    
    time.sleep(0.01)
    window.update()
    
    if i % 100 == 0:
        money += automatic_money


    if money >= 10000:
        m1.clear()
        m1.write("You win! You are now have $10,000!")
        time.sleep(10)
        turtle.exitonclick