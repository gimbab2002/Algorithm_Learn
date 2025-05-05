import sys
import math

input = sys.stdin.readline().rstrip()
a, b = map(int, input.split())
print(math.gcd(a,b))
print(math.lcm(a,b))