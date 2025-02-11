def find_bound(nums: list) -> int:
    numLens = len(nums)
    left = 0
    right = numLens - 1
    boundIndex = -1

    while left <= right: 
        mid = (left + right) // 2

        if arr[mid]:
            boundIndex = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundIndex
    

if __name__ == "__main__":
    arr = [False, False, True, True, True]
    print(find_bound(arr))