
'''
old_price = 100
new_price = 110

return_rate = (new_price - old_price) / old_price

print(return_rate)
'''


prices = [100, 105, 103, 108, 112]

for i in range(1, len(prices)):

    old_price = prices[i-1]
    new_price = prices[i]

    print((new_price - old_price)/ old_price)
