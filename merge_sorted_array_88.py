def merge(nums1, m, nums2, n):
    numList = list(reversed(nums1))
    for index in range(n):
        numList[index] = nums2[index]
    
    nums1 = numList
    nums1.sort()
    return nums1


if __name__ == "__main__":
    # nums1 = [1,2,3,0,0,0]
    # m = 3
    # nums2 = [2,5,6]
    # n = 3

    # numList = list(reversed(nums1))
    # for index in range(n):
    #     numList[index] = nums2[index]
    
    # nums1 = numList
    # nums1.sort()
    # print(nums1)
    # # print(merge(nums1, m, nums2, n))

    nums1 = [-1,0,0,3,3,3,0,0,0]
    print(set(nums1))
    # m = 6
    # n = 3
    # nums2 = [1,2,2]
    # print(merge(nums1, m, nums2, n))
    
    # nums1 = [0]
    # m = 1
    # n = 1
    # nums2 = [1]
    # print(merge(nums1, m, nums2, n))
