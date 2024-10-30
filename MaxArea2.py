# def maxArea2(height, param):
#     pass

def maxArea2(A, Len):
    area = 0
    for i in range(Len):
        for j in range(i + 1, Len):
            # Calculating the max area
            area = max(area, min(A[j], A[i]) * (j - i))
    return area

class Solution(object):
    def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea2(height, len(height))

    # def maxArea2(A, Len):
    #     area = 0
    #     for i in range(Len):
    #         for j in range(i + 1, Len):
    #             # Calculating the max area
    #             area = max(area, min(A[j], A[i]) * (j - i))
    #     return area

height = [2,3,4,5,18,17,6]
obj = Solution()
print(obj.maxArea(height))
