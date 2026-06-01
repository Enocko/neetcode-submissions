class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        full = len(A) + len(B)
        half = full // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A)-1
        while True:
            m = (l + r) // 2
            i = half - m - 2

            Aleft = A[m] if m >= 0 else float('-inf')
            Aright = A[m+1] if (m+1) < len(A) else float('inf') 
            Bleft = B[i] if i >= 0 else float('-inf')
            Bright = B[i+1] if (i+1) < len(B) else float('inf') 

            if Aleft <= Bright and Bleft <= Aright:
                if full % 2 != 0:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1





"""
A, B = nums1, nums2
full = len(A) + len(B)
half = full // 2

if len(A) > len(B):
    A, B = B, A

l, r = 0, len(A)-1
while True:
    m = (l + r) // 2
    i = half - m - 2

    Aleft = A[m] if m >= 0 else float('-inf')
    Aright = A[m+1] if (m+1) < len(A) else float('inf') 
    Bleft = B[i] if i >= 0 else float('-inf')
    Bright = B[i+1] if (i+1) < len(B) else float('inf) 

    if Aleft <= Bright and Bleft <= Aright:
        if full % 2 != 0:
            return min(Aright, Bright)
        else:
            return (max(A[left], B[left]) + min(A[right], B[right])) / 2

    elif Aleft > Bright:
        r = m - 1
    else:
        l = m + 1








"""