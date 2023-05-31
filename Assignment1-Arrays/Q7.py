def moveZeroes(nums):
    i, j = 0, 0
    while i < len(nums):
        if nums[i]!=0:
            k = nums[j]
            nums[j] = nums[i]
            nums[i] = k
            j += 1
        i += 1
if "__main__" == __name__:
    nums = [2,1,0,4,0,0,3,2]
    moveZeroes(nums)
    print(nums)

