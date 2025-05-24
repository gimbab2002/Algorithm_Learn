import sys
input=sys.stdin.readline

n=int(input().rstrip())
people= list(map(int, input().rstrip().split()))
t, p = map(int, input().rstrip().split())
count=0
for i in people:
    if i ==0 : continue
    elif i % t ==0:
        count += i//t
    else:
        count += i//t + 1    
print(count)
print(n//p, end=' ')
print(n%p)