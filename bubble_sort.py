def bubbleSort(nums: int):
    numsLen = len(nums)

    for i in range(numsLen):
        swapped = False
        for j in range(0, numsLen-i-1):

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j+1], nums[j]
                
    return nums

if __name__== "__main__":
    unsortedNums = [4,100,30,1,25,7,15,3,5]
    sortedNums = bubbleSort(unsortedNums)
    print(sortedNums)