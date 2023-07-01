function arrayChallenge(strArr: string[]): string {
    const graph: { [key: number]: number[] } = {};
    const parents: { [key: number]: number } = {};
  
    // Build the graph and track parent-child relationships
    for (const pair of strArr) {
      const [child, parent] = pair.slice(1, -1).split(',').map(Number);
      graph[parent] = graph[parent] || [];
      graph[parent].push(child);
      parents[child] = parent;
    }
  
    let root: number | null = null;
    for (const node in parents) {
      if (!(node in graph)) {
        if (root !== null) {
          return "false"; // More than one root node found
        }
        root = parseInt(node, 10);
      }
    }
  
    if (root === null) {
      return "false"; // No root node found
    }
  
    // Perform depth-first search (DFS) to check if the graph forms a proper binary tree
    function dfs(node: number, minValue: number, maxValue: number): boolean {
      if (!(node in graph)) {
        return true;
      }
  
      for (const child of graph[node]) {
        if (child in graph) {
          if (!(minValue < child && child < maxValue)) {
            return false;
          }
          if (!dfs(child, minValue, node) || !dfs(child, node, maxValue)) {
            return false;
          }
        } else {
          if (!(minValue < child && child < maxValue)) {
            return false;
          }
        }
      }
  
      return true;
    }
  
    if (dfs(root, -Infinity, Infinity)) {
      return "true";
    } else {
      return "false";
    }
  }
  
  console.log(arrayChallenge(prompt().split(',')));
  