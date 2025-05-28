import sys
n = int(input())
arr = list(map(int, sys.stdin.read().split()))
# for i in range(n):
#     num = int(input())
#     arr.append(num)

sort_list = sorted(arr)
for i in range(len(sort_list)):
    print(sort_list[i])

