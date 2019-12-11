# https://github.com/TDD-Katas/supermarket-checkout

# In a normal supermarket, things are identified using Stock Keeping Units, or SKUs.
# In our store, we’ll use individual letters of the alphabet (A, B, C, and so on).
# Our goods are priced individually.
# In addition, some items are multipriced: buy n of them, and they’ll cost you y pounds.
# For example, item ‘A’ might cost 50 pounds individually,
# but this week we have a special offer: buy three ‘A’s and they’ll cost you 130.
#
# The price table:
# ITEM 	PRICE
# A 	50
# B 	30
# C 	20
# D 	15
#
# The offer table:
# ITEM 	OFFER
# A 	3 for 130
# B 	2 for 45
#
# Our checkout accepts items in any order,
# so that if we scan a B, an A, and another B, we’ll recognize the two B’s and price them at 45 (for a total price so far of 95).
from supermarket import Item, Checkout

item_a = Item('A', 50)
item_b = Item('B', 30)
item_c = Item('C', 20)
item_d = Item('D', 15)


def test_simple_add_items():
    checkout = Checkout()
    checkout.add_item(item_a)
    checkout.add_item(item_b)
    assert len(checkout.get_items()) == 2


def test_simple_price():
    checkout = Checkout()
    checkout.add_item(item_a)
    assert checkout.get_total_cost() == 50


def test_simple_price_two_items():
    checkout = Checkout()
    checkout.add_item(item_a)
    checkout.add_item(item_b)
    assert checkout.get_total_cost() == 80
