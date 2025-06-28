import sys
input=sys.stdin.readline

n=int(input().rstrip())

for i in range(1,n+1):
    gen=sum(map(int,str(i)))
    gen_sum=i+gen
    if gen_sum == n:
        print(i)
        break
    if i == n:
        print(0)