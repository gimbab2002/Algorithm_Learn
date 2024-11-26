#피보나치와 동일
dp = []
dp.append(1)
dp.append(2)

n = int(input())


while(len(dp)<n):
    dp.append((dp[len(dp)-1]%10007 + dp[len(dp)-2])%10007)
if(n == 1): print(dp[0])
else:print(dp[len(dp)-1])