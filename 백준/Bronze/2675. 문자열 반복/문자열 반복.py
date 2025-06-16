import sys
input=sys.stdin.readline

t=int(input().rstrip())
result = []

for i in range(t):
    r,s=input().rstrip().split()
    r=int(r)
    string=''
    for i in s:
        string=string+i*r
    result.append(string)
print(*result, sep='\n')