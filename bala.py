class Shop:
    def __init__(self, items):
        self.items = items

    def calculate_bill(self, item_choices):
        total_bill = sum(
            self.items.get(item_name, 0) * quantity
            for item_name, quantity in item_choices.items()
        )
        return total_bill


def shop_interaction():
    items = {
        "Iphone": 1000,
        "Samsun": 300,
        "Airpods pro": 300,
        "Wireless earphones": 100,
        "Ipad": 600
    }
    shop = Shop(items)

    print("Welcome to the Shop!")
    print("Available items:")
    for item_name, item_price in shop.items.items():
        print(f"- {item_name}: ${item_price}")

    item_choices = {}
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name == "done":
            break

        quantity = int(input("Enter quantity: "))
        item_choices[item_name] = item_choices.get(item_name, 0) + quantity

    total_bill = shop.calculate_bill(item_choices)
    print(f"Total bill amount: ${total_bill}")


shop_interaction()
