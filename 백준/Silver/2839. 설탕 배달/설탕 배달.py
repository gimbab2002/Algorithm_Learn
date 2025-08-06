import sys
input=sys.stdin.readline

n=int(input().rstrip())
result= -1
if n % 5 == 0:
    result = n//5
if n % 3 == 0:
    if result == -1 :
        result = n//3
    if result > n//3:
        result = n//3
for j in range(n//5, 0, -1):
    for i in range(1, n//3 + 1):
        if 5 * j + 3 * i == n:
            if result == -1 :
                result = i+j
            if result > i+j:
                result = i+j
print(result)