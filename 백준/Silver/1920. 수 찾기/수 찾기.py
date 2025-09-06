from collections import Counter

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

answer = Counter(a)
for num in b:
    value = int(answer.get(num,0))
    if value >= 1:
        print("1")
    else:
        print("0")