import sys
input=sys.stdin.readline

n=int(input().rstrip())
num=input()
sum=0
for i in range(n):
    sum=int(num[i])+sum
print(sum)