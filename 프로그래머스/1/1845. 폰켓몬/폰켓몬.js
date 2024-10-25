function solution(nums) {
    var answer = 0;
    num = ~~(nums.length/2)
    nums_set = [...new Set(nums)]
    answer = nums_set.length > num ? num : nums_set.length
    return answer;
}