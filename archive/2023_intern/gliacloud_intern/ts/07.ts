function searchingChallenge(strArr: string[]): number {
    const matrix: number[][] = strArr.map(row => row.split('').map(Number)); // Convert the string matrix to a list of lists
  
    function dfs(row: number, col: number, prev: number, length: number): number {
      if (row < 0 || row >= matrix.length || col < 0 || col >= matrix[0].length) {
        return length; // Base case: out of bounds
      }
  
      const current: number = matrix[row][col];
      if (current <= prev) {
        return length; // Base case: current value is not strictly increasing
      }
  
      let maxLength: number = length;
      for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
        const newRow: number = row + dx;
        const newCol: number = col + dy;
        maxLength = Math.max(maxLength, dfs(newRow, newCol, current, length + 1));
      }
  
      return maxLength;
    }
  
    let maxLength: number = 0;
    for (let row = 0; row < matrix.length; row++) {
      for (let col = 0; col < matrix[0].length; col++) {
        maxLength = Math.max(maxLength, dfs(row, col, -Infinity, 0));
      }
    }
  
    return maxLength;
  }
  
  console.log(searchingChallenge(prompt().split(',')));
  