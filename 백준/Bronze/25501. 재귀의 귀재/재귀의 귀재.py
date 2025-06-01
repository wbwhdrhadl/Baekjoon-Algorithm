t = int(input())

def recursion(s, l, r, sum):
    if(l>=r):
        sum+=1
        return 1, sum
    elif(s[l] != s[r]):
        sum+=1
        return 0, sum
    else:
        sum+=1
        return recursion(s, l+1, r-1, sum)


def isPalindrome(s):
    sum = 0
    return recursion(s, 0 ,len(s)-1,sum)
    

for i in range(t):
    str = input()
    result, sum = isPalindrome(str)
    print(result, sum)