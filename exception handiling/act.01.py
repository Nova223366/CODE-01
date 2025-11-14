try :
    num = int(input("Enter a number: "))
    print(num)
except ValueError as ex:
    print("Exception caught:", ex)

print("I am outside the try block. ")