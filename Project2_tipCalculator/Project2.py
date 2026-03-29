print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
toatalTip = (bill * tip)/100
print("Tip Amount $"+ str(round(toatalTip)))
totalAmount = round(bill +toatalTip)
print("Total Amount = $" +str( totalAmount))
print("Each person should pay $" + str(round( totalAmount / people,2)))


