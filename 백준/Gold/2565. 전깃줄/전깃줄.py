# LIS 함수 구하기
def LIS(b_value):
    length = len(b_value)
    dp = [1] * length
    
    for i in range(length):
        for j in range(i):
            if b_value[i] > b_value[j]:
                    dp[i] = max(dp[i],dp[j]+1)
    return max(dp)



# 값 저장하기
pairs = []

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    pairs.append((a, b))

pairs.sort()

b_value = [b for _, b in pairs]

final_result = LIS(b_value)
print(n - final_result)

