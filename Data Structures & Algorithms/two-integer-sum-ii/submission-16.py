class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        

        l , r = 0, len(numbers)-1
        while l < r:
            curr = numbers[l] + numbers[r]
            if curr < target:
                l += 1   
            elif curr > target:
                r -= 1
            else:
                return [l+1, r+1]
