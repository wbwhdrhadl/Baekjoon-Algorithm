# 입력 형식 지정
import sys
input = sys.stdin.readline

# 입력받기
n_array = []
n, m = map(int, input().split())

for i in range(n):
    array = list(map(int,input().split()))
    n_array.append(array)
    
# dp 정의하기
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = n_array[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

# sum 계산 함수 정의
def sum_xy(x1,y1,x2,y2):
    sum = dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1])
    print(sum)

# 함수 불러오기
for j in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    sum_xy(x1,y1,x2,y2)
    

