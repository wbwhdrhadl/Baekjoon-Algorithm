n = int(input())
a = list(map(int,input().split()))

sub = []

for x in a:
    left, right = 0, len(sub) - 1
    pos = len(sub)

    while left <= right:
        mid = (left + right) // 2
        if sub[mid] >= x:
            pos = mid
            right = mid - 1
        else:
            left = mid + 1


    if pos == len(sub):
        sub.append(x)

    else:
        sub[pos] = x

print(len(sub))
