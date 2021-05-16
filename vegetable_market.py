vegetable_price_kg = float(input())  # зеленчуци
fruits_price_kg = float(input())   # плодове
vegetable_total_kg = int(input()) # общо кг зеленчуци
fruits_total_kg = int(input())    # общо кг плодове
total_vegatable = vegetable_price_kg * vegetable_total_kg
total_fruit = fruits_price_kg * fruits_total_kg
total_price = (total_vegatable + total_fruit) / 1.94
print(f'{total_price:.2f}')