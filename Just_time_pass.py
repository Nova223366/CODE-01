while True:
    list = ["Aditya", "Rohin", "Saqib", "Aakil"]
    print("Enter your name to check your name")
    n = input("Enter you name here: ").title()
    if n in list:
        print(f"{n} you can enter in class")
    else:
        print("your name is not in list, please kindly contact your teacher")
        