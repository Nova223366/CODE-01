try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter number: "))
    result = num1 / num2
    print("Result is:", result)
except ZeroDivisionError as zde:
    print("Division by zero is not allowed:")
except ValueError as ve:
    print("Please enter numeric values only:")
except Exception as ex:
    print("An unexpected error occurred:", ex)

except:
    print("This block will catch any exception.")
finally:
    print("Execution of the try-except block is complete.")