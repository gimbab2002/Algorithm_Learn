import sys
input=sys.stdin.readline

arr=[]
next= None
ind = None
for i in range(3):
    arr.append(input().rstrip())
for i in arr:
    if (i == 'FizzBuzz') or (i == 'Fizz') or (i == 'Buzz'):
        continue
    else:
        ind=arr.index(i)
        break    

next=int(arr[ind])+(len(arr)-ind)

if next % 3 == 0 and next % 5 == 0:
    print("FizzBuzz")
elif next % 3 == 0:
    print("Fizz")
elif next % 5 == 0:
    print("Buzz")
else:
    print(next)