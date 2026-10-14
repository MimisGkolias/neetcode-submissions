class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A = nums2
            B = nums1
        
        total_length = (len(nums1) + len(nums2))
        middle = total_length // 2

        l, r = 0, len(A)
        while l<=r:
            m_A = l + (r-l)//2
            m_B = middle - m_A
            left_A = A[m_A - 1] if m_A > 0 else float('-inf')
            right_A = A[m_A] if m_A < len(A) else float('inf')

            left_B = B[m_B - 1] if m_B > 0 else float('-inf')
            right_B = B[m_B] if m_B < len(B) else float('inf')

            if left_A > right_B:
                r = m_A - 1
            elif left_B > right_A:
                l = m_A + 1
            else:
                if total_length % 2 == 1:
                    return float(min(right_A, right_B))
                else:
                    return (max(left_A, left_B) + min(right_A, right_B)) / 2.0
        


        

        
        
        
        
        
        
        
        
        # m, n = len(nums1), len(nums2)
        # p1, p2, m1, m2 = 0, 0, 0, 0
        
        # for _ in range((m + n) // 2 + 1):
        #     m2 = m1
        #     if p1 < m and (p2 >= n or nums1[p1] < nums2[p2]):
        #         m1 = nums1[p1]
        #         p1 += 1
        #     else:
        #         m1 = nums2[p2]
        #         p2 += 1
                
        # if (m + n) % 2 == 1:
        #     return float(m1)
        # return (m1 + m2) / 2.0
