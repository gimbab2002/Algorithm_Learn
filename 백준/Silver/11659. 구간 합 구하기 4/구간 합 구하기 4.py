import sys
input=sys.stdin.readline

n, m = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
sums = [0]
temp = 0
for i in nums:
    temp = temp + i    
    sums.append(temp)
for _ in range(m):
    i, j = map(int, input().rstrip().split())
    print(sums[j] - sums[i-1])