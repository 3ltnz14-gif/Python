class vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class bus(vehicle):
    pass

schoolbus = bus("School Volvo", 180, 12)

print(schoolbus.name,  "- name")
print(schoolbus.maxspeed, "- max speed")
print(schoolbus.mileage, "- mileage")