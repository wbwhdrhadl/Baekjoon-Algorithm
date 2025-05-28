n = int(input())
num = list(map(int,input().split()))

sort_num = sorted(set(num))

compressed = {}


for index,value in enumerate(sort_num):
    compressed[value]= index

for x in num:
    print(compressed[x], end=' ')