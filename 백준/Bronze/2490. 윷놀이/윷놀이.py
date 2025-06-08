import sys
input = sys.stdin.readline
a = []
for i in range(3):
    a.append(list(map(int, input().rstrip().split())))

for i in a:
    count = 0
    for j in i:
        if j == 1:
            count +=1
    if count ==1:
        print('C')
    elif count ==2:
        print('B')
    elif count ==3:
        print('A')
    elif count ==4:
        print('E')
    else:
        print('D')