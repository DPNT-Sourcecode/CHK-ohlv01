

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
    for sku in skus:
        if sku not in items:
            return -1

        pass
