def total(bill, tip):
    total = bill*(1+ 0.01*tip)
    total = round(total, 2)
    print(f"Please pay {total}")

total(150, 20)