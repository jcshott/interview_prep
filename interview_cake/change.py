def change(amount, denominations):
    """
    function that computes the number of ways to make amount of money with coins of the available denominations

    Inputs:
    1. an amount of money (integer)
    2. a list of coin denominations (integers)

    Output: number of ways to compute that amount from given denominations
    Example: 4 cents from 1 cent, 2 cent & 3 cent coins

    >>> change(amount=4, denominations=[1,2,3])
    4

    """
    ### BOTTOM UP RECURSION - does extra work
    coin_combos = []

    def add_up(curr_amt, denominations, coins_used):
        # we've used the right number of coins to get to destination, check if we've already seen this combo before and, if not, add to combo output.
        if curr_amt == amount:
            coins_used.sort()
            if coins_used not in coin_combos:
                coin_combos.append(coins_used)
            return
        # if we've gone too far, amount is too much, return
        if curr_amt > amount:
            return
        # else, add each one of denominations
        for d in denominations:
            add_up(curr_amt+d, denominations, coins_used+[d])

    add_up(0, denominations, coins_used=[])
    return len(coin_combos)

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "ALL TESTS PASSED!"
