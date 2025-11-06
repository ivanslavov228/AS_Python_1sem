arr = list(map(int, input().split()))
result = sorted([x for x in arr if x > 10])
print(result)
