import sys
input=sys.stdin.readline

n = int(input().rstrip())
a=list(map(int, input().rstrip().split()))

people =0

for i in a:
    if n >= i:
        people+=i
    else:
        people+=n
print(people) 