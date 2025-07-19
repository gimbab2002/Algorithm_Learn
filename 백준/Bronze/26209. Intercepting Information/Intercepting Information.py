import sys
input=sys.stdin.readline

n_arr = list(map(int,input().rstrip().split()))
if 9 in n_arr:
    print("F")
else:
    print("S") 