import sys
input = sys.stdin.readline

fibo = []
fibo.append(0)
fibo.append(1)
n = int(input())

def fibonacci(n, fibo) :
    for i in range (2, n+1):
        fibo.append(fibo[i-1] + fibo [i-2])

fibonacci(n, fibo)
print(fibo[n])