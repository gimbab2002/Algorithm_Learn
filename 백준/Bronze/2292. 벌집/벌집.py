#1 7 19 37 61 ....
n=int(input())

a= []
count = 1
i=1
a.append(i)
while i <= 1000000000:
    i = i+6*count
    count+=1
    a.append(i)


for j in a:
    if n <=j:
        print(a.index(j)+1)
        break