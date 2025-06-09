n,m = map(int,input().split())
arr = []
for i in range(n):
    a = i+1
    arr.append(a)
for i in range(m):
    a, b = map(int,input().split())
    arr[a-1:b] = reversed(arr[a-1:b])

print(*arr)