print("Enter prices of 6 items:")
prices = [int(input(f"Item {i}: ")) for i in range(1, 7)]
budget = int(input("\nEnter total budget: "))
print()

total, bought = 0, []
for i, p in enumerate(prices, 1):
    can_buy = total + p <= budget
    if can_buy:
        total += p
        bought.append(p)
    print(f"Item {i} = {p} -> {'buy' if can_buy else 'cannot buy'}\nCurrent total = {total}\n")

print(f"Bought items: {bought}\nTotal spent: {total}\nRemaining budget: {budget - total}")