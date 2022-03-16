

# noinspection PyUnusedLocal
# skus = unicode string

# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+


special_offers = {
    'A': {
        'count': 3,
        'price': 130
    },
    'B': {
        'count': 2,
        'price': 45
    }
}

prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

items = prices.keys()


def checkout(skus):
    purchased_items = {}

    for sku in skus:
        if sku not in items:
            return -1

        if sku not in purchased_items:
            purchased_items[sku] = 0

        purchased_items[sku] += 1

    print(purchased_items)

    total_price = 0

    for purchased_item, count in purchased_items.items():
        if purchased_item not in special_offers:
            total_price += prices[purchased_item]
            continue

        


        # if count <







