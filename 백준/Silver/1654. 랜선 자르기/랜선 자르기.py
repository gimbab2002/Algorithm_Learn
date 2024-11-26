K, N = map(int, input().split())
array = [int(input()) for _ in range(K)]
array.sort()

start = 1
end = array[-1]

while(start<=end):   
    mid = (start+end)//2 
    count = 0
    for i in array :
        count += (i//mid)
    if count < N:
        end = mid-1
    else : 
        result = mid
        start = mid+1
        
print(result)
