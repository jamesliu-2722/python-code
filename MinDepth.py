

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
i = 0

def minD(root, i):
    if root:
        i + 1
        minD(root.left)
        print(root)
        minD(root.right)


class Solution(object):
    def minDepth(self, root):
        """
        :type height: List[int]
        :rtype: int
        """
        minD(root, i)


    # def maxArea2(A, Len):
    #     area = 0
    #     for i in range(Len):
    #         for j in range(i + 1, Len):
    #             # Calculating the max area
    #             area = max(area, min(A[j], A[i]) * (j - i))
    #     return area

root = [3,9,20,None,None,15,7]
obj = Solution()
print(obj.minDepth(root))
