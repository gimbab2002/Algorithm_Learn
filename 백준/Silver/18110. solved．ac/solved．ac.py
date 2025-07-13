import sys
import math
input=sys.stdin.readline
n=int(input().rstrip())
if n ==0:
    print(n)
    exit(0)
a=[]
for i in range(n):
    a.append(int(input().rstrip()))
a.sort()
erase = math.floor(len(a) * (15/100)+0.5)
start = erase
end = len(a)-erase
sum=0
count=0
for i in range(start, end):
    sum+=a[i]
    count+=1
avr = math.floor(sum/count + 0.5)
print(avr)