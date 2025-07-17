import sys
import operator
input=sys.stdin.readline

def remove_duplicate(word, w_dict):
    for i in word:
        if i in w_dict:
            w_dict[i]+=1
        else:
            w_dict[i] = 1
    for i, k in w_dict.items():
        if k >1 : 
            word.remove(i)



if __name__ == "__main__" :
    n=int(input().rstrip())
    word = []
    for i in range(n):
        word.append(input().rstrip())
    w_dict = {}
    remove_duplicate(word, w_dict)
    for i in word:
        w_dict[i] = len(i)
    w_dict_arranged = dict(sorted(w_dict.items(), key=operator.itemgetter(1,0)))
    for i in w_dict_arranged.keys():
        print(i)



