def sortColors(nums):
    numsLen = len(nums)

    for i in range(numsLen):
        for j in range(i + 1, numsLen):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    sortedNum = sortColors(nums)
    print(sortedNum)