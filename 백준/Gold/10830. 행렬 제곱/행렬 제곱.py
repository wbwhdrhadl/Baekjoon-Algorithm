import sys
input = sys.stdin.readline

# 행렬곱셈
def mul_matrix(result, array):
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                answer[i][j] += result[i][k] * array[k][j]
            answer[i][j] %=1000
    return answer
    

# 행렬 여러번 곱하기
def mul_power(matrix,b):
    result = [[int(i == j) for j in range(n)] for i in range(n)]  # 단위행렬
    while b > 0:
        if b %2 ==1:
            result = mul_matrix(result, matrix)
        matrix = mul_matrix(matrix,matrix)
        b //= 2
    return result
        

# 입력받기
n,b = map(int,input().split())
array = []
for i in range(n):
    a1 = list(map(int,input().split()))
    array.append(a1)
    
final_result = mul_power(array,b)
for row in final_result:
    print(' '.join(map(str,row)))

    