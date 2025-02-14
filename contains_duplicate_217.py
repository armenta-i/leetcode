from collections import Counter

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    # Convert nums into a set, if they are not the same length,
    # it means that nums contains duplicates
    
    numSet = set(nums)

    if(len(numSet) != len(nums)):
        return True
    return False


if __name__ == "__main__":
    nums = [1,2,3,4]
    print(containsDuplicate(nums))

