import sys

def prime_fact(N):
    while(N != 1):
       for i in range(2, N+1):
           if N%i == 0: 
               print(i)
               N = int(N/i)
               break
    

N = int(sys.stdin.readline().rstrip())
prime_fact(N)