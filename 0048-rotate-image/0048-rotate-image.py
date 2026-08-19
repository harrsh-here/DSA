class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        result = [[0]*c for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                # print(f"{j},{c - i - 1} : ", result[j][c - i - 1])
                result[j][c-i-1] = matrix[i][j]
                # print(f"{j},{c-i-1} : ",result[j][c-i-1])

        # for i in range(r):
        #     for j in range(c):
                # arr[i][j] = (
                # print(f"{j},{c-i-1} : ",result[j][c-i-1])
        matrix[:] = result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna