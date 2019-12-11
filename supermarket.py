from collections import Counter


# pytest --show-capture stdout
class Checkout:
    _items = []
    _offers = []

    def __init__(self):
        self._items = []
        self._offers = []
        self._offers.append(Offer(Item('A', 50), 130, 3))
        self._offers.append(Offer(Item('B', 30), 45, 2))

    def add_item(self, item):
        self._items.append(item)

    def get_total_cost(self):
        cost = 0
        items = self.get_items()
        if self._has_offers():
            for offer in self._offers:
                if offer.get_item() in items and items.count(offer.get_item()) == offer.get_quantity():
                    cost += offer.get_price()
                    for i in range(offer.get_quantity()):
                        items.remove(offer.get_item())
        for item in items:
            cost += item.get_price()
        return cost

    def get_items(self):
        return self._items

    def _has_offers(self):
        if self._offers:
            return True
        return False


class Item:
    _price = 0
    _letter = None

    def __init__(self, letter, price):
        self._price = price
        self._letter = letter

    def get_price(self):
        return self._price

    def __str__(self):
        return self._letter + ':' + str(self._price)

    def __eq__(self, other):
        return str(self) == str(other)


class Offer:
    _item = None
    _price = None
    _required_quantity = None

    def __init__(self, item, price, quantity):
        self._item = item
        self._price = price
        self._required_quantity = quantity

    def get_price(self):
        return self._price

    def get_item(self):
        return self._item

    def get_quantity(self):
        return self._required_quantity
