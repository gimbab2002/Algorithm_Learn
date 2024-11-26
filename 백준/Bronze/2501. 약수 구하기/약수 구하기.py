dp = []
N, K = map(int, input().split())
for i in range(1,N+1):
    if(N % i == 0):
        dp.append(i)


if(K > len(dp)):
    print(0)
else : 
    print(dp[K-1])