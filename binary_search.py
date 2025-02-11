def binarySearch(nums: list, target: int) -> int:
    if not nums:
        return False
    
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid > target]:
            right = mid - 1
    return -1

if __name__ == "__main__":
    unsortedNums = [4,100,30,1,25,7,15,3,5]
    print("Result of binary search: ",
          binarySearch(unsortedNums.sort(), 30))