foods = []
prices = []
total = 0
ind = 0

while True:
    food = input("Enter the name of food (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        foods.append(food)
        price = float(input(f"Enter the price of {food}: "))
        prices.append(price)
        total += price

print("--------------Shopping Cart--------------")

for x in foods:
    print(x, end="  ") 
    print(f"${prices[ind]}")
    ind += 1

print(f"Total: {total}$")
