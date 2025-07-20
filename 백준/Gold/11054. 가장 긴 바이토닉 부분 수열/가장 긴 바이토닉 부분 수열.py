n = int(input())
arr = list(map(int, input().split()))

# LIS(왼쪽에서 증가하는 부분 수열)
LIS = [1] * n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            LIS[i] = max(LIS[i], LIS[j] + 1)

# LDS(오른쪽에서 감소하는 부분 수열 길이)
LDS = [1] * n
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if arr[j] < arr[i]:
            LDS[i] = max(LDS[i], LDS[j] + 1)

# 총길이 계산
result = 0
for i in range(n):
    result = max(result, LIS[i]+LDS[i]-1)

print(result)
