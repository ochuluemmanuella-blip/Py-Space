class Cart:
    def __init__(self):
        self.items = {}

    def add(self, name, qty=1):
        self.items[name] = self.items.get(name, 0) + qty

    def total_items(self):
        return sum(self.items.values()) 

    def remove(self, name):
        self.items.pop(name, None)

cart = Cart()    
cart.add("apple")
cart.add("apple")
cart.add("pear")

cart.remove("apple")
print(cart.items)          # {'pear': 1}
print(cart.total_items())  # 1

cart.remove("banana")      # not in the cart, so no error
print(cart.items)          # {'pear': 1}


print(cart.items)
print(cart.total_items())