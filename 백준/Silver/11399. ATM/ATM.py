# 입력받기
n = int(input())
min = list(map(int, input().split()))

# 인출 배열 오름차순 정렬
min.sort()
# 인출 최솟값 구하기
sum_count = 0
sum_value = 0

for i in min:
    sum_count+= i
    sum_value+= sum_count

print(sum_value)