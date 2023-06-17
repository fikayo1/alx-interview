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
        if total < min(coins):
            return -1
        coins.remove(coin)
    return tot
    
print(makeChange([1256, 54, 48, 16, 102], 1453))