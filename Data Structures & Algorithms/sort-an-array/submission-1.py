class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        m = len(nums)//2
        l = self.sortArray(nums[:m])
        r = self.sortArray(nums[m:])
        return self.mergeSort(l,r)
    
    def mergeSort(self, l, r):
        sortedList = []
        i,j = 0,0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                sortedList.append(l[i])
                i += 1
            else:
                sortedList.append(r[j])
                j += 1
        
        sortedList += l[i:]
        sortedList += r[j:]

        return sortedList