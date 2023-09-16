'''
Searching Challenge
Have the function SearchingChallenge(strArr) take the array of strings stored in strArr, which will be an NxM matrix of positive single-digit integers, and find the longest increasing path composed of distinct integers. When moving through the matrix, you can only go up, down, left, and right. For example: if strArr is ["345", "326", "221"], then this looks like the following matrix:

3 4 5
3 2 6
2 2 1

For the input above, the longest increasing path goes from: 3 -> 4 -> 5 -> 6. Your program should return the number of connections in the longest path, so therefore for this input your program should return 3. There may not necessarily always be a longest path within the matrix.
Examples
Input: ["12256", "56219", "43215"]
Output: 5
Input: ["67", "21", "45"]
Output: 3
'''

def SearchingChallenge(strArr):
    matrix = [list(map(int, row)) for row in strArr]  # Convert the string matrix to a list of lists

    def dfs(row, col, prev, length):
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return length  # Base case: out of bounds

        current = matrix[row][col]
        if current <= prev:
            return length  # Base case: current value is not strictly increasing

        max_length = length
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row = row + dx
            new_col = col + dy
            max_length = max(max_length, dfs(new_row, new_col, current, length + 1))

        return max_length

    max_length = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            max_length = max(max_length, dfs(row, col, float('-inf'), 0))

    return max_length

print(SearchingChallenge(input()))