import sys

result = []
while(True):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    if a == 0 and b==0 and c ==0:
        break
    if a>b and a>c and a**2 == b**2 + c**2: result.append('right')
    elif b>a and b>c and b**2 == a**2 + c**2: result.append('right')
    elif c>b and c>a and c**2 == a**2 + b**2: result.append('right')
    else: result.append('wrong')
for _ in result:
    print(_)