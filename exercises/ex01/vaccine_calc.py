"""A vaccination calculator."""

__author__ = "730273306"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
print("Please input the correct information for best accuracy!")
""" My variable"""
Pop: int = int(input("Population: "))
dose_Admin: int = int(input("Doses administered: "))
dose_Per_Day: int = int(input("Does per day: "))
target: int = int(input("Target percent vaccinated: "))
if target > 100: 
    print("Unable to compute :/")
else:
    Total_doses: int = (Pop * 2)
    Target_number: int = round(Total_doses* target/ 100)
    Days_needed: int = round((Target_number-dose_Admin)/dose_Per_Day)
    today: datetime = datetime.today()
    One_Day: timedelta = timedelta(Days_needed)
    future: datetime = today + One_Day 
    Final_day: str = future.strftime("%B %d, %y")
    print("We will reach " + str(target) + "%" +" vaccincation in " + str(Days_needed) + " days, which falls on " + Final_day + ".")