def solution(spell, dic):
    answer = 2
    spell=sorted(spell);
    for i in dic:
        if sorted(i)==spell:
            answer=1
        
    return answer