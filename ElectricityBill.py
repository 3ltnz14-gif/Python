#Units Consumed By The User
units = int(input("Please enter the total number of units you consumed- "))

#Check condition of units consumed
#Then calculate amount and surcharge accordingly
#Surcharge is the tax value

#Check for units less than 50
if units < 50:
    amount = units * 2.60
    surcharge = 25
#Check for units less than 100
elif units < 100:
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35
#Check for units less than or equal to 200
elif units <= 200:
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45
#If units > 200:
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

#Calculate and Display the Total Electricity Bill:
total = amount + surcharge
print("\nAmount: {0}\nTax: {1}\nTotal: {2}" .format(amount, surcharge, float(total)))