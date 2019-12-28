"""
The naive recursive way to solve this is the following.

We track a current amount, current coin, target amount, and list of coins.

At each recursive step, we try three things:
    1. take the current coin type and keep current coin the same;
    2. take the current coin and move on to the next coin type;
    3. skip the current coin type.

Our base cases are:
    1. current amount equals target amount so we return 1; and
    2. current amount is greater than the target amount so we return 0.

Now, we note that there's overlap in the problems we solve since all that matters at any
given point is the current coin and the difference between the current amount and the
target amount.

So, we can use dynamic programming to solve this by counting the number of ways to get
all amounts between 0 and n for each coin. The subtlety here is that since we want all
combinations rather than all permutations, we need to make sure that each way represents
one set of coin choices rather than one order. We can accomplish this by iterating over
the coins in the outer loop (from smallest to largets) and the range 0 to amount in the
inner loop.
"""
from typing import List


def change_recursive(curr_amount: int, curr_coin: int, target_amount: int, coins: List[int]):
    if curr_coin >= len(coins):
        return 0

    if curr_amount == target_amount:
        return 1
    elif curr_amount > target_amount:
        return 0

    count_with_curr_coin = change_recursive(curr_amount + coins[curr_coin], curr_coin, target_amount, coins)
    count_wo_curr_coin = change_recursive(curr_amount, curr_coin+1, target_amount, coins)
    return count_with_curr_coin + count_wo_curr_coin


def change_dp(amount: int, coins: List[int]):
    curr_amount = min(coins)
    num_ways = [0] * (amount+1)
    num_ways[0] = 1
    for coin in coins:
        for i in range(coin, amount+1):
           num_ways[i] += num_ways[i-coin] 
    return num_ways[amount]


def change(amount: int, coins: List[int]):
    return change_dp(amount, coins)
