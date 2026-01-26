import sys
input = sys.stdin.readline

def solution(nums):
    total_count = 0
    unique_arr = set(nums)
    max_n = len(nums)//2

    if len(unique_arr) >= max_n:
        total_count = max_n
    else:
        total_count = len(unique_arr)

    return total_count

nums = [3,1,2,3]
solution(nums)