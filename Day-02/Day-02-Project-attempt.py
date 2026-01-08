print("Welcome to the tip Calculator!\n")
bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give\n 10, 12 or 15\n"))
split = int(input("How many people to split the bill?\n$"))

res = (bill + tip)/split 

print(f"Each person should pay: ${res:.2f}")