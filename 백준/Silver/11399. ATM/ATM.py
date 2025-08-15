import sys
input=sys.stdin.readline

n=int(input().rstrip())
p = list(map(int, input().rstrip().split()))
p.sort()
time = [0]
result = 0
for i in p:
    time.append(time[-1]+i)
for j in time:
    result+=j
print(result)