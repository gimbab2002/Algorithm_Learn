import sys

input = sys.stdin.readline

string1=input().rstrip()
string2=input().rstrip()
count=0
dp=[[0 for _ in range(len(string2)+1)] for _ in range(len(string1)+1)]


for i in range(0, len(string1)):
    for j in range(0, len(string2)):
        if(string1[i]==string2[j]):
            dp[i+1][j+1] = dp[i][j]+1
            
        else:
            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
            
print(dp[-1][-1])