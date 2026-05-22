class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        const arr = []
        for (let i=0; i < nums.length; i++){
            arr.push(nums[i])
        }
        return nums.concat(arr)
    }
}
