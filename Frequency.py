test = {"Codingal":2, "is":2, "best":2, "for":2, "Coding":1}

print("The original dictionary is: \n" + str(test))

k = 2
r = 0
for key in test:
    if test[key] == k:
        r += 1

print("Frequency of 2 is: "+ str(r))