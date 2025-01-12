def coin_change_dp(coins, target_amount):
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0  
    for coin in coins:
        for amount in range(coin, target_amount + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    return dp[target_amount] if dp[target_amount] != float('inf') else -1
coins = list(map(int, input("Enter coin denominations (space-separated): ").split()))
target_amount = int(input("Enter the target amount: "))
result = coin_change_dp(coins, target_amount)
if result != -1:
    print(f"The minimum number of coins required: {result}")
else:
    print("It is not possible to make the target amount with the given denominations.")
