import sys
input = sys.stdin.readline

def min_insert(x, min_array):
    min_array.append(x)
    position = len(min_array) - 1
    parent = (position - 1) // 2

    while position > 0 and (abs(min_array[position]), min_array[position]) < (abs(min_array[parent]), min_array[parent]):
        min_array[position], min_array[parent] = min_array[parent], min_array[position]
        position = parent
        parent = (position - 1) // 2


def min_abs(min_array):
    if not min_array:
        return 0
    if len(min_array) == 1:
        return min_array.pop()

    root = min_array[0]
    min_array[0] = min_array.pop()
    size = len(min_array)
    position = 0

    while True:
        left = position * 2 + 1
        right = position * 2 + 2
        smallest = position

        if left < size and (abs(min_array[left]), min_array[left]) < (abs(min_array[smallest]), min_array[smallest]):
            smallest = left
        if right < size and (abs(min_array[right]), min_array[right]) < (abs(min_array[smallest]), min_array[smallest]):
            smallest = right

        if smallest != position:
            min_array[position], min_array[smallest] = min_array[smallest], min_array[position]
            position = smallest
        else:
            break

    return root


n = int(input())
min_array = []
results = []   # 결과 모아두기

for _ in range(n):
    x = int(input())
    if x == 0:
        results.append(str(min_abs(min_array)))
    else:
        min_insert(x, min_array)

# 한 번에 출력
sys.stdout.write("\n".join(results))
