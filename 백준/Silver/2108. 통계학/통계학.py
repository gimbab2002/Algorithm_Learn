import sys
from collections import Counter
import math

input=sys.stdin.readline

n=int(input().rstrip())
arr = []
total = 0
for i in range(n):
    arr.append(int(input().rstrip()))

arr.sort()
for i in arr:
    total+=i
print(math.floor(total/n + 0.5))
print(arr[n//2])

cnt = Counter(arr).most_common(2)
if len(arr)>1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(arr[-1] - arr[0])