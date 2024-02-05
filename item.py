item_name = ["bag", "pencil", "glasses", "shoes"]
price = [2.5, 2.3, 5.2, 8.0]
quantity = [2, 4, 3, 2]
budget = 2.0

# Calculate the total_cost
total_cost = sum(quantity * price for quantity, price in zip(quantity, price))

# Budget check
if total_cost <= budget:
    print("You have enough budget.")
else:
    print("Review your shopping list.")
