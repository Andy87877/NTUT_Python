def binarySearch(data, left, right, key):
    mid = (left + right) // 2
    if data[mid] == key:
        return mid
    if left == right:
        return -1
    if data[mid] > key:
        right = mid - 1
    else:
        left = mid + 1
    return binarySearch(data, left, right, key)


data = [1, 2, 5, 7, 9, 14, 23, 26]
print(binarySearch(data, 0, 7, 9))
data = [11, 23, 49, 57, 66, 78, 84, 91]
print(binarySearch(data, 0, 7, 84))
