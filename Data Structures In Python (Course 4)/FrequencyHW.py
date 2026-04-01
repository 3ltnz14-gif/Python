dict = {"Hello":1, "My":1, "name":2, "is":2, "Elijah":1, ".":2, "How":1, "are":2, "you":1, "today":2, "?":1}

print("The original dictionary is: \n" + str(dict))

k = 2
r = 0
for key in dict:
    if dict[key] == k:
        r += 1

print("The frequency of 2 is" + str(r))