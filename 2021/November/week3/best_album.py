def solution(genres, plays):
    answer = []
    hash_genre = {}
    song_index_to_plays = {}
    hash_genre_to_songs = {}
    for i, genre in enumerate(genres): # 장르 : [몇번 인덱스 곡인지]  ans  3번 인덱스 플레이횟수 : 3번곡 인덱스
        if hash_genre.get(genre, 0):
            hash_genre[genre].append(i)
            song_index_to_plays[i] = plays[i]
            hash_genre_to_songs[genre][i] = plays[i]
        else:
            hash_genre[genre] = [i]
            song_index_to_plays[i] = plays[i]
            hash_genre_to_songs[genre] = {}
            hash_genre_to_songs[genre][i] = plays[i]

    order = []
    # 속한 노래가 가장 많이 재생된 장르를 먼저 수록 ( 장르 순 )
    for k, v in hash_genre.items():
        total = 0
        for i in v: # 인덱스가 나옴
            total += song_index_to_plays[i]
        order.append([k, total])
    oreder = sorted(order, key=lambda x: x[1], reverse=True) # total 의 크기가 큰 순으로 리스트가 정렬되엇음

    # 장르 내에서 가장 많이 재생된 노래를 먼저 수록 ( 노래 2개 순서대로 뽑기 ) -> 여긴 되게 빨리 끝날듯? -> 장르: {인덱스: 플레이수, 인덱스 ... 로 묶는게 있었어야 함
    for genre in oreder:
        songs = hash_genre_to_songs[genre[0]] # 인덱스: 플레이수 의 딕셔너리 반환
        # 딕셔너리 sort 필요
        songs = sorted(songs.items(), key=lambda x: x[1], reverse=True) # 플레이순으로 정렬된 상태 [(), () ..]
        fin = [i[0] for i in songs]
        answer.extend(fin[:2])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))