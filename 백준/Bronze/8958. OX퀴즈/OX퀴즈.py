import sys
input=sys.stdin.readline
n=int(input().rstrip())
a=[]
score = 0
count = 0
for i in range(n):
    a.append(input().rstrip())

for i in a:
    for j in i:
        if j == 'O':
            count+=1
            score = score + count
        elif j == 'X':
            count = 0
            continue
    print(score)
    score = 0
    count = 0