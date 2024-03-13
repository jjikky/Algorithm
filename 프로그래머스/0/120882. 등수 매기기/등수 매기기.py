def solution(score):
    answer = [1]*len(score)
    score=list(map(sum,score))
    for i in range(len(score)):
        for j in range(len(score)):
            if score[i]<score[j]:
                answer[i]+=1
    return answer