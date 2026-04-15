class parrot():
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

blu = parrot("Blu", 10)
woo = parrot("Woo", 15)

print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

print("Blu:\n -Name: {0}\n -Age: {1}".format(blu.name, blu.age))
print("Woo:\n -Name: {0}\n -Age: {1}".format(woo.name, woo.age))