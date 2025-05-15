import sys
input=sys.stdin.readline

p, r= map(int, input().rstrip().split())

if p/r < 0.2 :
    print('weak')
elif p/r >= 0.2 and p/r < 0.4 :
    print('normal')
elif p/r >=0.2 and p/r <0.6:
    print('strong')
elif p/r >= 0.6 :
    print('very strong')