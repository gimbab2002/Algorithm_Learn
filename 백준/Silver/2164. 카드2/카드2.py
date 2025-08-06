import queue
import sys

input=sys.stdin.readline

n=int(input().rstrip())
que = queue.Queue()
for i in range(1, n+1, 1):
    que.put(i)
while que.qsize() >1 :
    que.get()
    que.put(que.get())
print(que.get())