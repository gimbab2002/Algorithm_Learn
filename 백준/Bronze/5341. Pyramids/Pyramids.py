import sys
input=sys.stdin.readline

n_arr = []
result = []
n_arr.append(int(input().rstrip()))

while n_arr[-1] != 0 :
    n_arr.append(int(input().rstrip()))

for i in n_arr:
    if i == 0:
        break
    sum=0
    while i != 0 :
        sum+=i
        i-=1
    result.append(sum)
print(*result, sep='\n')