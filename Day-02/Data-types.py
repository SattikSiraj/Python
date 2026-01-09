# Data Types in Python
#Strings
print("hello"[1])  # Output: e
print("123" + "456")  # Output: 123456
# Integers
print(123 + 456)  # Output: 579
# Floats
print(f"{3.14 + 1.0:.1f}")  # Output: 4.1
# Booleans
print(True + False)  # Output: 1
print(type("Hello"))  # Output: <class 'str'>
print(type(123))      # Output: <class 'int'>
print(type(3.14))     # Output: <class 'float'>
print(type(True))     # Output: <class 'bool'>
# Type Conversion
num_str = "100"
num_int = int(num_str)
print(num_int + 50)  # Output: 150
float_num = float(num_int)
print(float_num + 0.5)  # Output: 100.5
bool_num = bool(1)
print(bool_num)  # Output: True
# Tip Calculator Example
print("Welcome to the tip Calculator!\n")
bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give\n 10, 12 or 15\n"))
split = int(input("How many people to split the bill?\n$"))
total_tip = bill * (tip / 100)
total_bill = bill + total_tip
res = total_bill / split
print(f"Each person should pay: ${res:.2f}")
# Note: The tip calculation has been corrected to calculate the tip as a percentage of the bill.
