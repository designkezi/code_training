# https://programmers.co.kr/learn/courses/30/lessons/42579

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    songArrayByGenre = dict()
    sumGenreSong = dict()
        
    for idx, val in enumerate(genres):
        if val in sumGenreSong:
            songArrayByGenre[val].append((plays[idx], idx))
            sumGenreSong[val] += plays[idx]
        else:
            songArrayByGenre[val] = list()
            songArrayByGenre[val].append((plays[idx], idx))
            sumGenreSong[val] = plays[idx]
    
    genreOrder = sorted(sumGenreSong.items(), key = lambda x : (-x[1], x[0]))

    for genre in genreOrder:
        tempList = songArrayByGenre[genre[0]]
        tempList = sorted(tempList, key = lambda x : (-x[0], x[1]))
        for song in tempList[0:2]:
            answer.append(song[1])

    return answer
