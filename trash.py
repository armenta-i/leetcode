def solution(A, B):
    def count_pieces(length, stick1, stick2):
        return (stick1 // length) + (stick2 // length)

    def can_form_square(length, stick1, stick2):
        return count_pieces(length, stick1, stick2) >= 4

    for length in range(min(A, B), 0, -1):
        if can_form_square(length, A, B):
            return length
    return 0

def spinWord(sentence):
    sentenceList = sentence.split()
    print(sentenceList)
    newString = ""
    reversedWord = ""
    for word in sentenceList:
        print("Word: ", word)
        if len(word) >= 5:
            reversedWord = word[::-1]
            newString += reversedWord + " "
        else:
            newString += word + " "
    return newString.strip()

if __name__ == "__main__":
    # print(solution(29,10))
    # word = "Welcome"
    # newWord = spinWord("Hey fellow warriors")
    # print(newWord)
    s = "Hello world"
    print(len(s.split().pop()))



