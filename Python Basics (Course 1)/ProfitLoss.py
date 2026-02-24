production_cost = float(input("Please enter the cost to produce your item:\n"))
sale_amount = float(input("Please enter the sales amount of your product:\n"))

if sale_amount > production_cost:
    amount = sale_amount - production_cost
    print("Production Cost: {0}\nSale Amount: {1}\nTotal Profit = {2}" .format(production_cost, sale_amount, amount))
else:
    print("No Profit!")