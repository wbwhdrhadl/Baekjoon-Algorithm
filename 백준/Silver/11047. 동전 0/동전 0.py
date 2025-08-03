# 입력받기
n, k = map(int,input().split())
money = []
for i in range(n):
    coin = int(input())
    money.append(coin)

money.sort(reverse=True)

# 총 개수 구하기
count = 0

for coin in money:
    while k >= coin:
        count += 1
        k -= coin

print(count)
    