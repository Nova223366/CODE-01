try:
    num1 = int(input("Enter your age: "))
    if num1 % 2 == 0:
        print(f"Your age is {num1} and it is divisible by 2.\n")
    else:
        print(f"Your age is {num1} and it is NOT divisible by 2.\n")
except ValueError as ve:
    print("Please enter numeric values only!")
except Exception as ex:
    print("An unexpected error occurred:", ex)
finally:
    print("\tExecution of the try-except block is complete.")
