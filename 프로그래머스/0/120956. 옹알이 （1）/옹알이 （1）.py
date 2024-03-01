from itertools import permutations
def solution(babbling):
    answer = 0
    data=["aya", "ye", "woo", "ma"]
    result = data+list(map(lambda x:x[0]+x[1],list(permutations(data,2))))+list(map(lambda x:x[0]+x[1]+x[2],list(permutations(data,3))))+list(map(lambda x:x[0]+x[1]+x[2]+x[3],list(permutations(data,4))))
    for b in babbling:
        for r in result:
            if b==r:
                answer+=1
                break
    return answer