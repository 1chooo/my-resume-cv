def reverseString(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s

# Example 1
s1 = ["h", "e", "l", "l", "o"]
reverseString(s1)
print(s1)  # Output: ["o", "l", "l", "e", "h"]

# Example 2
s2 = ["H", "a", "n", "n", "a", "h"]
reverseString(s2)
print(s2)  # Output: ["h", "a", "n", "n", "a", "H"]


def reverse(a):
    n = len(a)
    b = [None] * n  # 創建與 a 一樣大小的新陣列 b

    for i in range(n):
        b[n - 1 - i] = a[i]  # 將 a 中元素反轉存入 b

    return b

# 測試
arr1 = ["h", "e", "l", "l", "o"]
reversed_arr1 = reverse(arr1)
print(reversed_arr1)  # Output: ['o', 'l', 'l', 'e', 'h']

arr2 = ["H", "a", "n", "n", "a", "h"]
reversed_arr2 = reverse(arr2)
print(reversed_arr2)  # Output: ['h', 'a', 'n', 'n', 'a', 'H']


def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

# Example 1
nums1 = [1, 3, 5, 6]
target1 = 5
print(searchInsert(nums1, target1))  # Output: 2

# Example 2
nums2 = [1, 3, 5, 6]
target2 = 2
print(searchInsert(nums2, target2))  # Output: 1

# Example 3
nums3 = [1, 3, 5, 6]
target3 = 7
print(searchInsert(nums3, target3))  # Output: 4
