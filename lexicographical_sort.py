def lex_sort(nums: list) -> list:
    for index in range(1, len(nums) - 1):
        lexList = []
        firstNum = list(str(nums[index - 1]))
        secondNum = list(str(nums[index]))
        
        if(firstNum == secondNum):
            lexList.append(min(len(firstNum), len(secondNum)))
        
        print(lexList)

if __name__ == "__main__":
    unsortedList = [100,10,1,2]
    lex_sort(unsortedList)