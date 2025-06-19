import sys
input=sys.stdin.readline
a = [1,1,2,2,2,8]
b=list(map(int, input().rstrip().split()))

for i in range(len(a)):
    a[i]=a[i]-b[i] 
print(*a)