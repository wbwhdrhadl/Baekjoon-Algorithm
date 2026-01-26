def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w,h in sizes:
        small = min(w,h)
        big = max(w,h)
        
        max_w = max(max_w, small)
        max_h = max(max_h, big)
        
    return max_w * max_h

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
solution(sizes)
