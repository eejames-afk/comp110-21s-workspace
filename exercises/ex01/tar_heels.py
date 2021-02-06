"""An exercise in remainders and boolean logic."""

__author__ = "730273306"


# Begin your solution here...
b: int = int(input("Please, enter an int: "))
c: bool = (b%2 == 0)
d: bool = (b%7 == 0)
if c and d:   
    print("Tar Heels!")
else: 
    if d:
        print("Heels!")
    else:
        if c:
            print("Tar")
        else: 
             print("Carolina")