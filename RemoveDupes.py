from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            else:
                nums[pos+1] = nums[i+1]
                pos += 1
        # print(nums)
        return pos + 1

head = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(head))
