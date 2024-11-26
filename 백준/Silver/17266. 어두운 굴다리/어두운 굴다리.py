# N = int(input())
# M = int(input())
# x = list(map(int, input().split()))

# result = 1
# start = 0
# end = N

# while(start <= end):
#     mid = (start + end)//2
    
import sys
import math

input = sys.stdin.readline

N = int(input())
M = int(input())
loc = list(map(int, input().split()))

between = []

for i in range(1, M):
    between.append(math.ceil((loc[i]- loc[i-1])/2))

between.append(loc[0])
between.append(N - loc[-1])


print(max(between))
