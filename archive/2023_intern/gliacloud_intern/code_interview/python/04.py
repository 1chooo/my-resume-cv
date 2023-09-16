'''
Searching Challenge
Have the function SearchingChallenge(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.
Examples
Input: "(coder)(byte))"
Output: 0
Input: "(c(oder)) b(yte)"
Output: 1
'''

def SearchingChallengeCount(str):
    count = 0

    for char in str:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return 0

    if count != 0:
        return 0
    else:
        return 1


def SearchingChallenge(str):
    stack = []

    for char in str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return 0
            else:
                stack.pop()

    if len(stack) == 0:
        return 1
    else:
        return 0

print(SearchingChallenge(input()))