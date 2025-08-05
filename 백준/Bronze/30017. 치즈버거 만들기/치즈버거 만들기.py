import sys
input=sys.stdin.readline

a, b = map(int, input().rstrip().split())
hamburg = 0
if a > b:
    hamburg = b+b+1
elif a <= b:
    hamburg = a+a-1
print(hamburg)