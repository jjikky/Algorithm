def solution(babbling):
    answer = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            answer += 1
    return answer