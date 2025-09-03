import sys
input=sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0 for _ in range(n+1)]
visited[0]=1
stack = []
count = 0
while 0 in visited:
    stack.append(visited.index(0))
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            stack.extend(graph[node])
            stack.sort(reverse=True)
    count += 1
print(count)