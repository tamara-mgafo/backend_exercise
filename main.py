from src.pricing import Pricing
from src.checkout import Checkout 


class Main:

    def __init__(self):
        pricing=Pricing()
        pricing_rules = pricing.get_pricing_rules()
        checkout = Checkout(pricing_rules)  # Crear instancia de checkout
        print(pricing_rules)

        while True:
            item = input("Introzuca el código del producto o 'EXIT' para finalizar: ")
            if item == "EXIT":
                break
            else:
                checkout.scan(item)
                print(checkout.result_total())

if __name__ == "__main__":
    Main()
            
