from collections import Counter

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

answer = Counter(a)
for num in b:
    print(answer.get(num,0), end =" ")
