import sys
input=sys.stdin.readline

t=int(input().rstrip())
input()

result=[]
for j in range(t):
    n=int(input().rstrip())
    candy = 0
    for i in range(n):
        candy+=int(input().rstrip())
    if candy % n == 0:
        result.append('YES')
    else: result.append('NO')
    input()
for i in result:
    print(i)