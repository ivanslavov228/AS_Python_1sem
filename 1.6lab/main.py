s = input()
n = int(input())
result = ''.join(s[i] for i in range(len(s)) if (i + 1) % n != 0)
print(result)
