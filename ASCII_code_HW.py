# only for single alphabet
print("This program is only aplicable for single alphabet")
ch = input("Enter any alphabet: ")
if len(ch) == 1 and ch.isalpha():
    ascii_value = ord(ch)
    print("The ASCII code of", ch, "is:", ascii_value)
else:
    print("Please enter a single alphabet only!")