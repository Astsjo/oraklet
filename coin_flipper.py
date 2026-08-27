import random
import time

# User welcomed and inputs choice and the winning number (side) gets assigned
print(" ")
print("Flip a coin to answer your question or dispute!")
print(" ")
pick = input("Heads or Tails? (h/t) ")
num = (1, 2)
rnd_num = random.choice(num)
print(" ")

# Winner picker
if pick.lower() == "heads" or pick.lower() == "h":
    print("Your pick was heads...")
    winning_number = 1 # Winner = heads
elif pick.lower() == "tails" or pick.lower() == "t":
    print("Your pick was tails...")
    winning_number = 2 # Winner = tails
else:
    print("Error: Picker")
    
time.sleep(1)
print("The coin is flipping...")
time.sleep(3)
print("It's spinning on the table...")
time.sleep(3)
print(" ")

# Part that checks if you won or not
if winning_number == rnd_num:
    if winning_number == 1:
        print("It's heads, you win!")
    elif winning_number == 2:
        print("It's tails, you win!")
elif winning_number != rnd_num:
    if winning_number == 1:
        print("It's heads, you lose.")
    elif winning_number == 2:
        print("It's tails, you lose.")
else:
    print("Error: Checker")
print(" ")


# Set debug to True to see if the values are working correctly
debug = False
if debug == True:
    print(" ")
    print("Debug")
    print("Num:", num)
    print("Winning num: ", rnd_num)
    print("Pick:" , pick)