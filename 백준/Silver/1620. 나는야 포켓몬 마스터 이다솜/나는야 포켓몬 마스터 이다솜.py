n,m = map(int,input().split())

name_arr = {}
index_arr = {}

for i in range(1,n+1):
    name = input()
    name_arr[name]=i
    index_arr[i]=name

for j in range(m):
    word = input()
    if(word.isdigit()):
        idx = int(word)
        print(index_arr[idx])

    else:
        print(name_arr[word])