n = int(input())
arr = list(map(int,input().split()))
stack = []
expected = 1

for number in arr:
    stack.append(number)
    while stack and stack[-1] == expected:
        stack.pop()
        expected += 1

if expected == n+1:
    print("Nice")
else:
    print("Sad")