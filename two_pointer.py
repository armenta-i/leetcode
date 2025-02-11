def two_pointer(arr, target):
    arr = sorted(arr)
    print(arr)
    left = arr[0]
    right = arr[len(arr) - 1]

    while (left < right):
        sum = left + right
        if sum == target:
            return sum
        elif (sum < target):
            left += 1
        else:
            right += 1
    return False

if __name__ == "__main__":
    unsortedList = [20,1,100,3,10,98]
    print(two_pointer(unsortedList, 108))