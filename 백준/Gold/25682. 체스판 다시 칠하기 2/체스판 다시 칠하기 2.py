# 입력받기
n,m,k = map(int,input().split())
line = [list(input().strip()) for _ in range(n)]

# 체스판 기준 보드 생성
board1 = [[0]*m for _ in range(n)]
board2 = [[0]*m for _ in range(n)]

# 보드 기준으로 true, false 생성
for i in range(n):
    for j in range(m):
        expected1 = 'W' if (i+j)%2 == 0 else 'B'
        expected2 = 'B' if (i+j)%2 == 0 else 'W'
        
        if line[i][j] != expected1:
            board1[i][j] = 1
        if line[i][j] != expected2:
            board2[i][j] = 1

# 누적합 구하는 함수
def sum_max(board):
    n, m = len(board), len(board[0])
    psum = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            psum[i+1][j+1] = (board[i][j] + psum[i][j+1] + psum[i+1][j] - psum[i][j])
            
    return psum

# 특정 범위의 누적합 구하기
def get_sum(psum,x1,y1,x2,y2):
    return psum[x2][y2] - psum[x1][y2] - psum[x2][y1] + psum[x1][y1]

# 누적합 생성
psum1 = sum_max(board1)
psum2 = sum_max(board2)

min_num = float('inf')
for i in range(n - (k-1)):
    for j in range(m - (k-1)):
        cnt1 = get_sum(psum1, i,j,i+k,j+k)
        cnt2 = get_sum(psum2, i,j,i+k,j+k)
        min_num = min(min_num, cnt1,cnt2)

print(min_num)

            