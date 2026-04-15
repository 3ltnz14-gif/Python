class dog():
    species = "Dog"
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

charlie = dog("Charlie", 12, "Golden Retriever")
luna = dog("Luna", 11, "Pug")

print("Charlie:\n -Species: {0}\n -Name: {1}\n -Age: {2}\n -Breed: {3}".format(charlie.species, charlie.name, charlie.age, charlie.breed))
print("Luna:\n -Species: {0}\n -Name: {1}\n -Age: {2}\n -Breed: {3}".format(luna.species, luna.name, luna.age, luna.breed))
