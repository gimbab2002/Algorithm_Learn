import sys
input = sys.stdin.readline
n,m=map(int,input().rstrip().split())

count=0

while m :
#n이 무조건 m보다 작도록 설정
    if n > m : 
        temp = n
        n=m
        m=temp
    if n==m : 
        count+=1 
        break
    elif n==1:
        count=count+m
        break
    else:
        count=count+(m//n)
        m=m%n

print(count)