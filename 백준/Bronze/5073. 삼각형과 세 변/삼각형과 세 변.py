import sys
input=sys.stdin.readline

edge = []
edge.append(list(map(int, input().rstrip().split())))


while edge[-1] != [0,0,0]:
    edge.append(list(map(int, input().rstrip().split())))
for i in edge:
    s1, s2, s3 = i
    if not s1 and not s2 and not s3:
        break
    if max(i) * 2 < sum(i):
        if s1 == s2 and s2 == s3:
            print("Equilateral") 
        elif s1 == s2 or s2 == s3 or s1 == s3:
            print("Isosceles") 
        else: 
            print("Scalene") 
    else:
        print("Invalid") 

    