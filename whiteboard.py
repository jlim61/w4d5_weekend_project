'''
Challenge: You have two ropes. Each takes exactly 60 minutes to burn but they do not burn at a consistent rate
(i.e., half the rope might burn in the first 10 minutes and the other half might take 50 minutes). Using only these two ropes and a way to light them, how can you measure out exactly 45 minutes?
Coding/Real-Life Connection: This challenge emphasizes the importance of thinking outside the box.
In coding, it's analogous to using unconventional methods to solve a problem more efficiently. In real life, it mirrors the skill of using available resources creatively to measure or estimate time.
'''

'''
burn both ends of rope 1 and one end of rope 2.
rope 1 burns in 30 min. this leaves rope 2 with 30 min left. 
once rope 1 finishes burning, burn rope 2 on the other end.
that cuts the remaining time in half giving you 15 min.

'''

# Sliding Window Maximum Whiteboard Exercise

# Problem Description:

# You are given an array of integers nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Your task is to return an array that contains the maximum number for each window as it moves from left to right across nums.

# Inputs:
# An array of integers, nums.
# An integer k representing the size of the sliding window.

# Outputs:
# An array of integers representing the maximum element in each of the sliding windows.

# Example:

# Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# Output: [3, 3, 5, 5, 6, 7]

# Constraints:
# The array nums will have at least k elements.
# Time complexity should ideally be better than O(n*k).

nums = [1, 3, -1, -3, 5, 3, 6, 7, 5, 8, 2]
k = 3

# O(n)
def window_max(nums, k):
    output = [] # O(1)
    left_point, right_point = 0, k # O(1)
    while right_point <= len(nums): # O(n)
        window = nums[left_point:right_point] # O(1)
        # print(window, 'window')
        output.append(max(window)) # O(1)
        # print(output, 'output added')
        left_point += 1 # O(1)
        right_point += 1 # O(1)
    # print(output, 'final output')
    return output # O(1)

window_max(nums, k)
# print(window_max(nums, k))

# Input:

nums2 = [9, 7, 2, 4, 6, 8, 2, 1, 5]
k2 = 4

# Output:

# [9, 7, 6, 8, 8, 8]
window_max(nums2, k2)