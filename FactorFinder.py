def printfactors(n):
    print("The factors of", n, "are: ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

number = int(input("ENter your number to find its factors: "))
printfactors(number)