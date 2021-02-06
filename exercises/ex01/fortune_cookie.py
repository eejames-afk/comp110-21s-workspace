"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730273306"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Hello! Your fortune cookie says... ")
a: int = randint(1,4)
if a == 1:
    print( "Life is nothing without friendship!")
else: 
    if a == 2:
        print("Good things happen to people who care.")
    else:
        if a == 3:
            print("You are far greater than you can even imagine.")
        else:
            if a == 4:
                print("Love yourself as you would want others to love you!")
print("Now go fourth and live an amazing life!")
 

