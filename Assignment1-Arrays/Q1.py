
#  **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# **Example:**
# Input: nums = [2,7,11,15], target = 9
# Output0 [0,1]

# **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1]

def twoSum(nums, target):
    hashMap = dict()
    out = [-1, -1]
    for i in range(len(nums)):
        hashMap[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in hashMap and i != hashMap[target - nums[i]]:
            out = [i, hashMap[target - nums[i]]]
    return out

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(f"The output is {twoSum(nums, target)}")
