# Binary Search
def binarySearch(arr, target):
    l=0
    r=len(arr)-1

    while l <= r:
        mid = l + (r - l) // 2
        # Check if x is present at mid
        if arr[mid] == target:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < target:
            l = mid + 1
        # If x is smaller, ignore right half
        else:
            r = mid - 1
    # If we reach here, then the element
    # was not present
    return -1

if __name__ == "__main__":
    arr = [1,3,5,6,8]
    target = 3
    print(f"The output is {binarySearch(arr, target)}")