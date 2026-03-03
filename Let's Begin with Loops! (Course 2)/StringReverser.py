#INput a string
string = input("Please enter a string to be reversed:\n--> ")

string2 = ""
#Loop for printing in reverse:
for i in string:
    string2 = i + string2

print("The Original String:\n{0}\n\nThe Reversed String:\n{1}" .format(string, string2))
