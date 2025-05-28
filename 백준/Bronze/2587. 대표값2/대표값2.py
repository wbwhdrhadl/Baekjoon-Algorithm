arr = []
for i in range(5):
    num = int(input())
    arr.append(num)

sort_arr = sorted(arr)

avg=0
for i in range(len(sort_arr)):
    avg+=sort_arr[i]

print(avg//5)
print(sort_arr[2])
            