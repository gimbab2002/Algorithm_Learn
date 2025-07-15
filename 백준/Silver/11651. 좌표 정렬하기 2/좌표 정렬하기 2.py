import sys
input=sys.stdin.readline

def switch(a):
    temp=a[-1]
    a[-1] = a[0]
    a[0] = temp

n=int(input().rstrip())
a=[]
for i in range(n):
    a.append(list(map(int, input().rstrip().split())))
    switch(a[-1])
a.sort()

for i in a:
    switch(i)
    print(*i)

