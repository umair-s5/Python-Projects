# Umair Sayeed
# Outputs the total cost of a meal including tip and tax.

meal = 53.48
tax = 0.07 # Percent in decimal form.
tip = 0.18 # Percent in decimal form.
total = meal + (meal*tip) + (meal*tax)
print("$"+str(total))
