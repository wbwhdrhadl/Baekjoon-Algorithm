n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

min_price = price[0]
sum_price = 0
for i in range(len(price)-1):
    if min_price > price[i]:
        min_price = price[i]
        
    sum_price+= min_price * distance[i]

print(sum_price)