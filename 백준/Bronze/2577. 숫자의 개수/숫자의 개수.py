import sys
input=sys.stdin.readline

a = int(input().rstrip())
b = int(input().rstrip())
c = int(input().rstrip())

d = str(a*b*c)

print(d.count('0'))
print(d.count('1'))
print(d.count('2'))
print(d.count('3'))
print(d.count('4'))
print(d.count('5'))
print(d.count('6'))
print(d.count('7'))
print(d.count('8'))
print(d.count('9'))

    