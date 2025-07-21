import sys
input=sys.stdin.readline
n=int(input().rstrip())
a=[]
for i in range(n):
    a.append(int(input().rstrip()))

def mkearr(a):
    arr = list(range(1, len(a)+1))
    count=0
    stack = []
    result=[]
    way=[]
    for i in range(len(a)):
        stack.append(arr[i])
        way.append('+')
        try:
            while stack[-1] == a[count]:
                result.append(stack.pop(-1))
                way.append('-')
                count+=1
        except:
            continue
    if result == a:
        print(*way, sep="\n")
    else:
        print('NO')
mkearr(a)
 


        