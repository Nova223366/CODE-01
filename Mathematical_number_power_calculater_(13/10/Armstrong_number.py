num = int(input("Enter your number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

print("Sum of cubes of digits:", sum)
