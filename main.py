from src.pricing import Pricing
from src.checkout import Checkout 

class Main:

    def __init__(self):
        pricing=Pricing()
        checkout = Checkout(pricing) 

        while True:
            item = input("Introzuca el código del producto o 'EXIT' para finalizar: ").strip().upper()
            if item == "EXIT":
                break
            else:
                checkout.scan(item)
                print(checkout.total())

if __name__ == "__main__":
    Main()
            
