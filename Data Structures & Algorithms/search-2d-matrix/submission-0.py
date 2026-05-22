class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for n in matrix:
            for k in n:
                if k == target:
                    return True
    

        return False
        