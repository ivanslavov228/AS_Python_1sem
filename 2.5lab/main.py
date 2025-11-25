def NOD(A, B):
    if A == 0:
        return B
    return NOD(B % A, A)

A, B, C, D = map(int, input().split())
print(NOD(A, B), NOD(A, C), NOD(A, D))
