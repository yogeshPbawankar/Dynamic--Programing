def minSubsetSumDiff(arr, w):
    # sub set sum problem code
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

# begin the change in code

    # Find the minimum subset sum difference
    mn = float("inf")
    for j in range(w // 2, -1, -1): # the our ans will lie in half of the arr
        if t[n][j]:
            mn = min(mn, w - 2 * j)

    return mn

arr = [1, 11, 6, 5]
total_sum = sum(arr)
print("Min Subset Sum Difference: ", minSubsetSumDiff(arr, total_sum))
