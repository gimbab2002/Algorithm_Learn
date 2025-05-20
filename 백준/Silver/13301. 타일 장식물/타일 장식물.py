import sys
input=sys.stdin.readline

n=int(input().rstrip())
dp=[4,6]

if n==1:
    print(dp[0])
elif n==2:
    print(dp[1]) 
else:
    for i in range(2,n):
        dp.append(dp[i-2]+dp[i-1])
    print(dp[-1])