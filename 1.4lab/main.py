arr = list(map(int, input().split()))
max_index = arr.index(max(arr))
product = 1
for i in range(max_index + 1, len(arr)):
    product *= arr[i]
print(product)
