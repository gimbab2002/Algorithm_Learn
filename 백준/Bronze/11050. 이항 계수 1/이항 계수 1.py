import math
import sys
input=sys.stdin.readline

n, k = map(int, input().rstrip().split())
result = math.comb(n,k)
print(result)