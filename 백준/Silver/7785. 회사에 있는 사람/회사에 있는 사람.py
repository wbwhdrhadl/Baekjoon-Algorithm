n = int(input())

arr = set()
for i in range(n):
    name,state = input().split()
    if(state == "enter"):
        arr.add(name)
    else:
        arr.remove(name)

arr_range = sorted(arr,reverse=True)
for i in range(len(arr_range)):
    print(arr_range[i])