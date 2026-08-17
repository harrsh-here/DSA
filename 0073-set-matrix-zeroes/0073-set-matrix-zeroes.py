class Solution(object):
    def setZeroes(self, matrix):
       
        r = len(matrix)
        c = len(matrix[0])
        row_track = [0]*r
        col_track = [0]*c

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row_track[i]=-1
                    col_track[j] = -1
        for i in range(r):
            for j in range(c):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna