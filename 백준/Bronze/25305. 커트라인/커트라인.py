n, k = map(int,(input().split()))

arr = list(map(int,input().split()))

sort_arr = list(reversed(sorted(arr)))


print(sort_arr[k-1])