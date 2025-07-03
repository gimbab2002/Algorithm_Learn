import sys
input=sys.stdin.readline

t = int(input().rstrip())
k, n = [] ,[]
for i in range(t):
    k.append(int(input().rstrip())+1)
    n.append(int(input().rstrip()))

for flo, ho  in zip(k,n):
    dp = []
    for p in range(1,ho+1):
        dp.append(p)
    for floor in range(1, flo):
        for p in range(0,ho):
            sum=0
            for r in range(p+1):
                sum += dp[r+(ho*(floor-1))]
            dp.append(sum)
    print(dp[-1])