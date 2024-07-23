import src.checkout as checkout

class main():

    while True:
        item = input("Introzuca el código del producto o 'EXIT' para finalizar: ")
        if item == "EXIT":
            break
        else:
            checkout.scan(item)

            
