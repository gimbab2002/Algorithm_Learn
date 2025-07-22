import sys
input=sys.stdin.readline

N=int(input().rstrip())
people=[]
for i in range(N):
    people.append(tuple(map(int, input().rstrip().split())))

rank=[]
for i in range(0, len(people)):
    count=1
    for j in range(0, len(people)):
        if i == j: continue
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count+=1
    rank.append(count)
print(*rank)