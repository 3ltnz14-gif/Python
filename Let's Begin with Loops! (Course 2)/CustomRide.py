print("Select your ride: ")
print("1. Bike")
print("2. Car")

#Choose which style you want
choice = int( input("Enter your choice: ") )

#Option 1 
if( choice == 1 ):
  print( "What type of bike? " )
  print("1. Motorcycle\n")
  print("2. Scooter\n")

  #Condition for selecting the type of bike
  choice2=int(input("Enter your choice: "))
  if choice2==1:
    print("you have selected motorcycle")
  else:
    print("you have selected scooter")

#Option 2
elif( choice == 2 ):
  print( "What type of car?" )
  print("1.Sedan")
  print("2.SUV")
  choice3=int(input("enter your choice3: "))

  if choice3==1:
  #Condition for selecting the type of car
    print("You have selected sedan")
  else:
    print("You have selected SUV")

else:
  print("Invalid input!")