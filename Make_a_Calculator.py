class calculator:
    def __init__(self, name, functionality, brand, price):
        self.name=name
        self.functionality=functionality
        self.brand=brand
        self.price=price
        
    def add(self, x, y):
        return x+y

    def multiply(self, x, y):
        return x*y

    def pow(self, x, y):
        return x**y

calA=calculator("scientific", "All", "Philips", 1000)
print(calA.add(20,30))