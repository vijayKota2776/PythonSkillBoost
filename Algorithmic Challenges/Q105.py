def coin_change_greedy(coins, target_amount):
    coins.sort(reverse=True)
    coin_count = 0
    remaining_amount = target_amount
    for coin in coins:
        if remaining_amount >= coin:
            coin_count += remaining_amount // coin  
            remaining_amount %= coin  
        if remaining_amount == 0:
            break
    if remaining_amount > 0:
        return -1
    
    return coin_count
coins = list(map(int, input("Enter coin denominations (space-separated): ").split()))
target_amount = int(input("Enter the target amount: "))
result = coin_change_greedy(coins, target_amount)
if result != -1:
    print(f"The minimum number of coins required: {result}")
else:
    print("It is not possible to make the target amount with the given denominations.")
