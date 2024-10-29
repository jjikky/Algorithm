function solution(numbers) {
    const nums_arr = numbers.split("").map((v)=>v)
    const permutations=[]
    for(let i=1; i<=nums_arr.length; i++){
        permutations.push(...getPermutations(nums_arr,i));
    }
    const dup_permutations = [...new Set(permutations.map((v)=>+v.join('')))]
    return dup_permutations.filter((v)=>isPrime(v)).length
}

const getPermutations = function (arr, selectNumber) {
    const results = [];
    // n개중에서 1개 선택할 때(nP1), 바로 모든 배열의 원소 return. 1개선택이므로 순서가 의미없음.
    if (selectNumber === 1) return arr.map((el) => [el]); 
    
    arr.forEach((fixed, index, origin) => {
      // 해당하는 fixed를 제외한 나머지 배열 
      const rest = [...origin.slice(0, index), ...origin.slice(index+1)] 
      // 나머지에 대해서 순열을 구한다.
      const permutations = getPermutations(rest, selectNumber - 1);
      //  돌아온 순열에 떼 놓은(fixed) 값 붙이기
      const attached = permutations.map((el) => [fixed, ...el]);
      // 배열 spread syntax 로 모두다 push
      results.push(...attached); 
    });

    return results;
}
function isPrime(num){
    if(num<2) return false
    for(let i=2; i<=Math.sqrt(num); i++){
        if(num%i==0){
            return false
        }
    }
    return true
}