print("\nNote-- 'This code can do square, even and odd number or enter only fair number not nagative or else'\n")
print("**This program will separate each digit of the number you enter and will treat them as individual numbers**\n")

statement = input("Did you read the statement above? (yes/no): ").lower()

if statement == "yes":
    num_str = input("Enter numbers without spaces: ")

    num_list = [int(digit) for digit in num_str]

    print("\nSeparated digits:", num_list,"\n")

    if all(n >= 0 for n in num_list):

        for n in num_list:
            print(f"'{n*n}' is the square of '{n}'")

            if n % 2 == 0:
                print(f"'{n}' is an even number\n")
            else:
                print(f"'{n}' is an odd number\n")

        print("\nThe length of the number digit by digit is:", len(num_list))

    else:
        print("Please enter positive numbers only.")

else:
    print("Please read the statement before using the program.")

print("\nThank you for using this program!")
