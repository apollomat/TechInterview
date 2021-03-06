  def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1
    # we only want to look at each coin once.. If we put it in the for loop (inner),
    # we could be looking more than once
    # 
    for coin in denominations:

        for higher_amount in xrange(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += (
                ways_of_doing_n_cents[higher_amount_remainder]
            )

    return ways_of_doing_n_cents[amount]
