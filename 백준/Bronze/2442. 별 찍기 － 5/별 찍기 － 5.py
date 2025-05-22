import sys
input=sys.stdin.readline

n=int(input().rstrip())

for i in range(1,n*2,2):
    print(("*"*i).center(n*2).rstrip())