import pandas as pd

class Pricing:

    def __init__(self):
        data = {
            'CODE': ['VOUCHER', 'TSHIRT', 'PANTS'],
            'NAME': ['Gift Card', 'Summer T-Shirt', 'Summer Pants'],
            'PRICE': [5.00, 20.00, 7.50]
        }
        self.df = pd.DataFrame(data)
        self.pricing_rules = {
            'VOUCHER': {
                'price': self.df.loc[self.df['CODE'] == 'VOUCHER', 'PRICE'].values[0]
            },
            'TSHIRT': {
                'min_count': 3,
                'discount_price': 19.00,
                'price': self.df.loc[self.df['CODE'] == 'TSHIRT', 'PRICE'].values[0]
            }
        }
        
    def get_price(self, item, count):
        if item in self.pricing_rules:
            rule = self.pricing_rules[item]
            if item == 'VOUCHER':
                return (count // 2 + count % 2) * rule['price']
            elif item == 'TSHIRT' and count >= rule['min_count']:
                return count * rule['discount_price']
            else:
                return count * rule['price']
        else:
            return count * self.df.loc[self.df['CODE'] == item, 'PRICE'].values[0]
