#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total
    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met
    Return:
        Number of coins or -1 if meeting the total is not possible
    """
    if total <= 0:
        return 0

    # Initialize dp array to hold the minimum number of coins for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make 0 amount

    # Iterate over each coin and update the dp array
    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] is still infinity
    return dp[total] if dp[total] != float('inf') else -1
