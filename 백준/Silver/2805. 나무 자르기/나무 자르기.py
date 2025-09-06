import sys
input = sys.stdin.readline

# 함수작성
def binary_separate(lane_array,m):
    right = max(lane_array)
    left = 1
    lane_len = 0
    result = 0
    while(left <= right):
        lane_sum = 0
        mid = (left + right) // 2
        array_len = len(lane_array)
        for i in range (0,array_len):
            if lane_array[i] > mid:
                lane_sum += lane_array[i] - mid
        if lane_sum >= m :
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

# 입력받기
n, m = map(int,input().split())
lane_array = list(map(int,input().split()))
answer = binary_separate(lane_array,m)
print(answer)