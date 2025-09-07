import sys
input=sys.stdin.readline

n, m = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))
tree = 0
end = max(trees)
start = 0
mid = (start+end) // 2
result = 0
while start <= end:
    for i in trees:
        if i > mid:
            tree+=(i - mid)
    if tree >= m:
        result=mid
        start = mid+1
        mid = (start+end)//2
    else:
        end = mid-1
        mid = (start+end) // 2
    tree=0
print(result)