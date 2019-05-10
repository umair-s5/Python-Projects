# Umair Sayeed
# tempConversion, 25 October 2017, Chapter 1 Lab
# Gets temperature in Fahrenheit from the user and prints it in Celsius.
# Inputs: Number from user
# Outputs: Conversion of user's input to Celsius.

tempFahrenheit = eval(input("Enter temperature in Fahrenheit: "))
conversionToCelsius = (tempFahrenheit - 32)*(5/9)
print("The temperature in Celsius: ", conversionToCelsius)