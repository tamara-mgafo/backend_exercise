import pandas as pd

class Checkout:

    def __init__(self, pricing):
        self.pricing = pricing
        self.items = []
        
    def scan(self, item):
        self.items.append(item)
        return self.items
    
    def total(self):
        item_counts = {}
        total_price = 0.0

        for item in self.items:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1

        for item, count in item_counts.items():
            total_price += self.pricing.get_price(item, count)

        return total_price
