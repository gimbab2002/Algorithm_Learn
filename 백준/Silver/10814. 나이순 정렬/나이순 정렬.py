import sys
input=sys.stdin.readline
n=int(input().rstrip())
people=[]

def merge_sort(unsorted_list):
    # 크기가 1이하면 반환
    if len(unsorted_list) <= 1:
        return unsorted_list
     
    # 리스트를 2분할
    mid = len(unsorted_list)//2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]
    
    # 2분할한 리스트를 각각 merge sort진행
    left_ = merge_sort(left)
    right_ = merge_sort(right)
    return merge(left_, right_)

def merge(left, right):
    i, j = 0,0
    sorted_list = []
    
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list

for i in range(n):
    age_name = input().rstrip().split()
    key = int(age_name[0])
    value = age_name[1]
    people.append((key, value))

people_sorted = merge_sort(people)

for i in people_sorted:
    print(i[0], end=' ')
    print(i[1], end = '\n')