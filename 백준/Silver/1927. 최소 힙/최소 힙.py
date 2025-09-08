import sys
input = sys.stdin.readline

# min_heap 구현하기
# min_heap 원소 넣기
def min_insert(x,min_array):
    min_array.append(x)
    position = len(min_array)-1
    while position > 0:
        parent = (position - 1) // 2
        if min_array[position] < min_array[parent]:
            temp = min_array[position]
            min_array[position] = min_array[parent]
            min_array[parent] = temp
            position = parent
        else:
            break

    
# min_heap 원소 출력
def min_heap(min_array):
    if not min_array:
        return 0
    if len(min_array) == 1:
        return min_array.pop()
    
    root = min_array[0]
    min_array[0]= min_array.pop()
    position = 0
    size = len(min_array)
    while True:
        left = position * 2 + 1
        right = position * 2 + 2
        smallest = position

        if left < size and min_array[position] > min_array[left]:
            smallest = left
        if right < size and min_array[smallest] > min_array[right]:
            smallest = right

        if position != smallest:
            min_array[position], min_array[smallest] = min_array[smallest], min_array[position]
            position = smallest
        else:
            break
            

    return root
    


# 입력받기
n = int(input())
min_array = []
for i in range(n):
    x = int(input())
    if x == 0:
        print(min_heap(min_array))
    else:
        min_insert(x, min_array)
        