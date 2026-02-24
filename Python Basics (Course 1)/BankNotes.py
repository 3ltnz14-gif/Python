input_amount = int(input("Please enter withdrawal amount:"))

note1 = input_amount//100
note2 = (input_amount%100)//50
note3 = ((input_amount%100)%50)//20
note4 = (((input_amount%100)%50)%20)//10
note5 = ((((input_amount%100)%50)%20)%10)//5
coin = (((((input_amount%100)%50)%20)%10)%5)//1

print("$100 notes:", note1)
print("$50 notes:", note2)
print("$20 notes:", note3)
print("$10 notes:", note4)
print("$5 notes:", note5)
print("$1 coins:", coin)