from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            if all(char in allowed for char in word):
                count += 1
        return count


# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print (Solution().countConsistentStrings(allowed, words))