# Umair Sayeed
# camel, 25 October 2017, Chapter 4 Lab
# User picks choices A-E or Q to try and escape from natives after their stolen camel.
# Inputs: A-E or Q
# Outputs: Appropriate game responses based on inputs.

import random
print("\nWelcome to Camel!"
      "\nYou have stolen a camel to make your way across the great Gobi desert."
      "\nThe natives want their camel back and are chasing you down!"
      "\nSurvive your desert trek and outrun the natives.")

done = False
miles = 0
fatigue = 0
thirst = 0
nativesMiles = -20
drinks = 5
while not done:
    oasis = random.randrange(0, 21)
    if oasis == 0:
        print("\nYou've found an oasis!")
        drinks = 5
        thirst = 0
        fatigue = 0
    print("\nA. Drink from your canteen."
          "\nB. Ahead moderate speed."
          "\nC. Ahead full speed."
          "\nD. Stop for the night."
          "\nE. Status check."
          "\nQ. Quit.")
    choice = input("\nChoose wisely: ")
    if choice.lower() == "q":
        done = True
        print("\nYou've quit the chase.")
    elif choice.lower() == "e":
        print("\nMiles traveled:", miles, "."
              "\nDrinks remaining:", drinks, "."
              "\nThe natives are "+str((miles-nativesMiles))+" miles behind you.")
    elif choice.lower() == "d":
        fatigue = 0
        nativesMiles += random.randrange(7, 15)
        print("\nA rested camel is a happy camel, but the natives moved closer!")
    elif choice.lower() == "c":
        miles += random.randrange(10, 21)
        print("\nYou've now traveled a total of "+str(miles)+" miles.")
        thirst += 1
        fatigue += random.randrange(1, 4)
        nativesMiles += random.randrange(7, 15)
    elif choice.lower() == "b":
        miles += random.randrange(5, 13)
        print("\nYou've now traveled a total of " + str(miles) + " miles.")
        thirst += 1
        fatigue += 1
        nativesMiles += random.randrange(7, 15)
    elif choice.lower() == "a":
        if drinks > 0:
            drinks -= 1
            thirst = 0
            print("\nThat was refreshing! You have "+str(drinks)+" drinks left.")
        else:
            print("\nYou're all out of drinks!")
    if thirst > 4:
        print("\nYou're thirsty.")
    elif thirst > 6:
        print("\nYou've died of thirst, and the natives got their camel back!")
        done = True
    if not done:
        if fatigue > 5:
            print("\nYour stolen camel is getting tired!")
        elif fatigue > 8:
            print("\nYour stolen camel died.")
            done = True
        if miles >= 200:
            print("\nYou won!")
            done = True
    if nativesMiles >= miles:
        print("\nThe natives caught you and took their beloved camel back.")
        done = True
    elif miles - nativesMiles < 15:
        print("\nThe natives are close!")



