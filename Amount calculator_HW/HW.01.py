n = int(input("Enter the amount you have (₹): "))
if n>0:
    n1 = int(input("Enter the amount you have to give to shopkeeper (₹): "))
    if n1>0 and n1<=n:
        print(f"{n}-{n1} ='₹{n-n1}'")
    else:
        print("Please enter a valid amount to give shopkeeper")
else:
    print("Please enter a valid amount you have")