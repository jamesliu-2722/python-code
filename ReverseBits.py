import math

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            if n % 2 == 1:
                # print (1)
                result = math.pow(2, 31 - i) + result
            # else:
            #     print (0)
            n = int(n / 2)

        return int(result)



n = 0b11111111111111111111111111111101
# n = 0b00000000000000000000000000000101
print (Solution().reverseBits(n))