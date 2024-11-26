def ways(n):
    if n == 1 : return 1
    if n == 2 : return 2
    if n == 3 : return 4
    if n>3:
        return ways(n-1) + ways(n-2) + ways(n-3)
    
T = int(input())
n = [int(input()) for i in range(T)]
for j in n:   
    print(ways(j))