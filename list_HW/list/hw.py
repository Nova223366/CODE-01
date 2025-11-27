print("\nNote-- 'This code is can do square, even and odd number check only once a digit at a time'\n")
n = int(input("Enter number's only: "))
if n == 0 or n <0:
    print("Please enter a fair number")
else:
    print(f"'{n*n}' is the square of '{n}'")

    if n%2 == 0:
        print(f"'{n}' is an 'even number'")
    else:
        print(f"'{n}' is an 'odd number'")
    z = [n]
    print("\n",z,"Also the lenth of this number digt by digit is:",len(str(n)))
print("\nThank you for using this program!")