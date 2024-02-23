def solution(k, m, score):
    answer = 0
    score.sort()
    while len(score)>=m:
        min=k
        for i in range(m):
            v = score.pop()
            if v<min:
                min=v
        answer+=min*m
    return answer