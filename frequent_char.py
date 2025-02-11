from collections import Counter

def most_frequent_char(s):
    sDict = Counter(s)
    # print(sDict)
    maxChar = 0
    for char in sDict:
        if sDict[char] > sDict[maxChar]:
            maxChar = char
    return maxChar

if __name__ == "__main__":
    print(most_frequent_char('bookeeper'))
    nums = [1,2,3]
    print(nums)