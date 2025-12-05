def math_word(words):
    ctr = 0
    list = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            list.append(word)

    print("List of words with first and last letter same:", list)
    return ctr
count = math_word(['aba', 'xyz', 'aa', 'x', 'bbb'])
print("Count of words with first and last letter same:", count)