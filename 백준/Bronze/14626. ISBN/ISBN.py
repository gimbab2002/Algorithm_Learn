import sys
input=sys.stdin.readline

code = input().rstrip()
flag = 0 
remember=0
sum=0
for i in code:
    if flag:
        if i == '*':
          remember=3  
          flag=0
        else:
            sum+=int(i)*3
            flag=0
    elif not flag:
        if i == '*':
            remember=1
            flag=1
        else:
            sum+=int(i)*1
            flag=1
for i in range(10):
    if (sum + i*remember) % 10 == 0:
        print(i)
