import sys
input=sys.stdin.readline

n=int(input().rstrip())
sentence = []
for _ in range(n):
    sentence.append(list(input().rstrip().split()))
    count = 0
    for i in range(len(sentence[-1])):
        if count == 2:
            break
        count+=1
        back = sentence[-1].pop(0)
        sentence[-1].append(back)
for i in sentence:
    print(*i, sep = ' ')