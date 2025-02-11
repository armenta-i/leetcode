def mergeAlternatively(word1: str , word2: str) -> str:
    minLen = 0
    newString = ""
    if len(word1) != len(word2):
        minLen = min(len(word1), len(word2))
    else:
        minLen = len(word1)
    print(minLen)
    for i in range(minLen):
        newString += word1[i]
        newString += word2[i]
    
    newString += word1[minLen:]
    newString += word2[minLen:]
    return newString


if __name__ == "__main__":
      word1 = "abcd"
      word2 = "pq"
      print(mergeAlternatively(word1, word2))