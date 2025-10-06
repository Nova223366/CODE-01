ride = input("Enter your ride choice (Car/bike): ").title()
if ride == "Car":
    print("You chose Car.")
    if input("Do you have a driving license? (yes/no): ").lower() == "yes":
        print("You can drive a car.")
    else:
        print("You need a driving license to drive a car.") 
elif ride == "Bike":
    print("You chose Bike.")
    if input("Do you have a bike license? (yes/no): ").lower() == "yes":
        print("You can ride a bike.")
    else:
        print("You need a bike license to ride a bike.")
else:
    print("Invalid choice. Please choose either 'Car' or 'Bike'.")