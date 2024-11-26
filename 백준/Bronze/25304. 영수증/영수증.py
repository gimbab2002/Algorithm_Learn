X = int(input())
N = int(input())
total = 0
for i in range(N):
    item = list(map(int, input().split()))
    total += item[0]*item[1]
if(total == X): 
    print("Yes")
else:
    print("No")