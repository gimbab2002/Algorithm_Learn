import sys
input=sys.stdin.readline

n=int(input().rstrip())

for i in range(n*2-1,0,-2):
    print(("*"*i).center(n*2).rstrip())

for j in range(3,n*2,2):
    print(("*"*j).center(n*2).rstrip())