N = int(input())
array1 = list(map(int, input().split()))    
M = int(input())
array2 = list(map(int, input().split()))

array1.sort()


for i in array2:
    start = 0
    end = len(array1) - 1
    while(start <= end):     
        mid = (start + end) // 2
        if array1[mid] > i :
            end = mid - 1
        elif array1[mid] < i : 
            start = mid + 1 
        else: 
            break
    if (array1[mid] == i):print(1)
    else:print(0)
        
