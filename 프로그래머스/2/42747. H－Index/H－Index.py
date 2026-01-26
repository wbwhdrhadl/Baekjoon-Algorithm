def solution(citations):
    citations.sort(reverse=True)
    h = 0
    
    for c in citations:
        if c >= h + 1:
            h += 1
        else:
            break
            
    return h
            
    
citations = [3, 0, 6, 1, 5] # [0,1,3,5,6]
solution(citations)
