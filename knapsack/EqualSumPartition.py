def isSubsetSumExist(arr, n):
    # finding the sum
    _sum = 0
    for i in range(n):
        _sum = _sum + arr[i]
    # check if the sum exists and is even
    if _sum % 2 == 0:
        return isSubsetSum(arr, n, _sum // 2)  # Pass _sum // 2 to isSubsetSum
    else:
        return False

def isSubsetSum(arr, n, target):
    # initialize 2D array with False
    t = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    # initialize the first row
    for i in range(n + 1):
        t[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[n][target]  # Check if t[n][target] is True


arr = [1, 5, 11, 5]
print(isSubsetSumExist(arr, len(arr)))
