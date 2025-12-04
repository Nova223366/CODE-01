test_dict = {"Codingal":2, "is":3, "best":2, "2":2, "coding": 1}

print("Original Dictionary:", str(test_dict))

k = 2
res = 0
for key in test_dict:
    if test_dict[key]==k:
        res = res +1

print("Frequency of", k, "is:", str(res))