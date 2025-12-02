with open('f.txt', 'r') as file:
    numbers = map(int, file.read().split())
    count = sum(1 for num in numbers if num % 2 == 0)
    print(count)
