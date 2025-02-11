from collections import Counter

def frequentEvenNum(nums):
    numsDict = Counter(filter(lambda num: num % 2 == 0, nums))
    if not numsDict:
        return -1
    print(numsDict)

    bigFreq = max(numsDict.values())
    freqNumList = []
    for num in numsDict:
        if numsDict[num] == bigFreq:
            freqNumList.append(num)
    return min(freqNumList)

if __name__ == "__main__":
    nums = [29,47,21,41,13,37,25,7]
    print(frequentEvenNum(nums))