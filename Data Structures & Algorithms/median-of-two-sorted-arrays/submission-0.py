class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        p1, p2, m1, m2 = 0, 0, 0, 0
        
        for _ in range((m + n) // 2 + 1):
            m2 = m1
            if p1 < m and (p2 >= n or nums1[p1] < nums2[p2]):
                m1 = nums1[p1]
                p1 += 1
            else:
                m1 = nums2[p2]
                p2 += 1
                
        if (m + n) % 2 == 1:
            return float(m1)
        return (m1 + m2) / 2.0
