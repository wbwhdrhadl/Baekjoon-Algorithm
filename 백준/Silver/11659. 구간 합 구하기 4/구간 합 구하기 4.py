# 기본 인수 받기
n, m = map(int,input().split())

nums = list(map(int,input().split()))
sum_nums = [0]
for i in range(n):
    sum_nums.append(sum_nums[i]+nums[i])

# # 부분합 함수 구현
def part_sum(a, b):
    print(sum_nums[b]-sum_nums[a-1])
        


for i in range(m):
    a, b = map(int,input().split())
    part_sum(a,b)