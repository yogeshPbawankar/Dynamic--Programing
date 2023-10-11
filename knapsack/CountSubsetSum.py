def countOfSubsetSum(arr, w):
    n = len(arr)

    # Initialize a 2D table to store the subset sum information
    t = [[False for _ in range(w + 1)] for _ in range(n + 1)]

    # Base case: If the sum is 0, there is always an empty subset that adds up to 0
    for i in range(n + 1):
        t[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j] # change is or turn in +
            else:
                t[i][j] = t[i - 1][j]

    return t[n][w]

arr = [2,3,5,6,8,10]
sum = 10
count = countOfSubsetSum(arr,sum)
if count > 0:
    print("Count : ",count)
else:
    print("Some doesn't exits")
