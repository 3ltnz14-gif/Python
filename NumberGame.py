import random
playing = True
att = 0
number = str(random.randint(0, 9))
print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.\n",
"The game ends when you get one correct.")
while playing:
    att += 1
    guess = input("Guess the number!")
    if number == guess:
        print("You won the game! It took you {0} attempts!" .format(att))
        print("The number was", number)
        break
    else:
        print("Your guess isnt quite right. You've taken {0} attempts." .format(att)) 
        