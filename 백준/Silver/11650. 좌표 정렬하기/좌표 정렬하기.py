import sys
input=sys.stdin.readline

n=int(input().rstrip())
a=[]
for i in range(n):
    a.append(list(map(int, input().rstrip().split())))
a.sort()

for i in a:
    print(*i)