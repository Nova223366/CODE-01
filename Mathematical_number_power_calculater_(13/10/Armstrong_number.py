string = input("Enter your word: ")
character = input("Enter a word you want to: ")
count = 0
while string.__len__() > count:
    if string[count] == character:
        print(f"Character '{character}' found at index {count}")
    count += 1
print(f"Total occurrences of '{character}': {string.count(character)}")