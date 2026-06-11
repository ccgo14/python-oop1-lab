class Coffee:
    VALID_SIZES = ["Small", "Medium", "Large"]
    
    def __init__(self, size, price):
        self.price = price
        self._size = None
        self.size = size
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value in self.VALID_SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
    
    def tip(self):
        self.price += 1
        # FIX: Use curly apostrophe (’) not straight (')
        print("This coffee is great, here’s a tip!")
