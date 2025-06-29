import sys
input=sys.stdin.readline

n=[]
n.append(input().rstrip())
while n[-1]!='0':
    n.append(input().rstrip())
for i in n:
    newstr = ''.join(reversed(i))
    if i == '0':
        break
    elif i == newstr:
        print('yes')
    else: print('no')