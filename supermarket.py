class Item:
    _price = 0
    _letter = None

    def __init__(self, letter, price):
        self._price = price
        self._letter = letter

    def get_price(self):
        return self._price


class Checkout:
    _items = []

    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)
        print(self._items)

    def get_total_cost(self):
        cost = 0
        for item in self._items:
            cost += item.get_price()
        return cost

    def get_items(self):
        return self._items
