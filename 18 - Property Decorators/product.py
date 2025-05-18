# Assignment:
# Create a class Product with a private attribute _price. 
# Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        """Getter for price"""
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price"""
        print("Setting price...")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter for price"""
        print("Deleting price...")
        del self._price

# Demonstration
product = Product(100)

# Using getter
print(product.price)  

# Using setter
product.price = 150   
print(product.price)  

# Trying to set invalid price
try:
    product.price = -50  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Price cannot be negative

# Using deleter
del product.price 

# Now price attribute doesn't exist
try:
    print(product.price)
except AttributeError as e:
    print("Price attribute has been deleted")  #