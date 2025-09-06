import sys
input = sys.stdin.readline

def can_install(wifi_array, mid, c):
    count = 1
    last_installed = wifi_array[0]
    for i in range(1, len(wifi_array)):
        if wifi_array[i] - last_installed >= mid:
            count += 1
            last_installed = wifi_array[i]
    return count >= c

def closest_wifi(wifi_array, m):
    left = 1
    right = wifi_array[-1] - wifi_array[0]
    distance = 0
    while left <= right:
        mid = (left + right) // 2
        if can_install(wifi_array, mid, m):
            distance = mid
            left = mid + 1
        else:
            right = mid - 1
    return distance

n, m = map(int, input().split())
wifi_array = [int(input()) for _ in range(n)]
wifi_array.sort()
print(closest_wifi(wifi_array, m))
