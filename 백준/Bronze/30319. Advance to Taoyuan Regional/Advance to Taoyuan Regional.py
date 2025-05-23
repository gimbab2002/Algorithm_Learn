import sys
input=sys.stdin.readline

year, month, day=map(int, input().split('-'))

if month < 9:
    print("GOOD")
elif month ==9 and day <= 16:
    print("GOOD")
elif month ==9 and day > 16:
    print("TOO LATE")
elif month >=10:
    print("TOO LATE") 
