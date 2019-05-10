# Umair Sayeed
# trapezoidArea, 25 October 2017, Chapter 1 Lab
# Calculates and prints the area of a trapezoid from the variables input by the user.
# Inputs: Top base, bottom base, height of trapezoid
# Output: Area of trapezoid.

topBase = eval(input("Enter the value of the top base of the trapezoid: "))
botBase = eval(input("Enter the value of the bottom base of the trapezoid: "))
height = eval(input("Enter the height of the trapezoid: "))
area = (1/2)*(topBase + botBase)*height
print("The area is:", area)