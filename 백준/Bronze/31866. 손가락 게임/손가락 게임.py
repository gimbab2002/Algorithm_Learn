import sys
input=sys.stdin.readline

n, m = map(int, input().rstrip().split())

if n==0:
    if m==2:
        print('>')
    elif m==5:
        print('<')
    elif m==0:
        print('=')
    else: print('>')

elif n==2:
    if m==5:
        print('>')
    elif m==0:
        print('<')
    elif m==2:
        print('=')
    else: print('>')
    
elif n==5:
    if m==0:    
        print('>')
    elif m==2:
        print('<')
    elif m==5:
        print('=')
    else: print('>')
elif m==1 or m==3 or m==4:
    print('=')
else: print('<')