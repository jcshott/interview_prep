cache = {}
def staircase(n):
    if n in cache:
        return cache[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    cache[n] = staircase(n-3) + staircase(n-2) + staircase(n-1)
    # return staircase(n-3) + staircase(n-2) + staircase(n-1)

    return cache[n]

print staircase(100)
