# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

def findErrorNums(nums):
    hashMap = dict()
    for num in nums:
        if num in hashMap:
            hashMap[num] += 1
            dup = num
        else:
            hashMap[num] = 1

    n = len(nums)
    mis = int((n*(n+1))/2) + dup - sum(nums) 

    return [dup, mis]

if __name__ == "__main__":
    nums = [1,1,2]
    print(f"The output is : {findErrorNums(nums)}")