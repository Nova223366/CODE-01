nums = input("Enter numbers without spaces: ")
num_list = [int(n) for n in nums]

print(num_list)
if all(n >= 0 for n in num_list):
    squares = [n * n for n in num_list]
    even_odd = ["even" if n % 2 == 0 else "odd" for n in num_list]
    
    for n, square, eo in zip(num_list, squares, even_odd):
        print(f"'{square}' is the square of '{n}'")
        print(f"'{n}' is an '{eo} number'")
    
    print("\nThe length of the number digit by digit is:", len(nums))


    # if n == 0 or n <0:
#     print("Please enter a fair number")
# else:
#     print(f"'{n*n}' is the square of '{n}'")

#     if n%2 == 0:
#         print(f"'{n}' is an 'even number'")
#     else:
#         print(f"'{n}' is an 'odd number'")
#     z = [n]
#     print("\n",z,"Also the lenth of this number digt by digit is:",len(str(n)))
#     print(num_list)
# print("\nThank you for using this program!")
