def partitionString(s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        partitionString = []
        substring = ""

        for i in s:
            if i not in substring:
                substring += i
            else:
                partitionString.append(substring)
                substring = ""
                substring += i
        partitionString.append(substring)
        return len(partitionString)
            

if __name__ == "__main__":
    stringOne = "abacaba"
    print(partitionString(stringOne))