import sys
input=sys.stdin.readline

a=[]
for _ in range(9):
    a.append(int(input().rstrip()))
print(max(a))
print(a.index(max(a))+1)