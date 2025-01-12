def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]
values = list(map(int, input("Enter values of the items (space-separated): ").split()))
weights = list(map(int, input("Enter weights of the items (space-separated): ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))
result = knapsack_01(values, weights, capacity)
print(f"The maximum value that can be obtained is: {result}")
