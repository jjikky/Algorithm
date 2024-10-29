function solution(answers) {
    const p1 = [1, 2, 3, 4, 5];
    const p2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    let result = [0, 0, 0];

    // 각 수포자의 패턴을 순환하며 정답 비교
    answers.forEach((v, i) => {
        if (v === p1[i % p1.length]) result[0] += 1;
        if (v === p2[i % p2.length]) result[1] += 1;
        if (v === p3[i % p3.length]) result[2] += 1;
    });

    const maxScore = Math.max(...result);
    // 최댓값을 가진 인덱스를 반환
    return result.map((score, index) => score === maxScore ? index + 1 : null).filter(v => v !== null);
}
