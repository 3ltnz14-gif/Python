class BMW:
    def fueltype(self):
        print("BMW uses petrol/diesel")
    def maxspeed(self):
        print("BMW max speed is 250 km/h")
    def mileage(self):
        print("BMW mileage is 15 km/l")
    def colour(self):
        print("BMW colour is black")
    def price(self):
        print("BMW price is $80000")

class Ferrari:
    def fueltype(self):
        print("Ferrari uses high-octane petrol")
    def maxspeed(self):
        print("Ferrari max speed is 340 km/h")
    def mileage(self):
        print("Ferrari mileage is 8 km/l")
    def colour(self):
        print("Ferrari colour is red")
    def price(self):
        print("Ferrari price is $250000")

b = BMW()
f = Ferrari()

for car in b, f:
    car.fueltype()
    car.maxspeed()
    car.mileage()
    car.colour()
    car.price()