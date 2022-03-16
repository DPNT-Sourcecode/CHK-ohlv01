

# noinspection PyUnusedLocal
# skus = unicode string

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+

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
    if not skus:
        return 0

    if skus is None:
        return -1

    purchased_items = {}

    for sku in skus:
        if sku not in items:
            return -1

        if sku not in purchased_items:
            purchased_items[sku] = 0

        purchased_items[sku] += 1

    total_price = 0

    for purchased_item, count in purchased_items.items():
        if purchased_item not in special_offers:
            total_price += count * prices[purchased_item]
            continue

        special_offer_count = special_offers[purchased_item]['count']
        special_offer_price = special_offers[purchased_item]['price']

        special_offers_number = count // special_offer_count
        regular_purchased_item_number = count % special_offer_count

        total_price += special_offers_number * special_offer_price + regular_purchased_item_number * prices[purchased_item]

    return total_price




