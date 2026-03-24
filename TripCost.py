def hotel(n):
    return 140*n

def plane(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
    
def car(d):
    if d >= 7:
        return 40*d - 50
    elif d>= 3:
        return 40*d - 20
    else:
        return 40*d
    
def tripcost(city, d, s):
    return car(d) + hotel(d) + plane(city) + s

print("Cost of car rental:", car(7))
print("Cost of plane ride:", plane("Los Angeles"))
print("Cost of hotel room:", hotel(7))
print("Total cost of the trip:", tripcost("Los Angeles", 7, 500))
