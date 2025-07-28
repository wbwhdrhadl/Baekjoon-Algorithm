import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())

# 누적 빈도 배열
arr = [[0] * 26 for _ in range(len(s))]

for i in range(len(s)):
    if i > 0:
        arr[i] = arr[i-1][:]
    idx = ord(s[i]) - ord('a')
    arr[i][idx] += 1

# 출력 결과 저장용 리스트
results = []

def num_alpha(alpha, start, end):
    idx = ord(alpha) - ord('a')
    if start > 0:
        return arr[end][idx] - arr[start-1][idx]
    else:
        return arr[end][idx]

for _ in range(n):
    alpha, start, end = input().split()
    start = int(start)
    end = int(end)
    results.append(str(num_alpha(alpha, start, end)))

# 한 번에 출력
print('\n'.join(results))
