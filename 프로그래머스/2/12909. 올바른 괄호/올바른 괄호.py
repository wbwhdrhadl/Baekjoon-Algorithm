def solution(s):
    stack = []
    answer = True
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        elif s[i] == ")":

            if len(stack) == 0:
                answer = False
            else:
                stack.pop()

    if len(stack)!=0:
        answer = False
    return answer