def solution(phone_book):
    s = set(phone_book)
    
    for num in phone_book:
        for i in range(1,len(num)):
            prefix = num[:i]
            if prefix in s:
                return False
    return True