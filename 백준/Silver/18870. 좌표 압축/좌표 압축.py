import sys
input=sys.stdin.readline

n = int(input().rstrip())
coordinate = list(map(int, input().rstrip().split()))
coordinate_unique = sorted(set(coordinate))

dic = {}
for index, value in enumerate(coordinate_unique):
    dic[value] = index
print(" ".join(str(dic[num]) for num in coordinate))