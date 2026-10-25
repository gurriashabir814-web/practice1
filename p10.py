class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = {"qty": qty, "price": price}

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named {name}")
        del self.items[name]

    def total_value(self):
        return sum(details["qty"] * details["price"] for details in self.items.values())

    def __len__(self):
        return len(self.items)
inv = Inventory()
stock_data = [
    "pen, 10, 25",
    "notebook, 5, 120",
    "bag, abc, 1500",   
    "marker, 4, 80"
]

for line in stock_data:
    parts = line.split(",")
    if len(parts) != 3:
        continue
    name = parts[0].strip()
    try:
        qty = int(parts[1].strip())
        price = float(parts[2].strip())
        inv.add_item(name, qty, price)
    except ValueError:
        print(f"Skipping {name}: bad number")
print(f"{len(inv)} items, total value {inv.total_value()}")
inv.remove_item("pen")
print(f"{len(inv)} items, total value {inv.total_value()}")
try:
    inv.remove_item("laptop")
except KeyError as e:
    print(f"Error: {e}")