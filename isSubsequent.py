from collections import Counter

def isSubsequence(s: str, t: str) -> bool:
    charComp = ""
    sDict = Counter(s)
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    for char in t:
        if char in sDict and sDict[char] == 1:
            sDict[char] = sDict[char] - 1
            charComp = charComp + char
    print(sDict.values())
    print(''.join(sDict.keys()))
    print(charComp)
    if  charComp == (s):
        return True
    else:
        return False

if __name__ == "__main__":
    print(isSubsequence("abc", "ahbgdc")) # True 
    print(isSubsequence("axc", "ahbgdc")) # False
    print(isSubsequence("ab", "baab")) # False
        