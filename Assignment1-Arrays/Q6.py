def containsDuplicate(nums):
    uniqueElements = list(set(nums))
    return len(uniqueElements) != len(nums)

if "__main__" == __name__:
    nums = [1,2,2,3,4,5,5,6,6,6,6,6]
    print(f"The output is {containsDuplicate(nums)}")
    nums = [1,2,3,4,5,6,7]
    print(f"The output is {containsDuplicate(nums)}")
