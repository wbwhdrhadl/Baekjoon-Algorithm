import sys

input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
count = [0] * 10001

for _ in range(n):
    num = int(input())
    count[num] += 1

# 안전하게 출력 (한 줄씩)
for i in range(10001):
    for _ in range(count[i]):
        write(f"{i}\n")
