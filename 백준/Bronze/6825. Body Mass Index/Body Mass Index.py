import sys

input=sys.stdin.readline

weight = float(input().rstrip())
height = float(input().rstrip())

bmi = weight / (height*height)

if bmi > 25:
    print('Overweight')
elif bmi < 18.5:
    print('Underweight')
else: 
    print("Normal weight")