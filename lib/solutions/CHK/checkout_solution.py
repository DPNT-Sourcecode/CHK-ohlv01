

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
    if skus is None or not skus:
        return -1

    purchased_items = {}

    print(skus)

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

        print(purchased_item, count)

        special_offer_count = special_offers[purchased_item]['count']
        special_offer_price = special_offers[purchased_item]['price']

        if count < special_offer_count:
            total_price += count * prices[purchased_item]

        special_offers_number = count // special_offer_count
        print(special_offers_number)
        regular_purchased_item_number = count % special_offer_count
        print(regular_purchased_item_number)

        total_price += special_offers_number * special_offer_price + regular_purchased_item_number * prices[purchased_item]
        print()
    return total_price








