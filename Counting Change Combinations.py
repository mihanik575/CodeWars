def count_change(money, coins):
    if money == 0:
        return 1
    if money < 0:
        return 0
    else:
        sum = 0
        for i in range(len(coins)):
            sum += count_change(money - coins[i], coins)
        return sum

print(count_change(4, [1, 2]))
