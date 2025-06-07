import sys
input=sys.stdin.readline

a,b,c=map(int, input().rstrip().split())

furiosa = b//a * 3
furiosa = furiosa * c
print(furiosa)