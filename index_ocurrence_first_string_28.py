def strStr(haystack, needle):
    haystackLen = len(haystack)
    subIndex = 0
    equal = False
    needleIndex = 0
    firstIndexFound = 0
    for i in range(haystackLen):
        if haystack[i] == needle[0]:
            subIndex = i
            firstIndexFound = subIndex
            break

    while equal:
        if needleIndex >= len(needle):
            return firstIndexFound
        if (haystack[subIndex] != needle[needleIndex]):
            equal = False
        else:
            print("Haystack[subindex]: ", haystack[subIndex])
            print("needle[needleIndex]: ", needle[needleIndex])
            subIndex += 1
            needleIndex += 1


if __name__ == "__main__":
    print(strStr("sadbutsad", "sad"))