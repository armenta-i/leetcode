def merge(left, right):
    sortedList = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedList.append(left[i])
            i += 1
        else:
            sortedList.append(right[j])
            j += 1
        
    sortedList += left[i:]
    sortedList += right[j:]
    return sortedList




def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)


if __name__ == "__main__":
    unsortedList = [3,10,32,100,4,0]
    print(merge_sort(unsortedList))
