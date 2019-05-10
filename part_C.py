# Umair Sayeed
# circleArea, 25 October 2017, Chapter 1 Lab
# Caculates the area of a circle using a radius value input by the user.
# Input: Number for radius.
# Output: Area of circle.

import math
radius = eval(input("Enter the radius of the circle: "))
area = math.pi*(radius**2)
print("The area of the circle is:", area)