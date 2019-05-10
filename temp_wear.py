#Umair Sayeed
#Get's input from user about temperature and uses input to suggest outfit.

temp = eval(input("Enter the outside temperature in degree Fahrenheit: "))

if temp > 90:
    print("Whoa, it's boiling! Wear sunscreen!")
elif temp >= 80:
    print("It's getting hot! Dont forget some sunglasses.")
elif temp < 80 and temp >= 32:
    print("A perfect day. Shorts and a tee.")
elif temp < 32:
    print("Brrr, you need a coat!")
