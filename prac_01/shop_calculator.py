MINIMUM_PRICE = 0
DISCOUNTED_PRICE = 100
DISCOUNTED = 0.1

total_price = 0
item_number = int(input("Number of items:"))
for i in range(item_number):
    price = float(input("Price of item:"))
    while price < MINIMUM_PRICE:
        print("Invalid number of items!")
        price = float(input("Price of item:"))
    else:
        total_price += price
if total_price >= DISCOUNTED_PRICE:
    total_price = total_price * (1 - DISCOUNTED)
print(f"Total price for {item_number} items is ${total_price} ")



