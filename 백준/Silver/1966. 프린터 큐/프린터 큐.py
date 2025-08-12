import sys
input=sys.stdin.readline

case_num = int(input().rstrip())
result = []
for i in range(case_num):
    n, m = map(int, (input().rstrip().split()))
    que= list(map(int, input().rstrip().split()))
    que_num = que[m]
    order = 1
    while que:
        j=0
        flag = 0
        if len(que)==1:
            result.append(order)
            break
        for k in range(j+1, len(que)):
            if que[j] < que[k]:
                flag = 1
                break
        if flag:
            if j == m:
                m=len(que)
            num = que.pop(j)
            que.append(num)
            m=m-1
        else:
            if j == m:
                result.append(order)
                break
            que.pop(j)
            m=m-1
            order+=1





print(*result, sep='\n')