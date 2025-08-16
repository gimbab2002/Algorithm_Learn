import sys

input=sys.stdin.readline
n, m = map(int, input().rstrip().split())
listen = []
see = []

for i in range(n):
    listen.append(input().rstrip())
for i in range(m):
    see.append(input().rstrip())

set_listen = set(listen)
set_see = set(see)
listen_and_see = list(set_listen&set_see)
listen_and_see.sort()
print(len(listen_and_see))
print(*listen_and_see, sep='\n')