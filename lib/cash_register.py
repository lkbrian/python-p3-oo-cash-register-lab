class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transaction_history = []

    def add_item(self, item, price, quantity=1):
        self.items.extend([item] * quantity)
        self.total += price * quantity
        self.transaction_history.append((price, quantity))
        print(self.items)

    def apply_discount(self):
        discount = self.total * self.discount / 100
        self.total -= discount
        (
            print(f"After the discount, the total comes to ${int(self.total)}.")
            if self.discount > 0
            else print("There is no discount to apply.")
        )

    def void_last_transaction(self):
        if self.transaction_history:
            last_transaction = self.transaction_history.pop()
            last_price, last_quantity = last_transaction
            self.total -= last_price * last_quantity
            print("Last transaction has has been voided.")
        else:
            print("Nothing to void")