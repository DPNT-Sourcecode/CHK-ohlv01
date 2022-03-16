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

special_offers_discount = {
    'A': [
        {
            'count': 3,
            'price': 130,
        },
        {
            'count': 5,
            'price': 200,
        }
    ],
    'B': [
        {
            'count': 2,
            'price': 45,
        }
    ]
}

special_offers_free = {
    'E': [
        {
            'count': 2,
            'target': 'B',
            'target_count': 1,
        },
    ]
}

prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}

items = prices.keys()

def get_special_offers_discount_counts(discount_counts, total_count):
    result = []
    loop = 1

    for x in discount_counts:
        for y in discount_counts:
            if x + y == total_count:
                result.append((x, y))

        discount_counts = discount_counts[loop:]
        loop += 1

    return result


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

    print(purchased_items)

    for purchased_item, count in purchased_items.items():
        if purchased_item not in special_offers_discount and purchased_item not in special_offers_free:
            total_price += count * prices[purchased_item]
            continue

        if purchased_item in special_offers_free:
            is_exact_special_offer_free = False
            final_exact_special_offer_free_target = None
            final_exact_special_offer_free_target_count = 0

            for exact_special_offer_free in special_offers_free[purchased_item]:
                exact_special_offer_free_count = exact_special_offer_free['count']
                exact_special_offer_free_target = exact_special_offer_free['target']
                exact_special_offer_free_target_count = exact_special_offer_free['target_count']

                if count >= exact_special_offer_free_count:
                    if exact_special_offer_free_target in purchased_items:
                        if purchased_items[exact_special_offer_free_target] >= exact_special_offer_free_target_count:
                            is_exact_special_offer_free = True
                            final_exact_special_offer_free_target = exact_special_offer_free_target
                            final_exact_special_offer_free_target_count = exact_special_offer_free_target_count

            total_price += count * prices[purchased_item]

            if is_exact_special_offer_free:
                purchased_items[final_exact_special_offer_free_target] -= final_exact_special_offer_free_target_count
                continue

        if purchased_item in special_offers_discount:
            is_exact_special_offer_discount = False
            final_exact_special_offer_discount_count = 0
            final_exact_special_offer_discount_price = 0

            discount_counts = [discount.get('count') for discount in special_offers_discount[purchased_item]]
            target_discounts = get_special_offers_discount_counts(discount_counts=discount_counts, total_count=count)

            for exact_special_offer_discount in special_offers_discount[purchased_item]:
                exact_special_offer_discount_count = exact_special_offer_discount['count']
                exact_special_offer_price = exact_special_offer_discount['price']

                if exact_special_offer_discount_count in target_discounts:
                    if count >= exact_special_offer_discount_count:
                        is_exact_special_offer_discount = True
                        final_exact_special_offer_discount_count = exact_special_offer_discount_count
                        final_exact_special_offer_discount_price = exact_special_offer_price

                    if is_exact_special_offer_discount:
                        special_offer_discount_count = final_exact_special_offer_discount_count
                        special_offer_discount_price = final_exact_special_offer_discount_price

                        special_offers_number = count // special_offer_discount_count
                        regular_purchased_item_number = count % special_offer_discount_count

                        total_price += special_offers_number * special_offer_discount_price + regular_purchased_item_number * prices[purchased_item]

            # else:
            #     total_price += count * prices[purchased_item]

    return total_price
