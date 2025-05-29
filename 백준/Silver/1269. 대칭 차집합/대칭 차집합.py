n, m = map(int,input().split())
a = input().split()
b = input().split()
a_list = set(a)
b_list = set(b)

# 집합의 차집합 연산
a_sum = a_list - b_list
b_sum = b_list - a_list
print(len(a_sum) + len(b_sum))
    