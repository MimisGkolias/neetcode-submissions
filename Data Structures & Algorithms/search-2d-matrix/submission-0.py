class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            middle = l + (r-l)//2
            if target >= matrix[middle][0] and target <= matrix[middle][len(matrix[middle])-1]:
                p, q = 0, len(matrix[middle]) - 1
                while p <= q:
                    nested_middle = p + (q-p)//2
                    if target == matrix[middle][nested_middle]:
                        return True
                    elif target < matrix[middle][nested_middle]:
                        q = nested_middle - 1
                    elif target > matrix[middle][nested_middle]:
                        p = nested_middle + 1
                return False
            elif target < matrix[middle][0]:
                r = middle - 1
            elif target > matrix[middle][len(matrix[middle]) - 1]:
                l = middle + 1
        
        return False