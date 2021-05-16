budget_movie = float(input())  # бюджет
stuntmen_count = int(input())  # статистите
price_per_clothes = float(input())  # цена на дрехи (статисти)
price_decor = 0.1 * budget_movie
total_clothes_price = price_per_clothes * stuntmen_count
if stuntmen_count > 150:
    total_clothes_price *= 0.9
money_needed = price_decor + total_clothes_price
if money_needed > budget_movie:
    print("Not enough money!")
    print(f"Wingard needs {(money_needed - budget_movie):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budget_movie - money_needed):.2f} leva left.")