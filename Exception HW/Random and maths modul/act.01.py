import random 
playing = True
number = str(random.randint(10,14))
print("I will generate a number from 10 to 14, and you have to guess it!")

print("The game ends when you get 1 hero!")

while playing:
    guess = input("Enter your guess: ")
    if number == guess:
        print("Congratulations! You guessed the number correctly.")
        print("The number was:", number)
        break
    else:
        print("Wrong guess. Try again!")