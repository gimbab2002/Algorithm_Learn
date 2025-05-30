import sys 
input= sys.stdin.readline

n=int(input().rstrip())
if n==1: 
    print(0)
    exit(0)

dp=[[0 for _ in range(n+1)] for _ in range(n+1)]

a=[0 for _ in range(n+1)]
for i in range(n):
    c, d = map(int, input().rstrip().split())
    a[i]=c
    a[i+1]=d        

for r in range(1,n):
    for i in range(1, n-r+1):
        j = i + r
        dp[i][j] = sys.maxsize
        for k in range(i,j):
            temp=dp[i][k] + dp[k+1][j] + a[i-1] * a[k] * a[j]
            if dp[i][j] > temp: dp[i][j] = temp  

print(dp[1][n])   

    