import sys
input=sys.stdin.readline

sentence = []
sentence.append(input().rstrip())
while sentence[-1] != '.':
    sentence.append(input().rstrip())
    

stack=[]
result = []
for i in sentence:
    if i == '.':
        break
    for j in i:
        if j == '(' or j == '[':
            if j=='(':
                stack.append('(')
            elif j == '[':
                stack.append('[')
        if j == ')' or j == ']':
            if not stack:
                result.append('no')
                result.append('1')
                break
            if j == ')':
                try:
                    if stack[-1] == '(':
                        stack.pop(-1)
                    elif stack[-1] == '[':
                        result.append('no')
                        result.append('1')
                        break
                except:
                    continue
            elif j == ']':
                try:
                    if stack[-1] == '[':
                        stack.pop(-1)
                    elif stack[-1] == '(':
                        result.append('no')
                        result.append('1')
                        break
                except:
                    continue
    try:
        if result[-1] == '1':
            result.pop(-1)
            stack = []
            continue
    except:
        None
    if stack:
        result.append('no')
    else:
        result.append('yes')
    stack = []

for i in result:
    if i == '1':
        continue
    print(i)