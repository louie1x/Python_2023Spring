n = int(input())
L = list(map(int, input().split()))
M = list(map(int, input().split()))

language_class = []
math_class = []

for i in range(n):
    if L[i] > M[i]:
        language_class.append(i+1)
    else:
        math_class.append(i+1)

if not language_class:
    print("-1")
else:
    print(" ".join(map(str, language_class)))
    
if not math_class:
    print("-1")
else:
    print(" ".join(map(str, math_class)))

