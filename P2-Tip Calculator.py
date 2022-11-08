print("Welcome to the tip calculator.")
# Actual bill
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# converting tip. Eg:Total bill with  19 percent tip  will be 119 percent of actual bill. So actual bill * 1.19 times will give total bill.
tip = 1 + tip/100
n = int(input("How many people to split the bill? "))
# Calculating total bill and dividing it by number of people
billperperson = (bill * tip) / n
# Formatting bill to 2 decimal points
billperperson = "{:.2f}".format(round(billperperson,2))
print(f"Each person should pay: ${billperperson}")
