import pandas as pd

class Pricing:

    def __init__(self):
        data = {
            'CODE': ['VOUCHER', 'TSHIRT', 'PANTS'],
            'NAME': ['Gift Card', 'Summer T-Shirt', 'Summer Pants'],
            'PRICE': [5.00, 20.00, 7.50]
        }
        df = pd.DataFrame(data)
        self.pricing_rules = {
            'VOUCHER': {
                'price': df.loc[df['CODE'] == 'VOUCHER', 'PRICE'].values[0]
            },
            'TSHIRT': {
                'min_count': 3,
                'discount_price': 19.00,
                'price': df.loc[df['CODE'] == 'TSHIRT', 'PRICE'].values[0]
            }
        }

    def set_pricing_rules(self, pricing_rules):
        self.pricing_rules = pricing_rules

    def get_pricing_rules(self):
        return self.pricing_rules