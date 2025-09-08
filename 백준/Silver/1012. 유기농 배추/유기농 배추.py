import sys
input=sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(bachu, x, y): #x: 세로, y: 가로
    q=deque()
    q.append([x,y])
    bachu[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or ny >= m or nx >= n:
                continue
            if bachu[nx][ny] ==1:
                q.append([nx, ny])
                bachu[nx][ny]=0
    return







t=int(input().rstrip())
for _ in range(t):
    m, n, k = map(int, input().rstrip().split())
    bachu = [[0 for _ in range(m)] for i in range(n)]

    for _ in range(k):
        x,y = map(int, input().rstrip().split())
        bachu[y][x] = 1
    count = 0
    for j in range(n): #세로
        for k in range(m): #가로
            if bachu[j][k]==1:
                bfs(bachu, j, k) #세로, 가로 인자
                count+=1
    print(count)