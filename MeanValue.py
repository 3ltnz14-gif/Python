#The mean of 40 numbers is 338. Late on, I detected that I misread the 
#number 56 as 36. Find the correct mean of given numbers.
mean1 = 38
wrongnumber = 36
correctnumber = 56
totalnumbers = 40
#sum of 40 numbers
sum = mean1 * totalnumbers
print("The sum of the 40 numbers:", sum)

#correct sum
num2 = sum - ((wrongnumber) - (correctnumber))
print("sum - ((wrongnumber) - (correctnumber)):", num2)

#correct mean
mean2 = num2 / totalnumbers
print(mean2)