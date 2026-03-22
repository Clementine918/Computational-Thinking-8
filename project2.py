
rory_points = 0
lorelai_points = 0
lane_points = 0
paris_points = 0

print("")
print ("Gilmore Girls Personality Quiz: Which character do you have the most in common with?")
input ("Press enter to start")
print ("")

answer1 = input("Which of these are your favorite colors? A - light pinks, blues, yellows, B - Pink, Dark Purple, C - red, purple, black, D - Bright, sharp reds and oranges ")
if answer1 == "B" or answer1 == "b":
    lorelai_points += 1
elif answer1 == "A" or answer1 == "a":
    rory_points += 1
elif answer1 == "C"or answer1 == "c":
    lane_points += 1
elif answer1 == "D" or answer1 == "d":
    paris_points += 1

print("")

answer2 = input("Which of these are your favorite classes at school? A - English, Philosophy, B - Entrepreneurship or Lunch, C - Music classes, or other visual art, D - Science, Debate, Mock trial type classes ")
if answer2 =="A" or answer2 == "a":
    rory_points += 2
elif answer2 == "B" or answer2 == "b":
    lorelai_points += 2
elif answer2 == "C" or answer2 == "c":
    lane_points += 2
elif answer2 == "D" or answer2 == "d":
    paris_points += 2
else:
    print("chose A, B, C, or D")

print("")

answer3 = input("Which of these artists or genres of music do you like best? A - 80s music, indie-rock, classic pop like The Shins, Sonic Youth, Belle and Sebastian, B - 80s pop and Rock like The Bangles, Bowie, The Go-Go’s, Madonna, C - Rock, punk and indie bands like The Ramones, Blondie, David Bowie, D - Mostly intense classical music with some fun bands like the Bangles. ")
if answer3 == "A" or answer3 == "a":
    rory_points += 1
elif answer3 == "B" or answer3 == "b":
    lorelai_points += 2
elif answer3 == "C" or answer3 == "c":
    lane_points += 2
elif answer3 == "D" or answer3 == "d":
    paris_points += 3

print("")

answer4 = input ("Favorite book genre? A - Classics like Anna Karenina, Pride and Prejudice, The Great Gatsby, B - Books about music like just kids or girls to the front, C - Long intense books like The Art of War by Sun Tzu or Post Office by Charles Bukowski, D - some classics but also some pop culture like To Kill a Mockingbird, The Bell Jar, The Dirt ")
if answer4 == "A" or answer4 == "a":
    rory_points += 2
elif answer4 == "B" or answer4 == "b":
    lane_points += 2
elif answer4 == "C" or answer4 == "c":
    paris_points += 2
elif answer4 == "D" or answer4 == "d":
    lorelai_points += 2

print("")

answer5 = input ("Which type of food do you eat most often? A - Takeout, junk food, and sugary food, B - Fast food is a favorite, especially fries and pizza, but parents force you to eat healthy, C - usually healthy but quick, D - a mix of healthy and unhealthy food, depending on what you feel like eating ")
if answer5 == "A" or answer5 == "a":
    rory_points += 2
    lorelai_points += 2
elif answer5 == "B" or answer5 == "b":
    lane_points += 1
elif answer5 == "C" or answer5 == "c":
    paris_points += 1
elif answer5 == "D" or answer5 == "d":
    paris_points += 1

print("")
input("Now press enter to see which character you have the most in common with")
print("")
print (f"You have {rory_points} rory points, {lane_points} lane points, {paris_points} paris points and {lorelai_points} lorelai points.")
if rory_points > lane_points and rory_points > paris_points and rory_points > lorelai_points:
    print("You have most in common with Rory! You love to read, listen to music, and eat junk food.")
elif lane_points > rory_points and lane_points > paris_points and lane_points > lorelai_points:
    print (" You have most in common with Lane! You love to listen to and make music, love pop culture and have a strong independence.")
elif paris_points > rory_points and paris_points > lane_points and paris_points > lorelai_points:
    print ("You have the most in common with Paris! You are strong, intense, and academically focused, and you love to win.")
elif lorelai_points > rory_points and lorelai_points > lane_points and lorelai_points > paris_points:
    print ("You are most like Lorelai! You have a witty, fast paced personality and love coffee, eating junk food, fashion, and entertainment.")

print ("")
print ("Thank you for playing!")