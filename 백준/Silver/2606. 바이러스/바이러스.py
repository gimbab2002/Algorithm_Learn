import sys
input=sys.stdin.readline

n = int(input().rstrip())
connection = int(input().rstrip())
network = [[0 for _ in range(n)] for _ in range(n)]
for i in range(connection):
    a, b = map(int, input().rstrip().split())
    network[a-1][b-1] = 1
    network[b-1][a-1] = 1

stack = [0]
count = 0
visited = [0 for _ in range(n)]
while stack :
    computer = stack.pop()
    if not visited[computer]:
        visited[computer] = 1
        count+=1
        for i in range(len(network[computer])-1, -1, -1):
            if network[computer][i] == 1 and not visited[i]:
                stack.append(i)
print(count-1)
