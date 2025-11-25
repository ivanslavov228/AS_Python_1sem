# а)
try:
    num = float(input())
    power = int(input())
    if power < 0:
        raise ValueError("Отрицательная степень")
    print(num ** power)
except ValueError as e:
    print(e)

# б)
try:
    num = int(input())
    if num % 2 != 0:
        raise ValueError("Число не является четным")
    print("Число является четным")
except ValueError as e:
    print(e)

# в)
num = float(input())
power = int(input())
assert power >= 0, "Отрицательная степень"
print(num ** power)
