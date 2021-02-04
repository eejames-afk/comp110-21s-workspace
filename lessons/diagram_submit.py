age: int = int(input("How old are you?"))
year: int = int(input("What year is this?"))
age_in_2041: int = 2041 - year + age
print("In 2041,"+ " " + str(age_in_2041) + "you'll be ")

age = age + 1
year = year + 1
print("In " + str(year) + ", you'll be " + str(age))

