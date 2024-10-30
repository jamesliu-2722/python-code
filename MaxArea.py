

class Solution(object):
    def maxArea(self, height):
        max = 0
        if len(height) == 2:
            if height[0] > height[1]:
                return height[1] * height[1]
            else:
                return height[0] * height[0]
        for i in range(len(height)):
            prev = i + 1
            for j in range(i+1, len(height)):
                if prev < j:
                    if height[i] < height[j]:
                        area = height[i] * (j - i)
                        if area > max:
                            max = area
                    else:
                        area = height[j] * (j - i)
                        if area > max:
                            max = area
                prev = j

        return max

height = [2,3,4,5,18,17,6]
obj = Solution()
print(obj.maxArea(height))