class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hash = new Set()
        for (let i=0; i < nums.length; i++){
            hash.add(nums[i])
        }

        return nums.length != hash.size
    }
}
