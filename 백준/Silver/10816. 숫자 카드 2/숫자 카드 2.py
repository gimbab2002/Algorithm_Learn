import sys
input=sys.stdin.readline

def binary_search(num, a, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if num == a[mid]:
        return dic[num]
    elif num > a[mid]:
        return binary_search(num, a, mid+1, end)
    elif num < a[mid]:
        return binary_search(num, a, start, mid-1)

n=int(input().rstrip())

a=list(map(int, input().rstrip().split()))
a.sort()

m=int(input().rstrip())

b=list(map(int, input().rstrip().split()))

dic = {}

for i in a:
    if i in dic:
        dic[i]+=1
    else: 
        dic[i]=1


    
for i in b:
    print(binary_search(i, a, 0, len(a)-1), end=' ')

