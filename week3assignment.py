class CartItem:
    def __init__(self, book_title, unit_price, copies):
        self.book_title = book_title
        self.unit_price = unit_price
        self.copies = copies
    
    def __str__(self):
        return f"{self.book_title}: {self.copies} copy(ies) at ${self.unit_price}"
    
    def __repr__(self):
        return f"CartItem('{self.book_title}', {self.unit_price}, {self.copies})"
    
    def __add__(self, other):
        if isinstance(other, CartItem):
            if self.book_title != other.book_title:
                return NotImplemented
            return CartItem(self.book_title, self.unit_price, self.copies + other.copies)
        elif isinstance(other, int):
            return CartItem(self.book_title, self.unit_price, self.copies + other)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, CartItem):
            return self.book_title == other.book_title and self.unit_price == other.unit_price
        return NotImplemented
    
    def __bool__(self):
        return self.copies > 0
    
item1 = CartItem("Python 101", 20.0, 1)
item2 = CartItem("Python 101", 20.0, 4)
item3 = CartItem("Data Science", 35.0, 0)

print(str(item1))
print(repr(item1))
print(item1 + item2)
print(item1 + 2)
print(item1 == item2)
print(bool(item1))
print(bool(item3))
