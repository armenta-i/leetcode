def twoSum(nums, target):
    numsDict = {}

    for index in range(len(nums)):
        secondNum = target - nums[index]

        if secondNum in numsDict:
            return [numsDict[secondNum], index]
        numsDict[nums[index]] = index

if __name__ == "__main__":
    numList = [2,7,11,15]
    target = 9
    print(twoSum(numList, target))