class vehicle():
    def __init__(self, maxspeed, mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

modelX = vehicle(240, 18)

print("Model X:\n -Max speed: {0}kph\n -Mileage: {1}km".format(modelX.maxspeed, modelX.mileage))