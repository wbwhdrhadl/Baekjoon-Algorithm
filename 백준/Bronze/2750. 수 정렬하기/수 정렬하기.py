n = int(input())

arr = []
for i in range(n):
    num = int(input())
    arr.append(num)

sort_arr = sorted(arr)

for i in range(len(sort_arr)):
    print(sort_arr[i])
    
            