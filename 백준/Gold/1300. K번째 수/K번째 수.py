n = int(input())
k = int(input())

def count_less(num):
    cnt = 0
    for r in range(1, n+1):
        cnt += min(n, (num-1) // r)
    return cnt

answer = 0 
left, right = 1, n*n

while left <= right:
    mid = (left + right) // 2
    cnt = count_less(mid)
    if cnt <= k - 1:
        answer = max(answer,mid)
        left = mid + 1
    elif cnt > k - 1:
        right = mid - 1

print(answer)
        