number = float(input())
convert_from = input()
convert_to = input()
meters = 0
if convert_from == "mm":
    meters = number / 1000
elif convert_from == "cm":
    meters = number / 100
elif convert_from == "m":
    meters = number
result = 0
if convert_to == "mm":
    result = meters * 1000
elif convert_to == "cm":
    result = meters * 100
elif convert_to == "m":
    result = meters
print(f"{result:.3f}")
