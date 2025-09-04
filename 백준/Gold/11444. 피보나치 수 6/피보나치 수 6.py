import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def matmul(A,B):
    # 2x2 행렬 구하기
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
         (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
         (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]

def matpow(A, n):
    result = [[1, 0], [0, 1]]  # 항등행렬
    base = [[A[0][0], A[0][1]], [A[1][0], A[1][1]]]
    while n > 0:
        if n % 2 == 1:
            result = matmul(result, base)
        base = matmul(base, base)
        n //= 2
    return result


def fibonacci(n):
    # n번째 피보나치 수
    if n == 0:
        return 0
    A = [[1,1],[1,0]]
    res = matpow(A,n-1)
    return res[0][0] % MOD

n = int(input())
print(fibonacci(n))