import sys

input=sys.stdin.readline

n=int(input().rstrip())
a=[]

for i in range(n):
    a.append(int(input().rstrip()))
a.sort()
print(*a, sep='\n')