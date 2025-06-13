import sys
input=sys.stdin.readline

a=list(map(int,input().rstrip().split()))

ind = a.index(max(a))
temp = a[ind]
a[ind]=a[0]
a[0]=temp

while a[0] >= a[1]+a[2]:
    a[0]-=1
print(a[0]+a[1]+a[2])