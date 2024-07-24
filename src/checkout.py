class Checkout:

    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.items = []
        
    def scan(self, item):
        self.items.add(item)
        return self.items
    
    #def total_pricing():