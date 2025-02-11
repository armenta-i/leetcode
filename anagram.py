from collections import Counter

def isAnagram(stringOne, stringTwo):
    dictOne = Counter(stringOne)
    dictTwo = Counter(stringTwo)

    for char in max(dictOne, dictTwo):
        if dictOne[char] != dictTwo[char]:
            return False
    return True

if __name__ == "__main__":    
    # print(isAnagram('cats', 'tocs')) # False
    # print(isAnagram('paper', 'reapa')) # False
    # print(isAnagram('monkeyswrite', 'newyorktimes')) # True
    # print(isAnagram('restful', 'fluster')) # True
    # print(isAnagram('tax', 'taxi')) # False
    stringOne = "tax"
    stringTwo = "taxi"
    dictOne = Counter(stringOne)
    dictTwo = Counter(stringTwo)

    print(max(dictOne, dictTwo))
    
    