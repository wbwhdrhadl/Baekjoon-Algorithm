import sys
input = sys.stdin.readline

# 최대힙 구현하기
def heap_insert(x, heap_array):
    heap_array.append(x)
    position = len(heap_array) - 1
    while position > 0:
        parent = (position-1) // 2 
        if heap_array[parent] < heap_array[position]:
            temp = heap_array[parent]
            heap_array[parent] = heap_array[position]
            heap_array[position] = temp
            position = parent
        else:
            break
        

def heap_delete(heap_array):
    if not heap_array:
        return 0
    if len(heap_array) == 1:
        return heap_array.pop()

    root = heap_array[0]
    heap_array[0] = heap_array.pop()
    position = 0
    size = len(heap_array)

    while True:
        left = position * 2 + 1
        right = position * 2 + 2
        largest = position

        if left < size  and heap_array[left] > heap_array[largest]:
            largest = left
        if right < size and heap_array[right] > heap_array[largest]:
            largest = right

        if largest != position:
            heap_array[position], heap_array[largest] = heap_array[largest], heap_array[position]
            position = largest

        else:
            break
            
    return root
        
# 입력받기
n = int(input())
heap_array = []
for i in range(n):
    x = int(input())
    if (x > 0):
        heap_insert(x, heap_array)
    else:
        print(heap_delete(heap_array))
        