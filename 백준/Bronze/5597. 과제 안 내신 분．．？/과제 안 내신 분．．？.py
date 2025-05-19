import sys
input=sys.stdin.readline

a=[0 for _ in range(30)]
for i in range(28):
    n=int(input().rstrip())
    a[n-1]=n
for i in a:
    if i == 0:
        print(a.index(i)+1)
        a[a.index(i)]=1