import sys
input=sys.stdin.readline

s = set()
n=int(input().rstrip())

for i in range(n):
    oper = input().rstrip()
    if 'add' in oper:
        s.add(int(oper[-2:].lstrip()))
    elif 'remove' in oper:
        try:
            s.remove(int(oper[-2:].lstrip()))
        except:
            continue
    elif 'check' in oper:
        if int(oper[-2:].lstrip()) in s:
            print(1)
        else:
            print(0)
    elif 'toggle' in oper:
        if int(oper[-2:].lstrip()) in s:
            s.remove(int(oper[-2:].lstrip()))
        else:
            s.add(int(oper[-2:].lstrip()))
    elif 'all' in oper:
        s = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif 'empty' in oper:
        s = set()