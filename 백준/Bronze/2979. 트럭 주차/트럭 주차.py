import sys
input=sys.stdin.readline

a,b,c = map(int, input().rstrip().split())
fee = 0
counter = 0

arr1, leave1 = map(int, input().rstrip().split())
arr2, leave2 = map(int, input().rstrip().split())
arr3, leave3 = map(int, input().rstrip().split())


time_range = list(range(min(arr1,arr2,arr3,leave1,leave2,leave3),max(arr1,arr2,arr3,leave1,leave2,leave3)+1))
for i in time_range:
    if i == arr1 or i == arr2 or i == arr3:
        if i == arr1 == arr2 ==arr3:
            counter+=3
        elif (i == arr1 and i == arr2) or (i == arr2 and i == arr3) or (i == arr3 and i == arr1):
            counter+=2
        else:
            counter +=1
    if i == leave1 or i == leave2 or i == leave3:
        if i == leave1 == leave2 == leave3:
            counter-=3
        elif (i == leave1 and i == leave2) or (i == leave2 and i == leave3) or (i == leave3 and i == leave1):
            counter-=2
        else:
            counter-=1
    if counter == 1 :
        fee += a
    if counter == 2:
        fee+=b*counter
    if counter==3:
        fee+=c*counter
print(fee)    
