class Solution {
    /**
     * @param {number[]} nums
     * @return {void} Do not return anything, modify nums in-place instead.
     */
     sortColors(nums) {
        let l = 0;
        let r = nums.length - 1;

        const swap = function(i, j) {
            let tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }

        let i = 0;
        while (i <= r) {
            if (nums[i] === 0) {
                swap(l, i);
                l++;
                i++;
            } else if (nums[i] === 2) {
                swap(i, r);
                r--;
                // don’t increment i here because the new element at i could be 0 or 2
            } else {
                i++;
            }
        }
    }
}