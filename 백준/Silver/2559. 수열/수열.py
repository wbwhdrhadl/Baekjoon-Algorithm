# 입력받기
n, k = map(int,input().split())
temp = list(map(int,input().split()))


# 부분합 배열 만들기
sum_temp = [0]
for i in range(n):
    sum_temp.append(sum_temp[i] + temp[i])



# 정답 구하는 함수
def ans_fun(k):
    ans_temp = []
    for i in range(k,n+1):
        ans_temp.append(sum_temp[i]-sum_temp[i-k])

    result = max(ans_temp)

    print(result)

# 함수실행
ans_fun(k)