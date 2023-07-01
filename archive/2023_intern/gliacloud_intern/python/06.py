'''
Matrix Challenge
Have the function MatrixChallenge(strArr) take the strArr parameter being passed which will be a 2D matrix of 0 and 1's, and determine the area of the largest square submatrix that contains all 1's. A square submatrix is one of equal width and height, and your program should return the area of the largest submatrix that contains only 1's. For example: if strArr is ["10100", "10111", "11111", "10010"] then this looks like the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

For the input above, you can see the bolded 1's create the largest square submatrix of size 2x2, so your program should return the area which is 4. You can assume the input will not be empty.
Examples
Input: ["0111", "1111", "1111", "1111"]
Output: 9
Input: ["0111", "1101", "0111"]
Output: 1
'''

def MatrixChallenge(strArr):
    # Convert the input strings into a 2D matrix of integers
    matrix = [list(map(int, row)) for row in strArr]

    rows = len(matrix)
    cols = len(matrix[0])
    max_size = 0

    # Create a dynamic programming table to store the sizes of square submatrices
    dp = [[0] * cols for _ in range(rows)]

    # Fill the first row and first column of the dp table
    for i in range(rows):
        dp[i][0] = matrix[i][0]
    for j in range(cols):
        dp[0][j] = matrix[0][j]

    # Fill the remaining cells of the dp table
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                if dp[i][j] > max_size:
                    max_size = dp[i][j]

    return max_size ** 2

print(MatrixChallenge(input()))