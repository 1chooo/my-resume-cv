function searchingChallenge(strArr) {
  const matrix = strArr.map(row => row.split('').map(Number)); // Convert the string matrix to a list of lists

  function dfs(row, col, prev, length) {
    if (row < 0 || row >= matrix.length || col < 0 || col >= matrix[0].length) {
      return length; // Base case: out of bounds
    }

    const current = matrix[row][col];
    if (current <= prev) {
      return length; // Base case: current value is not strictly increasing
    }

    let maxLength = length;
    for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
      const newRow = row + dx;
      const newCol = col + dy;
      maxLength = Math.max(maxLength, dfs(newRow, newCol, current, length + 1));
    }

    return maxLength;
  }

  let maxLength = 0;
  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[0].length; col++) {
      maxLength = Math.max(maxLength, dfs(row, col, -Infinity, 0));
    }
  }

  return maxLength;
}

console.log(searchingChallenge(prompt().split(',')));
