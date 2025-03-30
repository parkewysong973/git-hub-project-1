import random

def find_max_sum_subarray(nums):
    n = len(nums)
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for i in range(1, n):
        if nums[i] > current_sum + nums[i]:
            current_sum += nums[i]
        else:
            current_sum = nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum

# Example usage
nums = [3, -2, 5, -1]
print(find_max_sum_subarray(nums)) # Output: 6
