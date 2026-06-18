def romantoint(n):
    roman = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    result = 0

    for i in range(0, len(n) - 1):
        if roman[n[i]] < roman[n[i+1]]:
            result -= roman[n[i]]
        else: 
            result += roman[n[i]]
    return result + roman[n[-1]]

num = input("Enter Roman Numerals: ")

print("Int Equivalent:", romantoint(num))