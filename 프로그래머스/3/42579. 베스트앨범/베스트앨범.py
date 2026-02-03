from collections import defaultdict
def solution(genres, plays):
    genre_songs = defaultdict(list)
    genre_total = defaultdict(int)
    answer = []
    
    for i in range(len(genres)): 
        genre_songs[genres[i]].append((plays[i],i))
        genre_total[genres[i]]+=plays[i]
        
    sorted_genres = sorted(genre_total.keys(), key=lambda x: genre_total[x], reverse=True)
    
    for g in sorted_genres:
        songs = sorted(genre_songs[g], key = lambda x: (-x[0],x[1]))
        
        for play, idx in songs[:2]:
            answer.append(idx)
            
    return answer
    
    print(sorted_genres)
        
    
    return 0

genres = ["classic", "pop", "classic", "classic", "pop"]

plays = [500, 600, 150, 800, 2500]
solution(genres,plays)