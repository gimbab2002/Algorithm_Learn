import sys
input=sys.stdin.readline
n, m = map(int, input().rstrip().split())

arr=list(map(int, input().rstrip().split()))

sum=0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range (j+1, len(arr)):
            if (arr[i]+arr[j]+arr[k]) <= m and (arr[i]+arr[j]+arr[k]) > sum:
                sum = arr[i]+arr[j]+arr[k]                
print(sum)