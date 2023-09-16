function matrixChallenge(strArr: string[]): number {
    // Convert the input strings into a 2D matrix of integers
    const matrix: number[][] = strArr.map(row => row.split('').map(Number));
  
    const rows = matrix.length;
    const cols = matrix[0].length;
    let maxSize = 0;
  
    // Create a dynamic programming table to store the sizes of square submatrices
    const dp: number[][] = Array.from({ length: rows }, () => Array(cols).fill(0));
  
    // Fill the first row and first column of the dp table
    for (let i = 0; i < rows; i++) {
      dp[i][0] = matrix[i][0];
    }
    for (let j = 0; j < cols; j++) {
      dp[0][j] = matrix[0][j];
    }
  
    // Fill the remaining cells of the dp table
    for (let i = 1; i < rows; i++) {
      for (let j = 1; j < cols; j++) {
        if (matrix[i][j] === 1) {
          dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1;
          if (dp[i][j] > maxSize) {
            maxSize = dp[i][j];
          }
        }
      }
    }
  
    return Math.pow(maxSize, 2);
  }
  
  console.log(matrixChallenge(prompt().split(',')));
  