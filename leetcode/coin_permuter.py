# naive way
# subproblem:
# for a number of single denominations, what are the future denominations that we can break
# this into?
def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in xrange(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]


    return ways_of_doing_n_cents[amount]

print change_possibilities_bottom_up(4, [1,2,3])
