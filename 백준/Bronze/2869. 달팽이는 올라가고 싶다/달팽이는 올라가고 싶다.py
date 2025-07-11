import sys
input=sys.stdin.readline
a,b,v = map(int, input().rstrip().split())

x = (v-b)/(a-b)
if x == int(x):
    print(int(x))
else:
    print(int(x)+1)

