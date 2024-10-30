from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 1:
            return matrix
        # elif len(matrix) == 2:
        #     return [[matrix[1][0], matrix[0][0]],[matrix[1][1], matrix[0][1]]]
        else:
            for i in range(int(len(matrix) / 2)):  # i is the frame count
                for j in range(len(matrix) - 1 - (i * 2)): # j is the iteration count on each of the four sides of the frame
                    temp = matrix[i + j][len(matrix) - 1 - i]
                    matrix[i + j][len(matrix) - 1 - i] = matrix[i][i + j]
                    temp2 = matrix[len(matrix) - 1 - i][len(matrix) - 1 - i - j]
                    matrix[len(matrix) - 1 - i][len(matrix) - 1 - i - j] = temp
                    temp3 = matrix[len(matrix) - 1 - i - j][i]
                    matrix[len(matrix) - 1 - i - j][i] = temp2
                    matrix[i][i + j] = temp3
        return matrix

# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print (Solution().rotate(matrix))