import sys 
input = sys.stdin.readline
n=int(input().rstrip())
a=list(map(int ,input().rstrip().split()))
v=int(input().rstrip())
count =0
for i in a:
    if i == v:
        count += 1
print(count)