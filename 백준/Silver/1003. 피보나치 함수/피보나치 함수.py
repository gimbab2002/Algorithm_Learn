import sys
input=sys.stdin.readline

t=int(input().rstrip())
dp_0 = [1,0]
dp_1 = [0,1]

for i in range(t):
    n=int(input().rstrip())
    for j in range(len(dp_0), n+1):
        dp_0.append(dp_0[j-1]+dp_0[j-2])
        dp_1.append(dp_1[j-1]+dp_1[j-2])
    print(dp_0[n], end = ' ')
    print(dp_1[n])