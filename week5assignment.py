from abc import ABC, abstractmethod

class Billable(ABC):
    @abstractmethod
    def tip_amount(self):
        pass

class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass

class Order(Billable, Displayable):
    def __init__(self, dish, price):
        if price < 0:
            raise ValueError(f"Invalid price: {price}")
        self.dish = dish
        self.price = price
    
    def tip_amount(self):
        return round(self.price * 0.15, 2)
    
    def display(self):
        return f"{self.dish}: ${self.price:.2f}"
    
class HappyHourOrder(Order):
    def __init__(self, dish, price, discount):
        super().__init__(dish, price)
        if not 0 < discount < 1:
            raise ValueError("Discount should be between 0 and 1")
        self.discount = discount

    def final_price(self):
        return round(self.price * (1 - self.discount), 2)
    
    def tip_amount(self):
        return self.final_price() * 0.15
    
    def display(self):
        return f"{super().display()} -> ${self.final_price():.2f} (-{int(self.discount * 100)}%)"
    
class DeliveryOrder(Order):
    def __init__(self, dish, price, delivery_rate):
        super().__init__(dish, price)
        self.delivery_rate = delivery_rate

    def tip_amount(self):
        return round(self.price * 0.15 + self.price * self.delivery_rate, 2)
        
    def display(self):
        return f"{self.dish}: ${self.price:.2f} (delivery, fee {int(self.delivery_rate * 100)}%)"
        
class LoyaltyReward:
    def __init__(self, dish, price):
        self.dish = dish
        self.price = 0

    def tip_amount(self):
        return 0.0
    
    def display(self):
        return f"{self.dish}: $0.00 (loyalty reward)"
    
class BillSummary:
    def __init__(self):
        self.lines = []

    def add_line(self, description, tip):
        self.lines.append((description, tip))

    def print_bill(self):
        for line in self.lines:
            print(f"  {line[0]} | tip: ${line[1]:.2f}")
    
class TableBill:
    def __init__(self, guest_name):
        self.guest_name = guest_name
        self.orders = []
        self.bill_summary = BillSummary()

    def add_order(self, order):
        self.orders.append(order)

    def close(self):
        print(f"Bill for {self.guest_name}")
        subtotal = 0
        total_tips = 0
        for order in self.orders:
            self.bill_summary.add_line(order.display(), order.tip_amount())
            subtotal += order.price
            total_tips += order.tip_amount()
        self.bill_summary.print_bill()
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Total Tips: ${total_tips:.2f}")
        print(f"Grand Total: ${subtotal + total_tips}")

bill = TableBill('Jasur')

bill.add_order(Order('Steak', 45))
bill.add_order(HappyHourOrder('Cocktail', 20, 0.50))
bill.add_order(DeliveryOrder('Sushi Set', 30, 0.20))
bill.add_order(LoyaltyReward('Free Dessert', 0))

try:
    bill.add_order(Order('Bad Dish', -15))
except ValueError as e:
    print(f'Skipped: {e}')

bill.close()

try:
    b = Billable()
except TypeError:
    print('Cannot instantiate abstract class')
