import sys
input=sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']

n=int(input().rstrip())
word = []
for i in range(n):
    word.append(input().rstrip())
for i in word:
    count =0
    for j in i:
        if j in vowel:
            count +=1
    print(f'The number of vowels in {i} is {count}.')