n = list(map(int,input().strip()))

a = list(reversed(sorted(n)))

for i in range(len(a)):
    print(a[i], end="")