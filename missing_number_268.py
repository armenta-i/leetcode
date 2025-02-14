# Solved by using two pointer algorithm, and sets.
# Convert list to set to have better access time

# Use two pointer to test all number in range

def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Convert nums into a set to have O(1) access time
        numSet = set(nums)

        leftPointer = 0
        rightPointer = len(nums)

        while True:
            numToFind = rightPointer - leftPointer
            if  numToFind in numSet:
                leftPointer += 1
            else:
                return numToFind
    
if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]

    print(missingNumber(nums))