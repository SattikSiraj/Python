print("Welcome to the tip Calculator!\n")
bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give\n 10, 12 or 15\n"))
split = int(input("How many people to split the bill?\n$"))

total_tip = bill * (tip/100)
total_bill = bill + total_tip
result = total_bill/split

print(f"Each person should pay: ${result:.2f}")