n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

arr_map = set(arr)

for num in arr2:
    if num in arr_map:
        print(1, end=" ")
    else:
        print(0, end=" ")