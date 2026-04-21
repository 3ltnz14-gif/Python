class flashcard:
    def __init__(self, word, meaning):
        self.__word = word
        self.__meaning = meaning
    def __str__(self):
        return ("{0}({1})".format(self.__word, self.__meaning))

flash = []
print("Welcome to the Flashcard application.")

while(True):
    word = input("What's the flashcard word/answer? ")
    meaning = input("What's the flashcard meaning/question? ")

    flashobj = flashcard(word, meaning)
    
    flash.append(flashobj)
    if input("Would you like to add more flashcards? Y/N")[:1].lower() == "n":
        break
    else:
        pass

print("Your flashcards:")
for i in flash:
    print(">{0}".format(i))

