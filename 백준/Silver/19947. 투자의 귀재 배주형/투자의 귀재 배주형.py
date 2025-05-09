import sys

m, y = map(int, sys.stdin.readline().rstrip().split())
dp =[]
dp.append(m)
dp.append(int(m*1.05))
dp.append(int(dp[1]*(1.05)))
dp.append(int(m*(1.2)))
dp.append(max(int(dp[3]*(1.05)), int(dp[1]*(1.2))))
def money(m,y,dp):
    if y <len(dp) and y>0:
        return dp[y]
    elif y <=0:
        return dp[0]
    else:
        dp.append(max(int(money(m, y-5, dp)*(1.35)),
                        int(money(m, y-3, dp)*(1.2)), 
                        int(money(m,y-1,dp)*(1.05))))
        return dp[y]

print(money(m,y,dp))