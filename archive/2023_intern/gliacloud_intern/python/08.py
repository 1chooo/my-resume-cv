'''
Array Challenge
Have the function ArrayChallenge(strArr) take the array of strings stored in strArr, which will contain pairs of integers in the following format: (i1,i2), where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1. For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the following tree:



which you can see forms a proper binary tree. Your program should, in this case, return the string true because a valid binary tree can be formed. If a proper binary tree cannot be formed with the integer pairs, then return the string false. All of the integers within the tree will be unique, which means there can only be one node in the tree with the given integer value.
Examples
Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
Output: true
Input: ["(1,2)", "(3,2)", "(2,12)", "(5,2)"]
Output: false
'''
def ArrayChallenge(strArr):
    graph = {}
    parents = {}

    # Build the graph and track parent-child relationships
    for pair in strArr:
        child, parent = map(int, pair.strip('()').split(','))
        graph.setdefault(parent, []).append(child)
        parents[child] = parent

    root = None
    for node in parents:
        if node not in graph:
            if root is not None:
                return "false"  # More than one root node found
            root = node

    if root is None:
        return "false"  # No root node found

    # Perform depth-first search (DFS) to check if the graph forms a proper binary tree
    def dfs(node, min_value, max_value):
        if node not in graph:
            return True

        for child in graph[node]:
            if child in graph:
                if not (min_value < child < max_value):
                    return False
                if not dfs(child, min_value, node) or not dfs(child, node, max_value):
                    return False
            else:
                if not (min_value < child < max_value):
                    return False

        return True

    if dfs(root, float('-inf'), float('inf')):
        return "true"
    else:
        return "false"

print(ArrayChallenge(input()))