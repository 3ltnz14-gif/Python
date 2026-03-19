import random
while True:
    useraction = input("Enter a choice (rock, paper scissors): ")
    possibleactions = ["rock", "paper", "scissors"]
    computeraction = random.choice(possibleactions)
    print(f"\nYou chose {useraction}, the computer chose {computeraction}")

    if useraction == computeraction:
        print(f"Both players selected {useraction}. It's a tie!")
    elif useraction == "rock":
        if computeraction =="scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    elif useraction == "paper":
        if computeraction == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif useraction == "scissors":
        if computeraction == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")
    else:
        print("Wrong input! Typo?")