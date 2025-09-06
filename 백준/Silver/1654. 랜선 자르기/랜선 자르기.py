import sys
input = sys.stdin.readline

# 함수작성
def binary_separate(lane_array,m):
    right = max(lane_array)
    left = 1
    lane_len = 0
    while(left <= right):
        lane_sum = 0
        mid = (left + right) // 2
        array_len = len(lane_array)
        for i in range (0,array_len):
            lane_sum += lane_array[i] // mid
            
        if lane_sum >= m:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

# 입력받기
n, m = map(int,input().split())
lane_array = []
for i in range(n):

    
    length = int(input())
    lane_array.append(length)
    
answer = binary_separate(lane_array,m)
print(answer)