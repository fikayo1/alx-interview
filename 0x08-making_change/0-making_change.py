#!/usr/bin/python3
"""
Change Comes from within
"""


def makeChange(coins, total):
    """Returns the fewest number of coins needed to meet total."""
    if total < 1:
        return 0
    tot = 0
    for i in range(len(coins)):
        coin = max(coins)
        count = (total // coin)
        tot += count
        total = total - (coin * count)
        coins.remove(coin)
    return tot
