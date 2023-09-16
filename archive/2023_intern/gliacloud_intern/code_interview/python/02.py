'''
String Challenge
Have the function StringChallenge(str) take the str parameter being passed and return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string.
Examples
Input: "never odd or even"
Output: true
Input: "eye"
Output: true
'''


def StringChallenge(str):
    # Remove punctuation and spaces
    clean_str = ''.join(char for char in str if char.isalpha())

    # Reverse the clean string
    reversed_str = clean_str[::-1]

    # Compare the clean string with its reversed version
    if clean_str == reversed_str:
        return "true"
    else:
        return "false"


print(StringChallenge(input()))