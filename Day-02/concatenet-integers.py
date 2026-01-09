two_digit_number = input() #Output : as String

print(type(two_digit_number))    # Always check the datatype to avoid confusion.

# print(type(two_digit_number[0])) Str
# print(type(two_digit_number[1])) Str

#We have to add the "int" numbers such as: 35 to 3 + 5 = 8 should be the output

print(int((two_digit_number[0])) + int(two_digit_number[1]))