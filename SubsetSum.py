def isSubsetSum(arr, w):
    n = len(arr)

    # Initialize a 2D table to store the subset sum information
    t = [[False for _ in range(w + 1)] for _ in range(n + 1)]

    # Base case: If the sum is 0, there is always an empty subset that adds up to 0
    for i in range(n + 1):
        t[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]

    return t[n][w]


arr = [1, 3, 5, 7, 10]
w = 11
if isSubsetSum(arr, w):
    print("There exists a subset that adds up to the required sum.")
else:
    print("No subset exists that adds up to the required sum.")
