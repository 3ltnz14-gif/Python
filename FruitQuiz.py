import random
class fruitquiz:
    def __init__(self):
        self.fruits = {
                        "apple":"red",
                        "banana":"yellow",
                        "grape":"purple",
                        "orange":"orange",
                        "lemon":"yellow",
                        "watermelon":"green"
                    }
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print(f"What is the color of {fruit}?")
            ans = input("Your Answer: ")
            if ans.lower() == color:
                print("Correct!")
            else:
                print(f"Wrong! The correct color is {color}")
            if input("Enter y to continue, n to stop").lower()[:1] == "n":
                break
print("Welcome to fruit quiz:")
fq = fruitquiz()
fq.quiz()