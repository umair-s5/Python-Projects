# Umair Sayeed
# quiz, 25 October 2017, Chapter 3 Lab
# A five question quiz for the user that prints the final score.
# Inputs: A-D, numbers, true or false options from user.
# Outputs: Appropriate game responses based on inputs. Correct or incorrect and final score.


import math
print("\nLet's take a quiz!")
points = 0

q1 = eval(input("\n1. What is 6^2? "))
if q1 == 36:
    print("That is correct!")
    points += 1
else:
    print("Sorry. That is incorrect.")

q2 = eval(input("\n2. What is 10^2? "))
if q2 == 100:
    print("That is correct!")
    points += 1
else:
    print("Sorry. That is incorrect.")

a = "Ada Lovelace"
b = "Bill Gates"
c = "Steve Jobs"
d = "Professor Mercuri"
print("\na) "+a, "\nb) "+b, "\nc) "+c, "\nd) "+d)
q3 = input("\n3. Enter the letter corresponding to the first programmer: ")
if q3 == "a":
    print("That is correct!")
    points += 1
else:
    print("Sorry. That is incorrect.")

q4 = eval(input("\n4. What is the square root of 81? "))
if q4 == math.sqrt(81):
    print("That is correct!")
    points += 1
else:
    print("Sorry. That is incorrect.")

q5 = eval(input("\n5. What is the derivative of 2x? "))
if q5 == 2:
    print("That is correct!")
    points += 1
else:
    print("Sorry. That is incorrect.")

print("\nYou have completed the quiz. Your score: "+str(points)+"/5.", "\nThat is "+str(int((points*100)/5))+"%.")
