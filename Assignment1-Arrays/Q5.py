def merge(nums1, m, nums2, n):
    temp = [nums1[i] for i in range(m)] 
    i = 0
    j = 0
    k = 0
    while i < m and j < n:
        if temp[i] <= nums2[j]:
            nums1[k] = temp[i]
            i += 1
            k += 1
        else:
            nums1[k] = nums2[j]
            j += 1
            k += 1
            
    while i < m:
        nums1[k] = temp[i]
        k += 1
        i += 1
    
    while j < n:
        nums1[k] = nums2[j]
        k += 1
        j += 1
    return nums1

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(f"The output array is {merge(nums1=nums1, m=m, nums2=nums2, n=n)}")