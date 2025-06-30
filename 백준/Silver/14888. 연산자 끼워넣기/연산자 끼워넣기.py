import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
operator = list(map(int,input().split()))
min_result = float('inf')
max_result = float('-inf')

def backtracking(index, current_value, add, sub, mul, div):
    global min_result, max_result
    
    if(index == N):
        min_result = min(min_result,current_value)
        max_result = max(max_result,current_value)
        return
    num = A[index]

    if add > 0:
        backtracking(index+1, current_value + num, add - 1,sub,mul,div)
    if sub > 0:
        backtracking(index+1, current_value - num,add,sub - 1,mul,div)
    if mul > 0:
        backtracking(index+1, current_value * num,add,sub,mul -1,div)
    if div > 0:
        if current_value < 0:
            backtracking(index+1, -(-current_value // num), add, sub, mul, div - 1)
        else:
            backtracking(index+1, current_value // num, add, sub, mul, div - 1)


backtracking(1,A[0],operator[0], operator[1],operator[2],operator[3])
print(max_result)
print(min_result)
