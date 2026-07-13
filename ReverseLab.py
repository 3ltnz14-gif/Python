#Reverse Lab
#Topics: Digit Extraction | Reverse Number | Reverse String | Powers of 4

print("Reverse lab:\n")

#Part 1: Digit Scanner
n = int(input("Enter a Number: "))
temp = n
while temp > 0:
    print(f"Last Digit: {temp%10} \n Remaining digits: {temp//10}")
    temp //= 10
print()

#Part 2: Number Flipper
def flipnumber(num):
    if num // 10 == 0:
        return num
    last = num % 10
    rest = flipnumber(num // 10)
    return last * pow(10, len(str(rest))) + rest


n2 = int(input("Flip a Number: "))
print(f"{n2} flipped -> {flipnumber(n2)}")


#Part 3: Name Flipper
def flipname(s):
    if len(s) == 1:
        return s
    return flipname(s[1:]) + s[0]


n3 = input("Flip your Name: ")
print(f"{n3} flipped -> {flipname(n3)}")

#Part 4: Power of 4?
def ispower4(n):
    if n <= 0:
        return False #Stop - Impossible
    if n == 1:
        return True  #Stop - Confirmed!
    if n % 4 == 0:
        return ispower4(n//4)
    return False

print(f"16 -> {ispower4(16)}")
print(f"12 -> {ispower4(12)}")
guess = int(input("Test if your own number is a power of 4!\nInput: "))
print(f"{guess} -> {ispower4(guess)}")


